'''
Steps-
1.import pyspark library
2.build session
3.call sql module
4. read JSON file
'''

import findspark

findspark.init()

# import json
from pyspark.sql import SparkSession
from pyspark.sql.functions import explode

spark = SparkSession.builder.getOrCreate()

df = spark.read.option("multiline", "true").json(r"D:\git\python_-codes_-and_projects\sample_JSON\sample2.json")
df.printSchema()
df.show()
df.select('age').show()

print("after exploding")
df2 = df.select(explode(df.address))
df2.printSchema()
df2.show()
