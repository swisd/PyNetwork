import http.client
import random
import sys
import os
from colorama import *
from progressbar_ import bar
from time import sleep

# get http server ip
http_server = '127.0.0.1'
# create a connection
conn = http.client.HTTPConnection(http_server, 8000)

downloadsDir = "C:/Network/downloads/"
idt = random.randrange(0, 99999)

def fprint(text, aux, col):
    print((f'{col}[{aux}] {text}{Fore.WHITE}' if aux != '' else f"{col}{text}{Fore.WHITE}"))


def fprint_s(text, aux, stat):
    if (stat >= 100 and stat <= 299):
        col = Fore.GREEN
    elif (stat >= 300 and stat <= 399):
        col = Fore.YELLOW
    elif (stat >= 400 and stat <= 599):
        col = Fore.RED

    print((f'{col}[{aux}] {text}{Fore.WHITE}' if aux != '' else f"{col}{text}{Fore.WHITE}"))


conn.request("SeperateInterfaceID", f"RemoteClient{idt}")
rsp = conn.getresponse()

while 1:
    download = False
    upload = False
    cmd = input('input command (ex. GET index.html): ')
    cmd = cmd.split()

    if cmd[0] == ('exit' or '-e'):  # type exit or -e to end clientside
        break

    if cmd[0] == '--d':
        download = True
        cmd[0] = 'GET'

    elif cmd[0] == '--u':
        upload = True
        cmd[0] = 'UPLOAD'

    if upload:
        cmd[1] == f"name='{(cmd[1].split('/'))[((len(cmd[1].split('/')))-2):]}'_data={(open(cmd[1], 'r')).read()}"


    # request command to server
    conn.request(cmd[0], cmd[1])

    # get response from server
    rsp = conn.getresponse()

    # print server response and data
    fprint_s(f'{rsp.reason} - {cmd}', rsp.status, rsp.status)
    data_received = rsp.read()

    if download:
        print()
        print(downloadsDir + (cmd[1].removesuffix((cmd[1].split("/"))[len((cmd[1].split("/"))) - 1])).removeprefix("/db/"))
        if not os.path.exists(downloadsDir + (cmd[1].removesuffix((cmd[1].split("/"))[len((cmd[1].split("/"))) - 1])).removeprefix("/db/")):
            os.makedirs(downloadsDir + (cmd[1].removesuffix((cmd[1].split("/"))[len((cmd[1].split("/"))) - 1])).removeprefix("/db/"))

        items = list(range(0, 20))
        l = len(items)
        bar(0, 50, prefix='Downloading', suffix="Complete", length=10)
        for i, item in enumerate(items):
            # Do stuff...
            sleep(0.1)
            # Update Progress Bar
            bar(i + 1, l, prefix='Downloading:', suffix='Complete', length=10)
        with open(downloadsDir + cmd[1].removeprefix("/db/"), "x") as _f:
            _f.write((data_received.decode('utf-8')).split('<plaintext>')[1])
            _f.close()

    # print(data_received.decode('utf-8'))

conn.close()
