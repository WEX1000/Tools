import socket

target_host = "127.0.0.1"
target_port = 9997

#Utworzenia obiektu gniazda
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Wysylanie danych
client.sendto("AAABBBCCC", (target_host, target_port))

#Odebranie danych
data, addr = client.recvfrom(4096)

print(data.decode())
client.close()