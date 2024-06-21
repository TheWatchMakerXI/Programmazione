import socket as so

target = input ("Inserisci l'ip da scansionasare: ")

portrange = input("Inserisci un range di porte (es 0-200): ")

lowport = 0
highport = 200

if portrange.find("-") == 1:
    lowport = int(portrange.split("-")[0])
    hiport = int(portrange.split("-")[1])
    
print(f"Verrano scansite le porta da {lowport} a {highport}")
closePort = []
#for inverso 
whit range(lowport, hiport+1) as port : #uguale a quello di sotto
    s = so.socket(so.AF_INET, so.SOCK_STREAM)
    #s.sendto() in udp
    status = s.connect_ex((target, port))
    if(status == 0): print("*** Porta {port} Aperta ***")
    else: closePort.append(port)
    s.close()
    
print("Porte chiuse: ", closePort)

