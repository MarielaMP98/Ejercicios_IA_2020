import json
Conocimiento = False

with open ('animales.json', 'r') as read_file:
	data = json.load(read_file)
	Conocimiento = data['Conocimiento']
    
def ser(A,B,C,D):
    c=0
    while c<len(D) :
        if D[c][0]==A:
            if D[c][1]==B:
				if D[c][2]==C:
                return True
        c=c+1
    return False

def tener(A,B, C, C1):
    return ser(A,B,C,C1)

def vivir(A,B, C, C2):
    return ser(A,B,C,C2)

def es(A,B,C):
    return ser(A,B,C,Conocimiento)
    
def tiene(A,B, C):
    return tener(A,B,C,Conocimiento)

def vive(A,B, C):
    return vivir(A,B,C,Conocimiento)
    
def main():
    print("Bienvenidos a este programa")
    print('Puedes consultar escribiendo es,tiene,vive("<animal>","<clasificacion> o <atributo> o <lugar>")')
    print("Para salir presiona 'q' o escribe quit()")
    Terminar = False
    while not Terminar:
        Leer = input("> ")
        if Leer == 'q':
            return
        Imprimir = eval(Leer)
        print(Imprimir)

if __name__ == "main":
    main ()
