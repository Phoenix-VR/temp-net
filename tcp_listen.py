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

src_port = args.from_port

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

def listen(ip,port):
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    soc.bind((ip,port))
    print("[LISTENING] LISTENING ON PORT",str(port))
    soc.listen()
    while True:
        try:
            client_soc, addr = soc.accept()
            print("[ACCEPTED] CONNECTION HAS BEEN ESTABLISHED WITH",addr)
            print("[EXIT] EXITTING...")
        except KeyboardInterrupt:
            exit()

def connect(myip,target_ip,target_port):
    sockt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockt.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sockt.settimeout(5)
    sockt.bind((myip,src_port))
    try:
        print("[REQUEST SENT] CONNECTION REQUEST HAS BEEN SENT")
        sockt.connect((target_ip,target_port))
        print("[CONNECTED] CONNECTION HAS BEEN ESTABLISHED WITH",target_ip,str(target_port))
        print("[EXIT] EXITTING...")
        exit()
    except socket.timeout as Timeout:
        print("[RESENING] TIMEOUT. RESENDING...")
        connect(myip,target_ip,target_port)
    except ConnectionRefusedError as E:
        print("[REFUSED] CONNECT REFUSED BY THE TARGET. Resending the request...")
        sleep(1)
        connect(myip,target_ip,target_port)
    except KeyboardInterrupt:
        exit()

target_ip,target_port = str(args.send).split(":")
target_port = int(target_port)

threading.Thread(target=connect,args=('192.168.56.1',target_ip,target_port)).start()
threading.Thread(target=listen,args=('192.168.56.1',src_port)).start()
print("[STARTED] BOTH THREADS HAS BEEN EXECUTED")

# python tcp_listen.py --from_port 5000 --send 192.168.56.1:6000