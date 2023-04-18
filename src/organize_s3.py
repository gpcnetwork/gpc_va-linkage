#####################################################################     
# Copyright (c) 2021-2025 University of Missouri                   
# Author: Xing Song, xsm7f@umsystem.edu                            
# File: organize_s3.py                                                 
# After data is properly staged, we want to move from source folder 
# to extact folder
#####################################################################

import os
import json
import boto3
from botocore.exceptions import ClientError
from utils import get_objects, copy_file_to_folder 

# load templated folder structure
dir_path = os.path.dirname(os.path.realpath(__file__))

#========================================================================================================
# mu
# copy_file_to_folder('gpc-mu-upload','tokenization_output_MU.csv','va-linkage-pilot/source/')
# copy_file_to_folder('gpc-mu-upload','tokenization_output_MU.csv','va-linkage-pilot/source/')
#========================================================================================================

#========================================================================================================
# allina
# copy_file_to_folder('gpc-allina-upload','tokenization_output_Allina.zip','va-linkage-pilot/source/')
#========================================================================================================

#========================================================================================================
# ihc
# copy_file_to_folder('gpc-ihc-upload','tokenization_output_intermountain.csv','va-linkage-pilot/source/')
# copy_file_to_folder('gpc-ihc-upload','va-linkage-pilot/GPC_VA_Datavant.txt','va-linkage-pilot/source','tokenization_output_ihc.txt')
# copy_file_to_folder('gpc-ihc-upload','va-linkage-pilot/GPC_VA_Datavant.txt','va-linkage-pilot/extract','tokenization_output_ihc.txt')
#========================================================================================================

#========================================================================================================
# kumc
# copy_file_to_folder('gpc-kumc-upload','tokenization_output_kumc.csv.gz','va-linkage-pilot/source/')
#========================================================================================================

#========================================================================================================
# mcri
# copy_file_to_folder('gpc-mcri-upload','tokenization_output_MCRI.csv','va-linkage-pilot/source/')
# copy_file_to_folder('gpc-mcri-upload','tokenization_output_MCRI.csv','va-linkage-pilot/extract/')
#========================================================================================================

#========================================================================================================
# mcw
# copy_file_to_folder('gpc-mcw-upload','tokenization_ouput_MCW_to_gpc_va.csv','va-linkage-pilot/source/')
# copy_file_to_folder('gpc-mcw-upload','tokenization_ouput_MCW_to_gpc_va.csv','va-linkage-pilot/extract/')
#========================================================================================================

#========================================================================================================
# uiowa
# copy_file_to_folder('gpc-uiowa-upload','tokenization_output_UI_without_PAT_ID.zip','va-linkage-pilot/source')
#========================================================================================================

#========================================================================================================
# unmc
# copy_file_to_folder('gpc-unmc-upload','tokenization_output_unmc.csv','va-linkage-pilot/source/')
# copy_file_to_folder('gpc-unmc-upload','tokenization_output_unmc.csv','va-linkage-pilot/extract/')
#========================================================================================================

#========================================================================================================
# uthouston
# copy_file_to_folder('gpc-uthouston-upload','tokenization_output_UTH.zip','va-linkage-pilot/source')
#========================================================================================================

#========================================================================================================
# uthscsa
# copy_file_to_folder('gpc-uthscsa-upload','tokenzation_output_c4uthscsa.csv','va-linkage-pilot/source')
# copy_file_to_folder('gpc-uthscsa-upload','tokenzation_output_c4uthscsa.csv','va-linkage-pilot/extract')
#========================================================================================================

#========================================================================================================
# utsw
# copy_file_to_folder('gpc-utsw-upload','university_texas_southwestern__gpc_va__12-12-2022_16-30-41-053_transform_output.txt','va-linkage-pilot/source/')
# copy_file_to_folder('gpc-utsw-upload','university_texas_southwestern__gpc_va__12-12-2022_16-30-41-053_transform_output.txt','va-linkage-pilot/extract/','tokenization_output_utsw.txt')
#========================================================================================================

#========================================================================================================
# uu
# copy_file_to_folder('gpc-uu-upload','tokenization_output_utah.csv','va-linkage-pilot/source/')
# copy_file_to_folder('gpc-uu-upload','tokenization_output_utah.csv','va-linkage-pilot/extract/')
#========================================================================================================

#========================================================================================================
# washu
# copy_file_to_folder('gpc-washu-upload','tokenization_output_washu.csv','va-linkage-pilot/source/')
# copy_file_to_folder('gpc-washu-upload','tokenization_output_washu.csv','va-linkage-pilot/extract/')
#========================================================================================================
