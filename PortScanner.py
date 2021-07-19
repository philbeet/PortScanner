import argparse
import socket

socketvar = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# this is the timeout for syn-ack, mayyy need to be adjusted...
socketvar.settimeout(2)

# run from command line
parser = argparse.ArgumentParser(description='Scan open ports on a target machine')
parser.add_argument('-t', '--target', dest='Target', type=str,
                    help='specify a target IP')
parser.add_argument('-p', '--port', dest='Port', type=int,
                    help='specify a target port, if no port provided, will'
                         'scan first 1,000 ports')
args = parser.parse_args()

# error out if no target IP
if not args.Target:
    print('Error. Please specify a target with -t, --help for more info')
    quit()
host = args.Target
# Specify port... if no port specified will use first 1,000
if args.Port:
    port = args.Port
else:
    port = None

open_ports = []

def prettyprint():
    if open_ports:
        print('Open ports: \n')

        for x in open_ports:
            print(x, end='\n')
    else:
        print('No open ports')
def portscan(port):
    if port == None:
        for i in range(1001):
            port = i
            if socketvar.connect_ex((host,port)):
                pass
            else:
                open_ports.append(i)
        prettyprint()
    else:
        if socketvar.connect_ex((host,port)):
            print(f'Port {port} is closed')
        else:
            print(f'Port {port} is open')


portscan(port)
