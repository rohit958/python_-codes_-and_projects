import findspark

findspark.init()

from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder.getOrCreate()

df = spark.read.format("com.databricks.spark.xml").option("rowTag", "DATASET").load(
    "D:\Souce_files\sample_XML_files\datafile.xml")

df.show(n=5)
