import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

sock.bind(('0.0.0.0',5656))

print("Listening for connections on ",socket.gethostbyaddr(socket.gethostname()))


while True:
    data = sock.recvfrom(1024)
    if data:
        print("Recieved:",data)