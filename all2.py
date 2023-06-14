import socket
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("ip",type=str)
args = parser.parse_args()

other_machine_public_ip = args.ip

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# now since our other machine will be expecting some data to be recv to port which it sent the data from (6000)

sock.bind('0.0.0.0',5000)

sock.sendto("hello from somewhere".encode(),(other_machine_public_ip,6000))