# Databricks notebook source
dbutils.fs.ls('mnt/bronze/SalesLT')

# COMMAND ----------

input_path ='/mnt/bronze/SalesLT/Address/Address.parquet'
df = spark.read.format('parquet').load(input_path)

# COMMAND ----------

display(df)

# COMMAND ----------

df.show(10)

# COMMAND ----------


