import pandas as pd
import os
import shutil

originFile = 'D:\Programming\ML_projects\OutputFiles\stage\\3493882.csv'
dataSet = pd.read_csv(originFile)

#Below line hold Nan records
NanRecords = pd.isnull(dataSet['recommendation_status'])

#Below line hold not Nan records
NotNanRecords = pd.notnull(dataSet['recommendation_status'])

#Select the columns that want to be in new file
header = ['productID','body', 'recommendation_status']

#Write NaN and not NaN records to seperate files
dataSet[NanRecords].to_csv('D:\Programming\ML_projects\OutputFiles\Test\\3493882.csv', columns = header)
dataSet[NotNanRecords].to_csv('D:\Programming\ML_projects\OutputFiles\Train\\3493882.csv', columns = header)

# #After split the original file below code will remove and copy base file
# shutil.copy(originFile, 'D:\Programming\ML_projects\OutputFiles\OriginFile')
# os.remove(originFile)

#TrainSet
originFile = 'D:\Programming\ML_projects\OutputFiles\Train\\3493882.csv'
trainSet = pd.read_csv(originFile)

#TestSet
originFile = 'D:\Programming\ML_projects\OutputFiles\Test\\3493882.csv'
testSet = pd.read_csv(originFile)