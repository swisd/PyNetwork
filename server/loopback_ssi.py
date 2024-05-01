import threading

# Variables

clients = []
client = ''

# Functions

class DataManagement:
    def send(self, data):
        pass

    def handle(self, client):
        self.client = client
        try:
            data = self.client.recv(2048)
        except:
            index = clients.index(self.client)
            clients.remove(self.client)
            self.client.close()

    def recieve(self):
        thread = threading.Thread(target=DataManagement.handle, args=(client,))
        thread.start()

