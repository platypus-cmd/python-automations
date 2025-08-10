import os
import shutil

folder_path = input("enter the path: ").strip()

if not os.path.exists(folder_path):
    print("it doesnt exists")
    exit()

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"]
}
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path,filename)

    if os.path.isdir(file_path):
        continue

    ext = os.path.splitext(filename)[1].lower()

    moved = False
    for category, extensions in file_types.items():
        if ext in extensions:
            category_folder = os.path.join(folder_path, category)
            os.makedirs(category_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(category_folder, filename))
            moved = True
            break

    
    if not moved:
        other_folder = os.path.join(folder_path, "Others")
        os.makedirs(other_folder, exist_ok=True)
        shutil.move(file_path, os.path.join(other_folder, filename))

print("Files organized successfully!")




