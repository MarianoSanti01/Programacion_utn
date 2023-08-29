#ejercisio 1
palabra_encriptada =""
abecedario="abcdefghijklmnñopqrstuvwxyz"
corrimiento=int(input("¿cual es el corrimiento? "))
palabra=""
for i in range(1):
  palabra = input("ingrese el mensaje ")
  for letra in palabra:
    if (letra in abecedario):
      indice = abecedario.find(letra)
      indice_encriptado = (indice+corrimiento)%27
      palabra_encriptada += abecedario[indice_encriptado]
    else:
      palabra_encriptada += letra


  print(palabra_encriptada)