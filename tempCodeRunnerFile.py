abecedario="abcdefghijklmnñopqrstuvwxyz"
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

