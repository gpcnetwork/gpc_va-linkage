#####################################################################     
# Copyright (c) 2021-2025 University of Missouri                   
# Author: Xing Song, xsm7f@umsystem.edu                            
# File: utils.py                                                 
# Description: utility functions for stage_hashtoken.py                                      
#####################################################################

import os
import boto3
from botocore.exceptions import ClientError
import logging
import requests
import pandas as pd
import io
import zipfile
import psutil
import time
import zipfile
import urllib
import py7zr
from dataclasses import dataclass
from abc import ABC, abstractmethod

def get_objects(bucket_name,subfolder=None,s3_client=None)->dict:
    """
    bucket_name: string
    returns a dictionary: key: folder name, value: list of object names
    """
    if s3_client is None:
        s3_client = boto3.client('s3') # Using the default session
    response = s3_client.list_objects(Bucket=bucket_name)
    # Iterate over the content of the bucket and retreive folders and contents
    request_files = response["Contents"]
    filenames = {}
    mod_dates = []
    for file in request_files:
        path, filename = os.path.split(file['Key'])
        mod_dates.append(file['LastModified'].strftime('%Y%m%d'))
        if filename != '':
            if path not in filenames:
                filenames[path] = [filename]
            else:
                filenames[path].append(filename)
    # flattened
    if subfolder:
        filenames_cp = filenames
        mod_dates_cp = mod_dates
        filenames = {}
        filenames[''] = []
        mod_dates = []
        idx_counter = 0
        for key, val in filenames_cp.items():
            if key.startswith(subfolder):
                mod_dates.append(mod_dates_cp[idx_counter])
                filenames[''].extend(val)
    # attach modified dates
    filenames['modified_date'] = mod_dates
    return filenames

def load_meta_pcornet_url(url:str,sheet:str,tbl_col:str,var_col:str,dtype_col:str,exclude_raw_col=False)->dict:
    # get metadata content from the pcornet url link
    # url: https://pcornet.org/wp-content/uploads/2021/11/2021_11_29_PCORnet_Common_Data_Model_v6dot0_parseable.xlsx
    resp = requests.get(url)
    resp_df = pd.read_excel(resp.content,sheet_name=sheet)
    
    # force remove RAW columns
    if exclude_raw_col:
        resp_df = resp_df[~resp_df[var_col].str.startswith('RAW')]
    
    # # filter out RAW columns for better efficiencies
    # resp_df = resp_df[~resp_df[var_col].str.contains('RAW_')]
    
    # create a new column of lists with metadata info for each variable
    resp_df['data_type'] = resp_df[dtype_col].str.split('(', 1).str[0].str.split('SAS',1).str[1].str.strip().str.upper()
    resp_df['meta_col'] = resp_df[[var_col,'data_type']].values.tolist()
    resp_df = resp_df[[tbl_col,"meta_col"]]
    
    # convert into dictionary with table_name as key and [tbl_col,dtype_col] as val
    resp_dict = resp_df.groupby(tbl_col)['meta_col'].apply(list).to_dict()
    return(resp_dict)

def amend_metadata(old:list,new:dict)->list:
    old_keys = [i for i, j in old]
    meta = []
    for key in new.keys():
        key = key.upper()
        try:
            key_loc = old_keys.index(key) 
            meta.append(old[key_loc])
        except: 
            meta.append([key,'CHAR']) # data type char for all fields, as it is more generalizable
    return(meta)
    
def get_benchmark()->list:
    # return the time in seconds since the epoch (the epoch is January 1, 1970, 00:00:00 (UTC)) 
    t = time.time()
    # get current available memory (negative number to)
    m = -1*psutil.virtual_memory().available*1e-6
    # get current free disk
    d = -1*psutil.disk_usage('/').free*1e-6
    return([t,m,d])

def download_zip(url:str,path_to_folder='default')->list:
    if path_to_folder == 'default':
        path_to_folder = f'{os.path.abspath(os.path.dirname(__file__))}/tmp_dir'
    resp = urllib.request.urlopen(url)
    zipped_file = zipfile.ZipFile(io.BytesIO(resp.read()))
    zipped_file.extractall(path_to_folder) # by default, it will be a tmp_dir under the same parent folder of this script
    file_lst = zipped_file.namelist()
    print(f'{file_lst} downloaded and unpacked!')

@dataclass
class zipped_file_s3(ABC):
    """representation of a zipped file object in s3 bucket"""
    src_bucket:str
    src_key:str
    tgt_bucket:str
    tgt_prefix:str

    @abstractmethod
    def unzip_and_upload(self,verb=True)->None:
        """unzip file on local disk and upload to target location in s3"""
        if verb:
            print("unzip file from ",f'{self.src_bucket}/{self.src_key}'," to ",f'{self.tgt_bucket}/{self.tgt_prefix}')

