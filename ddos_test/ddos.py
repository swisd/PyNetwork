import http.client
from time import sleep

# get http server ip
http_server = '127.0.0.1'
# create a connection
conn = http.client.HTTPConnection(http_server, 8000)
cmd = input('input command (ex. GET index.html): ')
delay = int(input("Send Delay (ms):"))
cmd = cmd.split()
while 1:

    if cmd[0] == 'exit':  # type exit to end clientside
        break

        # request command to server
    conn.request(cmd[0], cmd[1])

    # get response from server
    rsp = conn.getresponse()

    # print server response and data
    print(f'\r{rsp.status}, {rsp.reason}', end='')
    data_received = rsp.read()
    sleep(delay / 1000)

conn.close()
