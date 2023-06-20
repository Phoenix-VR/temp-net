import socket
import argparse
from time import sleep

parser = argparse.ArgumentParser()
parser.add_argument("--from_port",type=int,required=True)
parser.add_argument("--send",type=str,required=False)
args = parser.parse_args()

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
sock.bind((socket.gethostbyname(socket.gethostname()),args.from_port))

ip,port = str(args.send).split(":")

while True:
    try:
        
        sock.connect((ip,int(port)))
        print("connected")
        break
    except socket.timeout as T:
        continue
    except OSError as E:
        print("Error:",E)
        continue
    except:
        sleep(1)
        continue


# 192.168.56.1