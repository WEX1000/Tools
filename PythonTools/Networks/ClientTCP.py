import socket

target_host = "192.168.0.41"
target_port = 9998

#Utworzenia obiektu gniazda
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Polaczenie sie z serwerem
client.connect((target_host, target_port))

#Wysylanie danych
client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n".encode())

#Odebranie danych
response = client.recv(4096)

print(response.decode())
client.close()