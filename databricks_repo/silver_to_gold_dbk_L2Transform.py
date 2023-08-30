# Databricks notebook source
dbutils.fs.ls('mnt/silver/SalesLT/')

# COMMAND ----------

input_path = 'mnt/silver/SalesLT/Address/'

# COMMAND ----------

df = spark.read.format('delta').load(input_path)

# COMMAND ----------

display(df)

# COMMAND ----------

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, regexp_replace
#getting the list of column names
column_names = df.columns

for old_col_name in column_names:
    #convert the column name from ColumnName to Column_Name format
    new_col_name = "".join(["_"+char if char.isupper() and not old_col_name[i-1].isupper() else char for i, char in enumerate(old_col_name)]).lstrip("_")

    #Changing the column name using withColumnRenamed
    df = df.withColumnRenamed(old_col_name,new_col_name)

# COMMAND ----------

display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Transformation - Changing column names of all tables

# COMMAND ----------


table_name =[]
for i in dbutils.fs.ls('/mnt/silver/SalesLT/'):
    table_name.append(i.name.split('/')[0])

# COMMAND ----------

table_name

# COMMAND ----------

for name in table_name:
    path = '/mnt/silver/SalesLT/'+name
    print(path)
    df = spark.read.format('delta').load(path)
    column_names = df.columns
    for old_col_name in column_names:
        #convert the column name from ColumnName to Column_Name format
        new_col_name = "".join(["_"+char if char.isupper() and not old_col_name[i-1].isupper() else char for i, char in enumerate(old_col_name)]).lstrip("_")

        #Changing the column name using withColumnRenamed
        df = df.withColumnRenamed(old_col_name,new_col_name)
    output_path = '/mnt/gold/SalesLT/'+name+'/'
    df.write.format('delta').mode("overwrite").save(output_path)


# COMMAND ----------


