import socket
import threading

IP = "192.168.0.41"
PORT = 9996

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    server.listen(5)
    print(f'[*] Nasluchiwanie na {IP}:{PORT}')

    while True:
        client, address = server.accept()
        print(f'[*] Przyjeto polaczenia od {address[0]}:{address[1]}')
        clinet_handler = threading.Thread(target=handle_client, args=(client,))
        clinet_handler.start()

def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print(f'[*] Odebrano: {request.decode("utf-8")}')
        sock.send(b'ACKKK')

if __name__ == '__main__':
    main()

