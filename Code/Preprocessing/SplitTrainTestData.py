import pandas as pd
import os

df = pd.read_csv('D:\Programming\ML_projects\OutputFiles\\3493882.csv')

#Below line hold Nan records
NanRecords = pd.isnull(df['recommendation_status'])

#Below line hold not Nan records
NotNanRecords = pd.notnull(df['recommendation_status'])

#Select the columns that want to be in new file
header = ['productID','body', 'recommendation_status']

#Write NaN and not NaN records to seperate files
df[NanRecords].to_csv('D:\Programming\ML_projects\OutputFiles\Test\\3493882.csv', columns = header)
df[NotNanRecords].to_csv('D:\Programming\ML_projects\OutputFiles\Train\\3493882.csv', columns = header)

#After split the original file below code will remove base file
os.remove('D:\Programming\ML_projects\OutputFiles\\3493882.csv')