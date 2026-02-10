Automatic File Sorter in File Explorer

import os, shutil

path = r"C:/Users/HP/Documents/Python Libraries/"
file_name = os.listdir(path)
folders_name = ['csv files','text files','image files']

for loop in range(0,3):
  if not os.path.exists(path + folders_name[loop]):
    print(path + folders_name[loop])
    os.makedirs(path + folders_name[loop])

for file in file_name:
  if ".csv" in file and not os.path.exists(path + "csv files/" + file):
     shutil.move(path + file, path + "csv files/" + file)
  elif ".png" in file and not os.path.exists(path + "image files/" + file):
    shutil.move(path + file, path + "image files/" + file)
  elif ".txt" in file and not os.path.exixts(path + "text files/" + file):
    shutil.move(path + file, path + "text files/" + file)
