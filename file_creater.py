import os 
def create_file(folder_path,ext,number):
    
    for i in range(1,number+1):
        file_path = os.path.join(folder_path,f"file_{i}.{ext}")
        with open(file_path,"w") as f:
            f.write(f"this is file number {i}")
    print("succesful")

folder_path = input("enter the folder path: ")
ext= input("enter the extension: ").lower()
number= int(input("enter the number of files: "))
create_file(folder_path,ext,number)
