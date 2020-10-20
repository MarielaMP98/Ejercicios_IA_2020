#Writing to a buffer
from io import open
import json
Probabilidad = False

#Read from the buffer
with open("base.json", "r") as read_file:
    data = json.load(read_file)
    Probabilidad = data['probabilidades']    
    
tweet = open ('tweet.txt','r')
leertweet = tweet.read()
divtweet = leertweet.split()
tweet.close()

##############################################

def Stream(p, C):
    suma = 0
    prom = 0
    a = len(p)
    b = len(C)
    n = []

# Discard List, Extended list - appened
    if a <= 2:
        return "No es Stream/ TXT"
    else:
        for i in range(a):
            for j in range (b):
                if C[j][0] == p[i]:
                    n.append(C[j])
        for a in range(len(n)):
            suma += float(n[a][1])
            prom = suma / len(n)
        if (prom > 0.55):
            return "Stream"
        else:
            return "No es Stream"

print(Stream(divtweet,Probabilidad))