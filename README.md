# Programacion_utn
nombre: Juan cruz Berrios
gmail: juancruzberrios73@gmail.com

#lunes=inicial/martes=intermiedio/miercoles=avanzado/jueves=practica/viernes=ingles
#ingresar dia(dd/mm) verfica que fecha exista, dia de semana puede ser minuscula o mayus 
#encontrar ", & /" separar el dia de la semana con elif 
dia_string = input("ingrese dia de la semana, y la fecha ")
dia=dia_string.split(",")
dia_semana=(dia[0]).lower()
dia_fecha=dia[1].split("/")
dia_mes=int(dia_fecha[0])
mes=int(dia_fecha[1])
if (dia_mes > 31 ) or (mes>12):
  print("fecha no valda")

semana=["lunes","martes","miercoles"]
if(dia_semana in semana):
  aprovados=input("ingrese los alumnos aprovados ")
  desaprovados=input("ingrese los alumnos desaprovados ")
  aprovados_num=int(aprovados)
  desaprovados_num=int(desaprovados)
  print("el porcentaje de aprovados es ", (aprovados_num*100)/(aprovados_num+desaprovados_num))
elif (dia_semana == "jueves"):
  asistencia=input("ingrese porcentaje de la asistencia del dia ")
  asistencia_num=int(asistencia)
  if (asistencia_num > 50):
    print("asistieron mas de la mitad")
  else:
    print("asistieron la mitad o menos")
elif(dia_semana=="viernes"):
  if (dia_mes==1) and (mes==1):
    print("comienza nuevo ciclo!")
    cant_alumnos=input("ingrese el numero de alumnos ")
    cant_alumnos_num=int(cant_alumnos)
    arancel=input("ingrese aransel por cada alumno ")
    arancel_num=int(arancel)
    print("el total es de: ",(arancel_num * cant_alumnos_num))
  else:
    print("fin")
else:
  print("ese dia de la semana no tiene actividades")
