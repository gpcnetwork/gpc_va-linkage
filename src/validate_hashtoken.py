#####################################################################     
# Copyright (c) 2021-2025 University of Missouri                   
# Author: Xing Song, xsm7f@umsystem.edu                            
# File: validate_hashtoken.py                                                 
# Description: validate aggregated hashtoken csv file                                       
#####################################################################

import pandas as pd

# load from local disk
df = pd.read_csv('gpc-va-hashtoken-20230407.csv')

# summarize counts
df_summ = df.groupby(['SITEID'])['PATID'].count()
print(df_summ)