# reading a excel file
import xlrd
import pandas as pd


df = pd.read_excel(r'D:\git\python_-codes_-and_projects\sample_excel_Files\file_example_XLS.xls')

print(df)
