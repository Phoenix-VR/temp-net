import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(('0.0.0.0',80))

print("Listening for connection requests")
sock.listen()

connections = {}
addresses = []

while True:
    client_sock, client_addr = sock.accept()

    print("Request from:",client_addr)
    data = client_sock.recv(1024).decode()
    recv_data = data.split(":")
    response = ""
    if recv_data[0] == "register":
        client_ip,client_port = recv_data[1],recv_data[2]
        client_addr = str(client_ip+":"+client_port)
        if len(connections.keys()) != 0:
            if client_addr not in connections:
                connections[client_addr] = client_sock
                addresses.append(client_addr)
                response = "registered success"
            else:
                response = "you have already registered please wait for other peer to connect"
        else:
            connections[client_addr] = client_sock
            addresses.append(client_addr)
            response = "registered success"
    
    if len(connections.keys()) == 1:
        client_sock.sendall(response.encode())
    elif len(connections.keys()) == 2:
        # we can finally tell the 2 connected peers when to initiate the hole punching
        for i,client in enumerate(connections.keys()):
            connections[client].sendall("Initiate".encode())
            if i == 0:
                connections[client].sendall(addresses[1].encode())
            elif i == 1:
                connections[client].sendall(addresses[0].encode())
            connections[client].close()
        connections.clear()
# recieve network address of that thing 
