import microtik_risk
import sys
import re
import os

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
            if len(sys.argv) != 8:
                print("Isert your destination folder")
                return
            else:
                folder_directory = sys.argv[7]
                create_folder = microtik_risk.create_remote_folder(get_ip,get_port,username,password,folder_directory)
                if create_folder:
                    # print("check datas")
                    # uploadFileOne = microtik_risk.upload_file("./konekyu/api.html", "konekyu/api.html", get_ip, get_port, username, password)
                    # print(uploadFileOne)
                    read_file = microtik_risk.read_files_in_directory("./konekyu/")
                    print(read_file)

            
if __name__ == "__main__":
    main()    