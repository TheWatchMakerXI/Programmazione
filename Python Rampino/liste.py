dizionario = {"nome" : "Pippa", "cognome" : "Elkan", "Hobby" : "Polveri bianche"}

print(dizionario.keys())

print(dizionario.values())

#array di double  
lista = [1, 2, 3] #destrutturazione del dato, 
x, y, z = lista 
#print (y) dovrebbe diventare 2

for n in lista:
    print(n)
    
    print(list(dizionario.items()))# mi stampa la duopla ossia tutto il dizionario kay e item
    
    for k, v in dizionario.items():
        print(f"{k} : {v}")
        
    print(f"{dizionario['cognome']} {dizionario['nome']} {dizionario['Hobby']}")
    
    