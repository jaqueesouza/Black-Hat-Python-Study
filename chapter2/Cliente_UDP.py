import socket

target_host = "127.0.0.1"
target_port = 80

# criar um objetivo socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# enviar dados
client.sendto(b"AAABBBCCC",(target_host,target_port))

# receber dados
data, addr = client.recvfrom(4096)

client.close()
print(data.decode())
