import findspark

findspark.init()
from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()

dfav=spark.read.
#dfav.show()
