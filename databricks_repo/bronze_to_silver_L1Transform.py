# Databricks notebook source
dbutils.fs.ls('mnt/bronze/SalesLT')

# COMMAND ----------

input_path ='/mnt/bronze/SalesLT/Address/Address.parquet'
df = spark.read.format('parquet').load(input_path)

# COMMAND ----------

display(df)

# COMMAND ----------

# converting the modified column to date format
from pyspark.sql.functions import from_utc_timestamp, date_format
from pyspark.sql.types import TimestampType
df = df.withColumn("ModifiedDate",date_format(from_utc_timestamp(df["ModifiedDate"].cast(TimestampType()),"utc"),"yyyy-MM-dd"))

# COMMAND ----------

# MAGIC %md
# MAGIC ##Doing Transformations for all tables

# COMMAND ----------

table_name = []
for i in dbutils.fs.ls('mnt/bronze/SalesLT'):
    table_name.append(i.name.split('/')[0])
table_name

# COMMAND ----------

from pyspark.sql.functions import from_utc_timestamp, date_format
from pyspark.sql.types import TimestampType
for i in table_name:
    path = '/mnt/bronze/SalesLT/'+i+'/'+i+'.parquet'
    df = spark.read.format('parquet').load(path)
    column = df.columns
    for col in column:
        if "date" in col or "Date" in col:
            df=df.withColumn(col,date_format(from_utc_timestamp(df[col].cast(TimestampType()),"UTC"),"yyyy-MM-dd"))
    output_path = '/mnt/silver/SalesLT/'+i+'/'
    df.write.format('delta').mode("overwrite").save(output_path)

# COMMAND ----------

display(df)

# COMMAND ----------


