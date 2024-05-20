import http.client
import sys
from printmods import fprint, Fore, fprint_s
from progressbar_ import bar
import os
from time import sleep

http_server = input("IP: ")
port = input("Port: ")
id_name = input("UID: ")
# create a connection
conn = http.client.HTTPConnection(http_server, port)
conn.request("SeperateInterfaceID", id_name)
downloadsDir = "C:/Network/downloads/"
rsp = conn.getresponse()
print(rsp.status, rsp.reason)
data_received = (rsp.read()).decode("utf-8")
print(data_received)
while 1:
    oneOP = False
    download = False
    cmd = input(f'\n{Fore.YELLOW}cmd> {Fore.WHITE}')

    cmd = cmd.split()

    if cmd[0] == '--e':  # type exit to end clientside
        break
    elif cmd[0]== '--rst':
        os.execv(sys.executable, ['python'] + sys.argv)

        # request command to server
    if cmd[0] == '--d':
        download = True
        cmd[0] = 'GET'

    if cmd[0].startswith('-'):
        cmd[0] = cmd[0].replace('-', '_')

    try:
        conn.request(cmd[0], cmd[1])
    except:
        conn.request(cmd[0], "/")

    fprint("Request sent.\n", "INFO", Fore.GREEN)

    # get response from server
    try:
        rsp = conn.getresponse()
    except:
        fprint("Server did not respond", "ERROR", Fore.RED)
        continue

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
        try:
            with open(downloadsDir + cmd[1].removeprefix("/db/"), "x") as _f:
                _f.write((data_received.decode('utf-8')).split('<plaintext>')[1])
                _f.close()
        except:
            fprint("File write error", "ERROR", Fore.RED)


    # print server response and data
    fprint_s(rsp.reason, rsp.status, rsp.status)
    data_received = (rsp.read()).decode("utf-8")
    if not data_received.endswith("File not found"):
        print(data_received)
    else:
        fprint("File not found for this path. ERR:404", "ERROR", Fore.RED)

conn.close()
print("Connection closed.")