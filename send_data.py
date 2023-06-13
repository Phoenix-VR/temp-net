import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

sock.bind(('0.0.0.0',5656))

addr = str(input("ip:"))
port = int(input("port:"))

sock.sendto("hello from somewhere".encode(),(addr,port))