import http.client
import sys

http_server = input("IP: ")
port = input("Port: ")
id_name = input("UID: ")
# create a connection
conn = http.client.HTTPConnection(http_server, port)
conn.request("SeperateInterfaceID", id_name)
rsp = conn.getresponse()
print(rsp.status, rsp.reason)
data_received = (rsp.read()).decode("utf-8")
print(data_received)
while 1:
    cmd = input('cmd> ')
    cmd = cmd.split()

    if cmd[0] == '-e':  # type exit to end clientside
        break

        # request command to server
    if cmd[0].startswith('-'):
        cmd[0] = cmd[0].replace('-', '_')
 
    if cmd[1] == '':
        cmd[1] = '/'

    conn.request(cmd[0], cmd[1])

    # get response from server
    rsp = conn.getresponse()


    # print server response and data
    print(rsp.status, rsp.reason)
    data_received = (rsp.read()).decode("utf-8")
    print(data_received)

conn.close()