#Ejercicio de cálculo del IMC

estatura = float(input("Ingrese su estatura en centimetros:"))
peso = float(input("Ingrese su peso en kilogramos:"))

#La formula de calculo es el peso dividido por la estatura al cuadrado
imc = peso / ((estatura/100) ** 2)
print("Su indice de masa corporal es:", imc)
if imc < 16:
    print("Su estado es de delgadez severa")
if imc > 40:
    print("Su estado es de obeso tipo III")
elif imc > 35 :
    print("Su estado es obeso tipo II")
elif imc > 30 :
    print("Su estado es obeso tipo I")
elif imc > 25 :
    print("Su estado es de sobrepeso")
elif imc > 18.5 :
    print("Su estado es normal")
elif imc > 17 :
    print ("Su estado es de delgadez aceptable")
elif imc > 16 :
    print("Su estado es de delgadez moderada")