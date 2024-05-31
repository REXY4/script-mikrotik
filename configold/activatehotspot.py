import paramiko
import sys
import requests

arg =  sys.argv
userpop  = arg[1]
passpop  = arg[2]
identity = arg[3]
code_pop = arg[4]
ip = arg[5]

errorConf = 0

pathConf = './confighotspot.txt'
urlPost = 'https://konekyu.id/api/v1/network-program/log-execution'

inputconfig = open(pathConf, "r")
line_count = 0
for line in inputconfig:
    if line != "\n":
        line_count += 1
inputconfig.close()


addcert = '/certificate import file-name=sslhot.cert passphrase=""'
addkey = '/certificate import file-name=sslhot.key passphrase=""'
setidentity = 'system identity set name="{}"_{}'.format(identity,code_pop)
adduser = 'user add name={} password={} group=full address=10.0.0.0/8,172.16.0.0/12,103.73.73.66,103.73.72.0/24'.format(userpop,passpop)
setserver = 'ip hotspot set 0 name={}'.format(code_pop)

try:
	ssh_client = paramiko.SSHClient()
	ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh_client.connect(hostname=ip,username='admin',password='',port=22)
	#print ("Successfull Login to {}, ".format(ip))
	pload = {'code_pop':"{}".format(code_pop),'log':'login Successfull'}
	r = requests.post(urlPost,data = pload)
	inputconfig = open(pathConf, "r").readlines()

	
	stdin, stdout, stderr = ssh_client.exec_command(addcert)
	stdin, stdout, stderr = ssh_client.exec_command(setidentity)
	stdin, stdout, stderr = ssh_client.exec_command(adduser)
	stdin, stdout, stderr = ssh_client.exec_command(setserver)
	stdin, stdout, stderr = ssh_client.exec_command(addkey)

	for x in range(0,line_count-1):
		stdin, stdout, stderr = ssh_client.exec_command(inputconfig[x])
		output = (stdout.read().decode("ascii").strip("\n"))
		if(len(output) != 0):
			pload = {'code_pop':"{}".format(code_pop),'log':'Error Config while Activate POP {} : line code {} {} '.format(code_pop,x,output),'line':'{}'.format(x)}
			r = requests.post(urlPost,data = pload)
			errorConf+=1

	#print ("Successfull config {}, ".format(code_pop))
	if(errorConf==0):
		pload = {'code_pop':"{}".format(code_pop),'log':'Successfull config activate on {}'.format(code_pop)}
		r = requests.post(urlPost,data = pload)
	else:
		pload = {'code_pop':"{}".format(code_pop),'log':'Please Check error config activate on {}'.format(code_pop)}
		r = requests.post(urlPost,data = pload)
	

except Exception as NoValidConnectionsError:
	print("Can't Connect to {}".format(ip))
	
	pload = {'code_pop':"{}".format(code_pop),'log':'login failed to {} IP {}'.format(code_pop,ip)}
	r = requests.post(urlPost,data = pload)
