import os

def rename_files_in_folder(folder_path,base_name,extension):
    files=[f for f in os.listdir(folder_path) if f.lower().endswith(extension.lower())]
    if not files:
        print("No data received")
        return
    for i, file in enumerate(files,start=1):
        new_name=f"{base_name}_{i}{extension}"
        print(f"{base_name}_{i}{extension}")
    confirm=input("Are you ok wiht the name : Y/N : ").strip().lower()
    if confirm !='y':
        print("Cancel")
        return
    for i, file in enumerate(files, start=1):
        src = os.path.join(folder_path, file)
        new_name = f"{base_name}_{i}{extension}"
        dest = os.path.join(folder_path, new_name)
        os.rename(src, dest)
    print(f"Renamed {len(files)} files successfully")



if __name__=="__main__":
    folder = input("Enter folder path or learn blank for current folder: ").strip() or os.getcwd()

    if not os.path.isdir(folder):
        print("Invalid folder")
    else:
        base_name = input("Enter base name for files: ").strip()
        extension = input("Enter extension name for files: ").strip()

        rename_files_in_folder(folder, base_name, extension)


