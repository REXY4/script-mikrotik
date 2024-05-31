import os
import re
# import glob

def read_files_in_directory(directory):
   try: 
    file_contents = []
    file_contents_folder = []
    # Mencari semua file dalam direktori
    files = os.listdir(f"{directory}")
    # Membaca isi setiap file dan memasukkannya ke dalam array
    for file_path in files:
        if not re.search(r'\.', file_path):
            file_contents_folder.append(file_path)
        else:
           file_contents.append(file_path)
    return {
            "status" : True,
            "folder" : file_contents_folder,
            "data" : file_contents,
        }    
   except Exception as e:
        return {
                "status" : False,
                "folder" : [],
                "data" : [],
        } 