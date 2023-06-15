import socket
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--from_port",type=int,required=True)
parser.add_argument("--connect",type=str,required=False)
args = parser.parse_args()

sockt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sockt.bind(("0.0.0.0",args.from_port))

ip,port = str(args.connect).split(":")

sockt.settimeout(5)

sockt.connect((ip,int(port)))


