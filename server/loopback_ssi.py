import threading
import socket

# Variables

clients = []
client = ''

# Functions

def send(data):
    pass

def handle(client):
    try:
        data = client.recv(2048)
    except:
        index = clients.index(client)
        clients.remove(client)
        client.close()

def recieve():
    thread = threading.Thread(target=handle, args=(client,))
    thread.start()

