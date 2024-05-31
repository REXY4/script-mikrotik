import microtik_risk
import sys
import re

def main():
    #  $popUsername $popPassword $popName $popId $popIp
    if len(sys.argv) < 6:
        print(len(sys.argv))
        print("Usage: python learn.py [username] [password] [pop_name] [pop_id] [ip:port]  [condition:optional]")
        return
    
    username = sys.argv[1]
    password = sys.argv[2]
    popName = sys.argv[3]
    popId = sys.argv[4]
    ipCommand = sys.argv[5]
    condition = sys.argv[6]
    # regex
    get_before_colon = r"([^:]+):"
    get_after_colon = r"([^:]+):"

    get_ip = re.findall(get_before_colon, ipCommand)[0]
    get_port = ipCommand.split(":")[1]
    if len(sys.argv) > 6:
        matches_upload = re.findall(get_before_colon, condition)
        if matches_upload[0] == "upload":
            if len(sys.argv) != 9:
                print("Isert your destination folder")
                return
            else:
                folder_directory = sys.argv[7]
                create_folder = microtik_risk.create_remote_folder(get_ip,get_port,username,password,folder_directory)
                source_file = sys.argv[8].split(":")[1]
                if create_folder:
                    read_file = microtik_risk.read_files_in_directory(f"{source_file}")
                    if read_file["status"] == True: 
                         if len(read_file["data"]) > 0:
                              for data_file1 in read_file["data"]:
                                uploadFileOne = microtik_risk.upload_file(f"{source_file}/{data_file1}", f"{folder_directory}/{data_file1}", get_ip, get_port, username, password)
                                print(uploadFileOne)
                         if len(read_file["folder"]) > 0:
                            for data_folder1 in read_file["folder"]:
                                folder_directory_item = f"{folder_directory}/{data_folder1}"
                                microtik_risk.create_remote_folder(get_ip,get_port,username,password,folder_directory_item)
                                read_file_item = microtik_risk.read_files_in_directory(f"{source_file}{data_folder1}/")
                                for data_file2 in read_file_item["data"]:
                                    uploadFileOne2 = microtik_risk.upload_file(f"{source_file}{data_folder1}/{data_file2}", f"{folder_directory_item}/{data_file2}", get_ip, get_port, username, password)    
                                    print(uploadFileOne2)
                    else:
                        print("error : failed to get data directory")     

                        
            
if __name__ == "__main__":
    main()    