
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder.config("spark.ui.port", "4042").getOrCreate()
print("Spark UI:", spark.sparkContext.uiWebUrl)
# ...existing code...


data = [("Alice", 34), ("Bob", 45), ("Cathy", 29), ("David", 40), ("Eva", 38)]
columns = ["Name", "Age"]
df = spark.createDataFrame(data, columns)
df_filtered = df.filter(col("Age") > 35)
df_filtered.show()
