import http.client
import sys

http_server = sys.argv[1]
port = sys.argv[2]
# create a connection
conn = http.client.HTTPConnection(http_server, port)

while 1:
    cmd = input('srvr> ')
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
    data_received = rsp.read()
    print(data_received)

conn.close()