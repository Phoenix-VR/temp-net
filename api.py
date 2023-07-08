import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(('0.0.0.0',80))
connections = []
print("Listening for connection requests")
sock.listen()

while True:
    client_sock, client_addr = sock.accept()
    print("Request from:",client_addr)
    req_data = client_sock.recv(1024)
    print(req_data)
    response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n" + "<html><head><title>Demo</title></head><body><h1>Hello</h1></body></html>"
    client_sock.sendall(response.encode())
    client_sock.close()
