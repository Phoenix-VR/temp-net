import socket
import argparse
import time

connections = []

def open_port_with_udp(port,target_addr):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('0.0.0.0',port))
    sock.sendto("hi".encode(),target_addr)



parser = argparse.ArgumentParser()
parser.add_argument("--from_port",type=int,required=True)
parser.add_argument("--send",type=str,required=False)
parser.add_argument("-m",type=str,required=False)
args = parser.parse_args()

ip,port = str(args.send).split(":")

open_port_with_udp(args.from_port,(ip,int(port)))

# wait for other peer to send something

sockt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockt.bind(('0.0.0.0',args.from_port))
sockt.listen(5)
sockt.settimeout(10)
try:
    target_soc, addr = sockt.accept()
    if target_soc:
        connections.append(target_soc)
        print("Connection established with",addr)
        exit(1)
except:
    print("[NO RESPONSE FROM OTHER SIDE] Time Limit ran out for port, no connections recieved.")    
