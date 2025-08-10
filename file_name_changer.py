import os

folder_path ='/home/neil/Pictures'
for count,filename in enumerate(os.listdir(folder_path),start=1):
    ext= os.path.splitext(filename)[1]
    new_name = f"image{count}{ext}"
    old_file= os.path.join(folder_path,filename)
    new_file= os.path.join(folder_path,new_name)
    os.rename(old_file,new_file)

print("succesful")

