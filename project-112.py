import os
import shutil

from_dir="/Users/apple/Downloads"
to_dir="/Users/apple/Desktop"

list_of_file=os.listdir(from_dir)
print(list_of_file)

for file_name in list_of_file:
    name,extension=os.path.splitext(file_name)
    if extension == "":
        continue
    if extension in [".tox",".doc",".docx",".pdf"]:
        path1= from_dir + '/'+ file_name
        path2=to_dir + '/'+ "images_file"
        path3=to_dir + '/'+ "images_file" + '/' + file_name


        if os.path.exists(path2):
            print("Moving the"+file_name+".....")
            shutil.move(path1,path3)

        else:
            os.mkdir(path2)
            print("Moving the"+file_name+".....")
            shutil.move(path1,path3)

