#MarielaMoralesPerez
Es = [
	("Ballena","Mammalia"),
	("Delfin", "Mammalia"),
	("Gato", "Mammalia"), 
	("Oso", "Mammalia"),
	("Tortuga", "Oviparos"), 
	("Cocodrilo", "Oviparos"),
	("Iguana", "Oviparos"),
	("Gallo", "Oviparos"), 
	("Mammalia","Viviparos"),
	("Viviparos","Tetrapodos"),  
	("Oviparos", "Seuropsidos"), 
	("Seuropsidos", "Tetrapodos"), 
	("Tetrapodos", "Vertebrados")
]

Tiene = [
	("Ballena","G Mamarias"),
	("Ballena", "Piel queratina"),	
	("Delfin","G Mamarias"),
	("Oso","G Mamarias"),
	("Oso","Pelo"),
	("Oso", "Garras"),
	("Gato","G Mamarias"),    
	("Gato","Pelo"),
	("Gato", "Garras"), 

	("Oviparos", "Piel queratina")
]

Vive = [
	("Ballena","Agua"),
	("Delfin", "Agua"),
	("Gato", "Tierra"), 
	("Oso", "Tierra"),
	("Iguana", "Tierra"),
	("Gallo", "Tierra"),  
	("Tortuga", "Agua"), 
	("Tortuga", "Tierra"), 
	("Cocodrilo", "Agua"), 
	("Cocodrilo", "Tierra")
]

def Ser(A, B, C):
    c=0
    while c<len(C) :
        if C[c][0]==A:
            if C[c][1]==B:
                return True
            A = C[c][1] 
        c=c+1
    return False

def Tener(A, B, C):
    e=0
    while e<len(C) :
        if C[e][0]==A:
            if C[e][1]==B:
                return True
        e=e+1
    return False

def Vivir(A, B, C):
    e=0
    while e<len(C) :
        if C[e][0]==A:
            if C[e][1]==B:
                return True
        e=e+1
    return False 

print(Ser("Ballena","Vertebrados",Es))
print(Tener("Gato","Garras",Tiene))
print(Vivir("Gato","Agua",Vive))
    

