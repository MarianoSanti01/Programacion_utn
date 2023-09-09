import math

#ejercisio 1
'''abecedario="abcdefghijklmnñopqrstuvwxyz"
corrimiento=int(input("¿cual es el corrimiento? "))
palabra=""
for i in range(5):
  print("ingrese el mensaje para el general ",i+1)
  palabra = input().lower()
  palabra_encriptada =""
  for letra in palabra:
    if (letra in abecedario):
      indice = abecedario.find(letra)
      indice_encriptado = (indice+corrimiento)%27
      palabra_encriptada += abecedario[indice_encriptado]
    else:
      palabra_encriptada += letra


  print(palabra_encriptada)

'''
  #ejercisio 2

n = 1
dig_pares = 0
dig_inpares = 0
while n != 0:
  n = int(input("INGRESE UN NUMERO POSITIVO - PARA FINALIZAR INGRESE 0 "))
  if (n < 0):
    print("numero no valido")
  else:
    auxiliar = n
    dig_pares_p = 0
    dig_inpares_p = 0
    while auxiliar > 0:
      digito = auxiliar % 10
      if (digito % 2 == 0):
        dig_pares = dig_pares + 1
        dig_pares_p = dig_pares_p + 1
      else:
        dig_inpares_p = dig_inpares_p + 1
        dig_inpares = dig_inpares + 1
      auxiliar = math.floor(auxiliar/10)
    if(n!=0):
      print("hay ", dig_pares_p, " pares y ", dig_inpares_p, " inpares")
print("hay ", dig_pares, " pares y ", dig_inpares, " inpares")
