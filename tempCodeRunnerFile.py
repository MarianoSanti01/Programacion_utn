age_job=int(input("¿cuantos años lleva en la empresa?\n"))
if (age_job<1):
    print("su utilidad es del 5 por cientod del salario")
elif(age_job==1):
    print("su utilidad es del 7 por ciento del salario")
elif(age_job>=2 and age_job<5):
    print("su utilidad es del 10 porciento del salario")
elif(age_job>=5 and age_job<10):
    print("su utilidad es del 15 por ciento del salario")
elif(age_job>=10):
    print("su utilidad es del 20 por ciento del salario")