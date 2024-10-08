'''
Steps-
1.import pyspark library
2.build session
3.call sql module
4. read JSON file
'''
import pandas
import findspark

findspark.init()

# import json
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
import pandas

# create session
spark = SparkSession.builder.getOrCreate()

# readding file
df = spark.read.option("multiline", "true").json(r"D:\Souce_files\sample_JSON\Govement_data\City_bus.JSON")
df1 = df.select(["fields", "data"])
df1.show(n=5)
# nested JSOn file parsing and writing to table in MYSQL


df2 = df1.withColumn('fields', explode(col("fields")))
df3 = df2.withColumn('data', explode(col("data")))
df3.printSchema()
# separating columns from data column
df4 = df3.select(df3.data[0].alias("ID"), df3.data[1].alias("Label"), df3.data[2].alias("Type"))
# converting ID to integer type
df5 = df4.withColumn("ID", df4["ID"].cast('integer'))
# removing duplicate values
df6 = df5.distinct().orderBy("ID")

# writing data to
PD_DF = df6.toPandas()
PD_DF.to
print(PD_DF.head(6))
