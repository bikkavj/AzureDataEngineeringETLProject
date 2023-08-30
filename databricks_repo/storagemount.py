# Databricks notebook source
#mounting BRONZE container
container_name = "bronze"
storage_account = "bikkavjdatalakegen2"
key = "7+RPo5NThGZ3vZEtOZ2DQct1oGtQVLy3lK0XJZu8oO3+ZAyPYQLAxrOSHgRdKJ23uq2Z8DLULNVa+AStrJ4Leg=="
url = "wasbs://" + container_name + "@" + storage_account + ".blob.core.windows.net/"
config = "fs.azure.account.key." + storage_account + ".blob.core.windows.net"

mount_folder = "/mnt/bronze"
mounted_list = dbutils.fs.mounts()

mounted_exist = False
for item in mounted_list:
    if mount_folder in item[0]:
        mounted_exist = True
        break

if not mounted_exist:
    dbutils.fs.mount(source = url, mount_point = mount_folder, extra_configs = {config : key})

# COMMAND ----------

#mounting SILVER container
container_name = "silver"
storage_account = "bikkavjdatalakegen2"
key = "7+RPo5NThGZ3vZEtOZ2DQct1oGtQVLy3lK0XJZu8oO3+ZAyPYQLAxrOSHgRdKJ23uq2Z8DLULNVa+AStrJ4Leg=="
url = "wasbs://" + container_name + "@" + storage_account + ".blob.core.windows.net/"
config = "fs.azure.account.key." + storage_account + ".blob.core.windows.net"

mount_folder = "/mnt/silver"
mounted_list = dbutils.fs.mounts()

mounted_exist = False
for item in mounted_list:
    if mount_folder in item[0]:
        mounted_exist = True
        break

if not mounted_exist:
    dbutils.fs.mount(source = url, mount_point = mount_folder, extra_configs = {config : key})

# COMMAND ----------

#mounting GOLD container
container_name = "gold"
storage_account = "bikkavjdatalakegen2"
key = "7+RPo5NThGZ3vZEtOZ2DQct1oGtQVLy3lK0XJZu8oO3+ZAyPYQLAxrOSHgRdKJ23uq2Z8DLULNVa+AStrJ4Leg=="
url = "wasbs://" + container_name + "@" + storage_account + ".blob.core.windows.net/"
config = "fs.azure.account.key." + storage_account + ".blob.core.windows.net"

mount_folder = "/mnt/gold"
mounted_list = dbutils.fs.mounts()

mounted_exist = False
for item in mounted_list:
    if mount_folder in item[0]:
        mounted_exist = True
        break

if not mounted_exist:
    dbutils.fs.mount(source = url, mount_point = mount_folder, extra_configs = {config : key})

# COMMAND ----------


