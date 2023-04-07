#####################################################################     
# Copyright (c) 2021-2025 University of Missouri                   
# Author: Xing Song, xsm7f@umsystem.edu                            
# File: stage_hashtoken.py                                                 
# Description: automate hash token integration and transfer workflow
# - move file from current location to pre-stage source/ folder
# - copy or unzip from source/ to extract/ 
# - load into to memory and add SITEID
# - download to disk as csv file
# - append csv to the integrated hash token table                                       
#####################################################################

import utils 
import pandas as pd
import csv
from datetime import datetime
import gc
import os

#diagnosic mode
diagnostic_mode = False

#if skip download
skip_download = False

#if skip unzip and copy from source/ to extract/
skip_copy = True

#tagged date
proc_date = datetime.today().strftime('%Y%m%d')

#possible zip types
zip_types = [
    ".zip",    
    ".7z",
    ".gz"
]

#loop over gpc sites
gpc_dict = {
    'mu':'S00',
    'allina':'S01',
    'ihc':'S02',
    'kumc':'S03',
    'mcri':'S04',
    'mcw':'S05',
    # 'uiowa':'S06',
    'unmc':'S07',
    'uthouston':'S08',
    'uthscsa':'S09',
    'utsw':'S10',
    'uu':'S11',
    'washu':'S12'
}


#==== loop over files
for idx, site in enumerate(gpc_dict):
    gc.collect()
    
    # reconstruct source bucket name and target schema name
    src_bucket = f'gpc-{site}-upload'   # make sure the bucket/subfolder name structure is correct
    src_prefix = 'va-linkage-pilot/source'
    
    # identify file
    src_objs = utils.get_objects(bucket_name=src_bucket,subfolder=src_prefix)
    max_mod_date = max(src_objs['modified_date'])
    max_pos = src_objs['modified_date'].index(max_mod_date)
    src_file = src_objs[''][max_pos]
    src_key = f'{src_prefix}/{src_file}'
    
    #=====================================================
    if diagnostic_mode: print(src_key,":",max_mod_date)
    #=====================================================

    tgt_prefix = 'va-linkage-pilot/extract'
    if any(zt in src_file for zt in zip_types):
        if '.zip' in src_file:
            zip_obj = utils.zipped_zip(
                src_bucket = src_bucket, src_key = src_key,
                tgt_bucket = src_bucket, tgt_prefix = tgt_prefix    
            )
        elif '.gz' in src_file:
            zip_obj = utils.zipped_gz(
                src_bucket = src_bucket, src_key = src_key,
                tgt_bucket = src_bucket, tgt_prefix = tgt_prefix    
            )
            skip_download = False
        elif '.7z' in src_file:
            zip_obj = utils.zipped_7z(
                src_bucket = src_bucket, src_key = src_key,
                tgt_bucket = src_bucket, tgt_prefix = tgt_prefix    
            )
            skip_download = False
        src_file = zip_obj.unzip_and_upload()[0]
    else:
        # copy over to target location
        if not skip_copy:
            utils.copy_file_to_folder(
                bucket_name = src_bucket,
                src_file = src_key,
                tgt_folder = tgt_prefix)

    # load unzipped csv file from disk
    if not skip_download:
        tgt_key = f'{tgt_prefix}/{src_file}'
        utils.Download_S3Objects(src_bucket,tgt_key,src_file)
    
    # sites may submit illegal formated files
    delim = '|'
    if site in ['mu','ihc','uthouston']:
        delim = None 
    df = pd.read_csv(
        src_file,
        delimiter = delim,
        names=['PATID','TOKEN_1','TOKEN_2','TOKEN_3','TOKEN_4','TOKEN_5','TOKEN_16','TOKEN_ENCRYPTION_KEY'],
        header = None,
        skiprows = 1
    )
    
    #=====================================================
    if diagnostic_mode: print(df.head()); print(df.columns)
    #=====================================================
    
    # attach siteid
    side_idx = gpc_dict[site]
    df['SITEID'] = f'{side_idx}'
    
    #=====================================================
    if diagnostic_mode: print(df.head()); print(df.columns)
    #=====================================================
    
    # download to disk and append to existing file
    file_name = f'gpc-va-hashtoken-{proc_date}.csv'
    with open(file_name, 'a') as f:
        #https://stackoverflow.com/questions/30991541/pandas-write-csv-append-vs-write
        df.to_csv(f, mode='a', header=f.tell()==0,index=False)
    
    # get sample for each file
    file_name = f'gpc-va-hashtoken-{proc_date}-sample.csv'
    with open(file_name, 'a') as f:
        #https://stackoverflow.com/questions/30991541/pandas-write-csv-append-vs-write
        df.sample(5).to_csv(f, mode='a', header=f.tell()==0,index=False)
    
    # get summary for each file
    df_summ = df.groupby(['SITEID'])['PATID'].count()
    file_name = f'gpc-va-hashtoken-{proc_date}-summ.csv'
    with open(file_name, 'a') as f:
        #https://stackoverflow.com/questions/30991541/pandas-write-csv-append-vs-write
        df_summ.to_csv(f, mode='a', header=f.tell()==0)
    
    # remove appended file form disk
    os.remove(src_file)

'''
#===== upload from local disk to s3 bucket
utils.Upload_S3Objects(
    path_to_file = f'{file_name}.csv',
    bucket_name = 'nextgenbmi-snowpipe-master', # require put permission to the target bucket
    tgt_key = f'{file_name}.csv'
)
'''
#=====
utils.pyclean()