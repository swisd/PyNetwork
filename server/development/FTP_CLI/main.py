from ftplib import FTP

host = "localhost"
user = "anonymous"
password = ''

with FTP(host) as ftp:

    ftp.login(user=user)
    print(ftp.getwelcome())