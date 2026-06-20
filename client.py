import socket
import threading
from config import HOST_CLIENT as HOST, PORT


username = input("Nome de usuário: ").strip()
if not username:
    username = "Anônimo"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect((HOST, PORT))
except ConnectionRefusedError:
    print("Erro: servidor não encontrado. Verifique HOST e PORT.")
    raise SystemExit

ready = threading.Event()


def receive():
    while True:
        try:
            message = client.recv(1024).decode("utf-8")
            if message == "USERNAME":
                client.send(username.encode("utf-8"))
            else:
                print(message, end="")
                if "Conectado" in message:
                    ready.set()
        except:
            print("Conexão encerrada.")
            client.close()
            raise SystemExit


def write():
    while True:
        try:
            text = input()
            if text.strip():
                message = f"{username}: {text}\n"
                client.send(message.encode("utf-8"))
        except (EOFError, KeyboardInterrupt):
            client.close()
            raise SystemExit


receive_thread = threading.Thread(target=receive, daemon=True)
receive_thread.start()

if __name__ == "__main__":
    ready.wait()
    write()