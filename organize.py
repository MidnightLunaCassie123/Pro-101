import os
import shutil

from_dir="G:/Other computers/My Laptop/BYJUs coding class work/class 102/C102_assets-main/assets"
to_dir="G:/Other computers/My Laptop/BYJUs coding class work/class 102/C102_assets-main/assets"

list_of_file=os.listdir(from_dir)

for file_name in list_of_file:
    name,extension=os.path.splitext(file_name)

    if extension=="":
        continue
    if extension in [".gif",".png",".jpeg",".jfif","jpg"]:
        path1=from_dir+"/"+file_name
        path2=to_dir+"/"+"image_files"
        path3=to_dir+"/"+"image_files"+"/"+file_name

        if os.path.exists(path2):
            print("Moving "+file_name+"....")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("Moving "+file_name+"....")
            shutil.move(path1,path3)