import sys

def main():
    #  $popUsername $popPassword $popName $popId $popIp
    if len(sys.argv) != 6 :
        print("Usage: python learn.py [username] [password] [pop_name] [pop_id] [ip]")
        return
    
    username = sys.argv[1]
    password = sys.argv[2]
    popName = sys.argv[3]
    popId = sys.argv[4]
    ip = sys.argv[5]

    print(len(sys.argv))
    print(sys.argv)  
    



if __name__ == "__main__":
    main()    