@dataclass
class zipped_zip(zipped_file_s3):
    """files compressed using conventional zip technique"""
    # https://medium.com/@johnpaulhayes/how-extract-a-huge-zip-file-in-an-amazon-s3-bucket-by-using-aws-lambda-and-python-e32c6cf58f06
    def unzip_and_upload(self):
        # read zip file into a BytesIO buffer object
        s3_resource = boto3.resource('s3')
        zip_obj = s3_resource.Object(
            bucket_name=self.src_bucket, 
            key=self.src_key
        )
        buffer = io.BytesIO(zip_obj.get()["Body"].read())
        # upload individual zipped file into a target bucket
        z = zipfile.ZipFile(buffer)
        for filename in z.namelist():
            file_info = z.getinfo(filename)
            tgt_key = f'{self.tgt_prefix}/{filename}'
            s3_resource.meta.client.upload_fileobj(
                z.open(filename),
                Bucket=self.tgt_bucket,
                Key=tgt_key
            )
        # return extracted file names
        return z.namelist() 

@dataclass
class zipped_7z(zipped_file_s3):
    """files compressed using 7-zip technique"""
    def unzip_and_upload(self):
        # download 7z-like file to local disk
        s3 = boto3.resource('s3')
        s3.download_fileobj(
            Bucket  = self.src_bucket, 
            Key = self.src_key
        )
        zipname = self.src_key.rsplit('/',1)[-1]
        # collect all file names
        with py7zr.SevenZipFile(zipname, 'r') as zip:
            allfiles = zip.getnames()
        # extract and upload
        with py7zr.SevenZipFile(zipname, 'r') as zip:
            for filename in allfiles:
                zip.extract(targets=filename)
                tgt_key = f'{self.tgt_prefix}/{filename}'
                s3.upload_file(
                    Filename = filename,
                    Bucket=self.tgt_bucket,
                    Key=tgt_key
                )
        # return extracted file names
        return allfiles 

def copy_file_to_folder(bucket_name,src_file,tgt_folder,tgt_file=None,verb=True):
    """
    bucket_name: s3 bucket needs to be organized
    src_file: source file; 
      - could be either full name of a single file (contains '.'), or 
      - folder name (must end with '/'), or
      - file name pattern directly under bucket (e.g., zip)
    tgt_folder: target folder;
    tgt_file: to change file name in target folder. NOTE this is only allowed when copying a single file
    """
    if(src_file.endswith('/')):
        # input is a folder
        file_lst = get_objects(bucket_name,subfolder=src_file[:-1])['']
        file_lst = [f'{src_file}{x}' for x in file_lst]
    elif('.' not in src_file and '/' not in src_file):
        # input is a file type or name pattern
        file_lst = get_objects(bucket_name)['']
        file_lst = [x for x in file_lst if src_file in x]
    elif('.' in src_file):
        # input is a single file
        file_lst = []
        file_lst.extend([src_file])
    else:
        exit("src_file should either contain '.' for single file or end with '/' for folder or '*.<file-type>' for file type!")
    # s3 bucket copy 
    s3 = boto3.resource('s3')
    for key in file_lst:
        # https://stackoverflow.com/questions/47468148/how-to-copy-s3-object-from-one-bucket-to-another-using-python-boto3
        copy_source = {
              'Bucket': bucket_name,
              'Key': key
        }
        file_key = key.rsplit('/', 1)[-1]
        if tgt_file is not None:
            file_key = tgt_file
        tgt_key = f'{tgt_folder}/{file_key}'
        s3.meta.client.copy(
            copy_source,
            bucket_name,
            tgt_key
        )
        if(verb): print(f'{key} copied to {tgt_key}')

def Download_S3Objects(bucket_name,path_to_src_obj,download_file,s3_client=None,verbose=True)->None:
    # download data to local storage
    if s3_client is None:
        s3_client = boto3.client('s3') # Using the default session
    s3_client = boto3.resource('s3')
    s3_bucket = s3_client.Bucket(bucket_name)
    s3_bucket.download_file(
        Key = path_to_src_obj,
        Filename = download_file
    )
    if verbose: 
        print(f'file {path_to_src_obj} downloaded!')

def Upload_S3Objects(path_to_file,bucket_name,tgt_key,s3_client=None)->None:
    # initialize s3 client
    if s3_client is None:
        s3_client = boto3.client('s3') # Using the default session
    # upload_file from disk to s3
    try:
        s3_client.upload_file(
            Filename = path_to_file, 
            Bucket_name = bucket_name, 
            Key = tgt_key
        )
    except ClientError as e:
        logging.error(e)



def pyclean():
    os.popen('find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf')