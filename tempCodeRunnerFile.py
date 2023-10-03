total=0
index=1
while True:
    print("ingrese el cuadrado o 0 para terminar de ingresar cuadrados")
    print("ingrese el cuadrado ",index)
    square=int(input())
    if(square != 0):
        total+= 2**square
    else:
        break
modulo=total**1/2
print("el modulo es de: ",modulo)