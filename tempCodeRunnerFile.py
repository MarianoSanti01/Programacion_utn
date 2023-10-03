from functions.numbers_addition import *
days=int(input("de cuantos dias quiere saber la temperatra media? \n"))
for i in range(days):
    print("dia ",i)
    max_temp=int(input("ingrese temperatura maxima del dia en celsius del dia \n"))
    minimal_temp=int(input("ingrese temperatura minima del dia en celcius del dia \n"))
    mid_temp=middle_temp(max_temp,minimal_temp)
    print("la temperatura minima del dia",i ,"es de: ",mid_temp)