import findspark

findspark.init()
# Read avro file into dataframe

import pyspark
from pyspark.sql import SparkSession
from pyspark.sql import Column
from pyspark.conf import SparkConf

conf=SparkConf()
conf.set("spark.jars.packages","com.databricks:spark-avro_2.11:4.0.0")


spark=SparkSession.builder.config(conf=conf).getOrCreate()

df=spark.read.format('avro').load(r"D:\sample_avro_file\train.avro")

df.show()