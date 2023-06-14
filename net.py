import socket
import argparse

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

parser = argparse.ArgumentParser()
parser.add_argument("--listen",action='store_true')
parser.add_argument("--from_port",type=int,required=True)
parser.add_argument("--send",type=str,required=False)
parser.add_argument("-m",type=str,required=False)
args = parser.parse_args()

if args.listen:
    sock.bind(('0.0.0.0',args.from_port))
    print("Listening on port",args.from_port)
    while True:
        data_recv = sock.recv(1024)
        print("data recieved:",data_recv)
    
elif args.send:
    ip,port = str(args.send).split(":")
    sock.bind(('0.0.0.0',args.from_port))
    sock.sendto(str(args.m).encode(),(ip,int(port)))
    print("Sent message to",args.send)