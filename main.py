import microtik_risk
from read_command import readCommand
import sys
import re

def main():
    #  $popUsername $popPassword $popName $popId $popIp
    read = readCommand()
    if read["status"] == False:
        print(f"Useage : {read["message"]}")
        return
      
    username = read["data"]["username"]
    password = read["data"]["password"]
    popName = read["data"]["pop_name"]
    popId = read["data"]["pop"]
    condition = read["data"]["condition"]
    get_ip = read["data"]["ip"]
    get_port = read["data"]["port"]
    dir = read["data"]["directory"]
    src = read["data"]["source"]
    try:
            if condition == "upload":
                folder_directory = dir
                create_folder = microtik_risk.create_remote_folder(get_ip,get_port,username,password,folder_directory)
                if create_folder:
                    read_file = microtik_risk.read_files_in_directory(f"{src}")
                    if read_file["status"] == True: 
                         if len(read_file["data"]) > 0:
                              for data_file1 in read_file["data"]:
                                uploadFileOne = microtik_risk.upload_file(f"{src}/{data_file1}", f"{folder_directory}/{data_file1}", get_ip, get_port, username, password)
                                print(uploadFileOne)
                         if len(read_file["folder"]) > 0:
                            for data_folder1 in read_file["folder"]:
                                folder_directory_item = f"{folder_directory}/{data_folder1}"
                                microtik_risk.create_remote_folder(get_ip,get_port,username,password,folder_directory_item)
                                read_file_item = microtik_risk.read_files_in_directory(f"{src}{data_folder1}/")
                                print(f"{src}{data_folder1}/")
                                for data_file2 in read_file_item["data"]:
                                    uploadFileOne2 = microtik_risk.upload_file(f"{src}{data_folder1}/{data_file2}", f"{folder_directory_item}/{data_file2}", get_ip, get_port, username, password)    
                                    print(uploadFileOne2)
                    else:
                        print("error : failed to get data directory")     
    
    except Exception as e:
        print(e)
                        
            
if __name__ == "__main__":
    main()    