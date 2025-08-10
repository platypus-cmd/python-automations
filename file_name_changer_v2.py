import os
folder_path= input("enter the folder path: ").strip()

if not os.path.exists(folder_path):
    print("no such path exists")
    exit()

files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path,f))]

if not files:
    print("no files here")
    exit()

for count,filename in enumerate(files,start=1):
    ext= os.path.splitext(filename)[1]
    new_name = f"image{count}{ext}"
    old_file= os.path.join(folder_path,filename)
    new_file= os.path.join(folder_path,new_name)
    os.rename(old_file,new_file)

print("succesful")



