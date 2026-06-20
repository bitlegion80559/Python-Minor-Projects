import os
import shutil

EXTENSION_MAP = {
    "PDFs": [".pdf"],
    "Word_documents": [".doc", ".docx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Spreadsheets": [".xls", ".xlsx"],
    "Text_files": [".txt"]
}

def get_dest_folder(filename):
    ext=os.path.splitext(filename)[1].lower()
    for Folder, extensions in EXTENSION_MAP.items():
        if ext in extensions:
            return Folder
    return "Others"

def Sort_files(folder):
    for filename in os.listdir(folder):
        file_path=os.path.join(folder,filename)
        if os.path.isfile(file_path):
            dest_folder=get_dest_folder(filename)
            dest_path=os.path.join(folder,dest_folder)
            os.makedirs(dest_path,exist_ok=True)
            shutil(file_path,os.path.join(dest_path,filename))
            print(f"Moved : {filename} -> {dest_folder}/")

if "__name__"=="main":
    folder = input("Enter the folder path or leave blank: ").strip()
    folder = folder or os.getcwd()

    if not os.path.isdir(folder):
        print("Invalid directory")
    else:
        Sort_files(folder)
        print("✅ sorting completed")