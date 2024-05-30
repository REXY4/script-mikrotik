import os
import re
# import glob

def read_files_in_directory(directory):
    file_contents = []
    # Mencari semua file dalam direktori
    files = os.listdir(f"{directory}")
    
    # Membaca isi setiap file dan memasukkannya ke dalam array
    for file_path in files:
        if not re.search(r'\.', file_path):
            print("hallo")
        else:
           file_contents.append(file_path)
    
    return file_contents