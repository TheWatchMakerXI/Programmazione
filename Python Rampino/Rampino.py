
#4
# print(f"prova {x} + {y} = {x + y}")

scelta = 0

while(scelta == 0):
    x = int(input("inserisci un numero:"))
    y = int(input("inserisci un altro numero:"))
    print = int(input("l - addizione\n2- sottrazione\n3- moltiplicazione\n4 - esci\n Scegli ", scelta))
    if (scelta == 1) : print(f"{x} + {y}= {x + y}") 
    elif (scelta == 2) :print(f"{x} + {y}= {x - y}")   
    elif (scelta == 3) :print(f"{x} + {y}= {x * y}") 
    else: print("esco")
    scelta = 0