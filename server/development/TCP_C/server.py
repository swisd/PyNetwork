import threading
import socket

# Variables

host = '127.0.0.1' #localhost
port = 55400

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []
banned_nicknames = ''

# Methods

def broadcast(message, cl):
    for client in clients:
        if not client == cl:
            client.send(message)
        else:
            continue

def handle(client):
    while True:
        try:
            msg = message = client.recv(1024)
            if msg.decode('ascii').startswith('KICK'):
                if nicknames[clients.index(client)] == 'admin':
                    name_to_kick = msg.decode('ascii')[5:]
                    kick_user(name_to_kick)
                    print(f'{name_to_kick} was kicked.')
                else:
                    client.send('Command was refused.'.encode('ascii'))
            elif msg.decode('ascii').startswith('BAN'):
                if nicknames[clients.index(client)] == 'admin':
                    name_to_ban = msg.decode('ascii')[4:]
                    kick_user(name_to_ban)
                    banned_nicknames += name_to_ban + '\n'
                    print(f'{name_to_ban} was banned.')
                else:
                    client.send('Command was refused.'.encode('ascii'))
            else:
                broadcast(message, client)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f"{nickname} is offline.".encode('ascii'), client)
            nicknames.remove(nickname)
            break

def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {address}")

        client.send("NICK".encode('ascii'))

        nickname = client.recv(1024).decode('ascii')

        if nickname+'\n' in banned_nicknames:
            client.send('BAN'.encode('ascii'))
            client.close()
            continue

        if nickname == 'admin':
            client.send('PASS'.encode('ascii'))
            password = client.recv(1024).decode('ascii')

            if password != 'adminpass':
                client.send('REFUSE'.encode('ascii'))
                client.close()
                continue

        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname of the client is {nickname}")
        broadcast(f"{nickname} has connected".encode('ascii'), client)
        client.send("Connected to the server".encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


def kick_user(name):
    if name in nicknames:
        name_index = nicknames.index(name)
        client_to_kick = clients[name_index]
        clients.remove(client_to_kick)
        client_to_kick.send("You were kicked by admin".encode('ascii'))
        client_to_kick.close()
        nicknames.remove(name)
        broadcast(f'{name} was kicked by admin'.encode('ascii'))

print("Server started")
print("Server running")
print("Listening @ 127.0.0.1 * 55400")
receive()
