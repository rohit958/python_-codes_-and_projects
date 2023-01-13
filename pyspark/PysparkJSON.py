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

spark = SparkSession.builder.getOrCreate()

def Read_JsonFile():
    df = spark.read.option("multiline","true").json("D:\git\python_-codes_-and_projects\sample_JSON\sample2.json")
    df.printSchema()
    df.show()


if __name__ == '__main__':
    Read_JsonFile()
