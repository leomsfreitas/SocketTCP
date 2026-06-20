import socket
import threading
from config import HOST_SERVER as HOST, PORT


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
usernames = []

print(f"Servidor iniciado em {HOST}:{PORT}")


def broadcast(message, sender=None):
    for client in clients:
        if client != sender:
            try:
                client.send(message)
            except:
                pass


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message, client)
        except:
            index = clients.index(client)
            username = usernames[index]
            clients.remove(client)
            usernames.remove(username)
            client.close()
            broadcast(f"[Servidor] {username} saiu do chat.\n".encode("utf-8"))
            print(f"{username} desconectado.")
            break


def receive():
    while True:
        client, address = server.accept()
        print(f"Conexão aceita: {address}")
        client.send("USERNAME".encode("utf-8"))
        username = client.recv(1024).decode("utf-8")
        usernames.append(username)
        clients.append(client)
        broadcast(f"[Servidor] {username} entrou no chat!\n".encode("utf-8"))
        client.send("[Servidor] Conectado com sucesso!\n".encode("utf-8"))
        print(f"Usuário registrado: {username}")
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

if __name__ == "__main__":
    receive()
