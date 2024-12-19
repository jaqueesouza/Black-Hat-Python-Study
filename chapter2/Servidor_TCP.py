import socket
import threading

IP = '0.0.0.0'
PORT = 9998


# socket.AF_INET = indica que vai ser usado endereço IPv4.
# socket.SOCK_STREM = indica que o cliente é TCP.
def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    server.listen(5)
    print(f'[*] Ouvindo em {IP}:{PORT}')

    while True:
        client, address = server.accept()
        print(f'[*] Conexão aceita de {address[0]}:{address[1]}')
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print(f'[*] Recebido: {request.decode("utf-8")}')
        sock.send(b'ACK')

if __name__ == '__main__':
    main()
