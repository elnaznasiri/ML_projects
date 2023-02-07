import pandas as pd
import os
import shutil

OriginFile = 'D:\Programming\ML_projects\OutputFiles\stage\\3493882.csv'
df = pd.read_csv(OriginFile)

#Below line hold Nan records
NanRecords = pd.isnull(df['recommendation_status'])

#Below line hold not Nan records
NotNanRecords = pd.notnull(df['recommendation_status'])

#Select the columns that want to be in new file
header = ['productID','body', 'recommendation_status']

#Write NaN and not NaN records to seperate files
df[NanRecords].to_csv('D:\Programming\ML_projects\OutputFiles\Test\\3493882.csv', columns = header)
df[NotNanRecords].to_csv('D:\Programming\ML_projects\OutputFiles\Train\\3493882.csv', columns = header)

#After split the original file below code will remove and copy base file
shutil.copy(OriginFile, 'D:\Programming\ML_projects\OutputFiles\OriginFile')
os.remove(OriginFile)