import findspark

findspark.init()
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
df = spark.sql('''select 'spark' as hello''')
df.show()
