import os
import time
import csv

path = "/Users/rahulprajapat/Desktop"


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

#####for all things in the folder

# for entry in os.listdir(path):
#     if os.path.isfile(os.path.join(path, entry)):
#         df = [entry, " " + os.path.join(path, entry), " " + assess_time," " + creation_time, " " + modification_time]
#         li.append(df)

# with open('file2.csv', 'w') as csvfile:
#     csv_writer = csv.writer(csvfile)
#     csv_writer.writerow(fields_name)
#     csv_writer.writerows(li)
            




##### for all py files

# for file in os.listdir(path):
#     if os.path.isfile(os.path.join(path, file)):
#         df = [file, " " + os.path.join(path, file), " " + assess_time," " + creation_time, " " + modification_time]
#         li.append(df)
        

with open('file2.csv', 'w') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(fields_name)
    csv_writer.writerows(li)
            
        