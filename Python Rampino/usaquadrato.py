
import socket


SRV_ADDR = "192.168.42.44"
SRV_PORT = 44444


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((SRV_ADDR, SRV_PORT))
s.listen(1)
print(f"Server started on port {SRV_PORT}")


connection, address = s.accept()
print("Connection established with address " + address)


while 1:
    data = connection.recv(1024)
    if not data: 
        break


    print(data.decode('utf-8'))
connection.close()