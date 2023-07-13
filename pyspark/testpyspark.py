import pandas as pd
from sqlalchemy import create_engine
import findspark

url = 'mysql://Rohit:Hulk1998@database-1.cvn6jr6crdmc.eu-north-1.rds.amazonaws.com:3306'
findspark.init()

engine = create_engine(url)
my_conn = engine.connect()
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

print(my_conn)
spark = SparkSession.builder.getOrCreate()

data = pd.read_csv("D:\Souce_files\sample_CSV\email.csv", sep=';', header=0)

data.to_sql('FinalDB', con=my_conn, if_exists='replace', index=False, method='multi')
df.show(n=5)
