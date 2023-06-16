import socket
import asyncio
import argparse
from time import sleep
import threading

parser = argparse.ArgumentParser()
parser.add_argument("--from_port",type=int,required=True)
parser.add_argument("--send",type=str,required=False)
parser.add_argument("-m",type=str,required=False)
args = parser.parse_args()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('0.0.0.0',args.from_port))

connections = []
sock.settimeout(10)



ip,port = str(args.send).split(":")
port = int(port)

def connect():
    try:
        sock.connect((ip,port))
        print("[CONNECTED] CONNECTION ESTABLISED WITH",ip,port)
        sock.close()
        exit()
    except socket.timeout as Timeout:
        print("[TIMEOUT] Connection request timeout. Sending another request...")
        connect()
    except:
        sleep(1)
        print("[ERROR] The connect function ran into an error. Peer might have refused the connection. Retrying...")
        connect()

def listen():
    sock.listen(5)
    print("[LISTENING] Listening on port",args.from_port)
    while len(connections)!=1:
        soc, addr = sock.accept()
        print("[CONNECTED] Accepted connection from",addr)
        connections.append(addr)

# this will not go thru but will open the port for responses (dummy req)
threading.Thread(target=connect()).start()
# listen for stuff on the opened port
threading.Thread(target=listen()).start()

# send a connect request every 10 seconds

# send a connect request to this pc as well

# we got connected congrats