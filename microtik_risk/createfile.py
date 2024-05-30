import paramiko;

def create_remote_folder(hostname, port, username, password, folder_path):
    # Membuat koneksi SSH
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh_client.connect(hostname, port=port, username=username, password=password)
        # Membuka koneksi SFTP
        sftp_client = ssh_client.open_sftp()
        # Membuat folder di server
        sftp_client.mkdir(folder_path)
        # Menutup koneksi SFTP
        sftp_client.close()
        return {
        'status': True,
        'message': f"Create folder {folder_path} in {hostname} success"
         }
    except Exception as e:
        ssh_client.close()
        return {
        'status': False,
        'message': f"Create folder failed!: {e}"
         }
    # Menutup koneksi SSH