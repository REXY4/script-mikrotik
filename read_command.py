import sys
import re

def readCommand():
   arg = sys.argv
   try:
      host = arg[arg.index('-h') + 1]
      port = arg[arg.index('-P') + 1]
      password = arg[arg.index('-p') + 1]
      pop = arg[arg.index('-pop') + 1]
      condition = arg[arg.index('-c') + 1]
      dir=""
      src=""
      filtered_dir = [x for x in arg if x == "-dir"]
      if filtered_dir :
         dir = arg[arg.index('-dir') + 1]

      if [x for x in arg if x == "-src"]:
         src = arg[arg.index('-src') + 1]
      #regex
      if condition == "upload" and (dir == "" or src == ""):
         return {
            "status" :False,
            "message" : "Usage -dir, example : -dir directory_path" if dir == "" else ("Usage -src example : -src source_path" if src == "" else "Usage -dir and -src") 
         }
      
      beforeHost = r'([^@]+)@'
      before_collon = r'([^:]+):'

      username = re.search(beforeHost, host).group(1)
      ip = host.split("@")[1]
      result = {
         "status" : True,
         "message" : "success!",
         "data" : {
            "ip" : ip,
            "username" : username,
            "password" : password,
            "port" : port,
            "pop" : pop.split(":")[1],
            "pop_name": re.search(before_collon, pop).group(1),
            "source" : src,
            "directory" : dir,
            "condition" : condition
         }
      }
      return result
   except Exception as e:
      return {
         "status" :False,
         "message" : e,
         "data" : []
      }

readCommand()