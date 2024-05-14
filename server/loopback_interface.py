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
    cmd = input('\ncmd> ')
    cmd = cmd.split()

    if cmd[0] == '-e':  # type exit to end clientside
        break

        # request command to server
    if cmd[0].startswith('-'):
        cmd[0] = cmd[0].replace('-', '_')
 
    if cmd[1] == '':
        cmd[1] = '/'

    conn.request(cmd[0], cmd[1])
    print("Request sent.\n")

    # get response from server
    try:
        rsp = conn.getresponse()
    except:
        print("Server did not respond")
        continue


    # print server response and data
    print(rsp.status, rsp.reason)
    data_received = (rsp.read()).decode("utf-8")
    if not data_received.endswith("File not found"):
        print(data_received)
    else:
        print("File not found for this path. ERR:404")

conn.close()
print("Connection closed.")