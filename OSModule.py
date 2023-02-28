import os
import time
import pandas as pd
import glob
import csv

path = "/Users/rahulprajapat/Desktop"

# l = os.listdir(path)
# print(l)

# x = glob.glob("*.py")
# print(x)


# Atime
time_of_last_assess = os.path.getatime(path)
assess_time = time.ctime(time_of_last_assess)
# Ctime
time_of_creation = os.path.getctime(path)
creation_time = time.ctime(time_of_creation)
# Mtime
time_of_modification = os.path.getmtime(path)
modification_time = time.ctime(time_of_modification)




li = []

fields_name = ["file_name", "file_path", "file_ctime", "file_mtime", "file_atime"]

for root, dirs, files in os.walk(path):
    for f in files:
        df = [f," " + os.path.join(root, f), " " + creation_time," " + modification_time," " + assess_time]
        li.append(df)
# print(li)
            

with open('file.csv', 'w') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(fields_name)
    csv_writer.writerows(li)
            

            
            
            















