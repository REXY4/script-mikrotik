import paramiko

def upload_file(source_file, destination_file, hostname, port, username, password):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh_client.connect(hostname, port=port, username=username, password=password)
        scp_client = ssh_client.open_sftp()
        scp_client.put(source_file, destination_file)
        scp_client.close()
        ssh_client.close()
        return {
        'status': True,
        'message': "File transferred successfully!"
         }
    except Exception as e:
        return {
        'status': False,
        'message': f"An error occurred: {e}"
         }

