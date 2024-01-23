import os
import shutil

if not os.path.exists("Data"):
    os.mkdir("Data")

for file in os.listdir():
    shutil.copy2(file, "Data")
    #to move file use
    shutil.move(file,"dest_folder")
    #delete file use
    os.remove('filename')
    #delete  empty directory use
    os.rmdir("Data")
    #delete non empty directory use
    shutil.rmtree("Data")