# Funciones en python

def suma(num1, num2): #parametros
    return num1 + num2

def division(num1,num2):
    return num1 / num2

print("la suma es : ", suma(2,3)) #(2,3) son argumentos
print("la suma es : ", suma(7,6))

print("la suma es : ", 8+8)

print("la division 3/7 es : ", division(3,7))

print("la division 7/3 es : ", division(num2=3,num1=7))

# funciones con parametros  por default
#calculadora de alimento mensual y dia por animal

cantConsDia = float(input("cuanto consume por dia en gramos : "))
precioEst = float(input("cuanto cuesta el kg de alimento : "))
print("#"*80)
print("Para terminar complete con 0 ambos ingresos de datos")
print("#"*80)


def costoKg(precioEst, kilosMensuales) :
        costoTotal = precioEst * kilosMensuales
        return costoTotal

def kilos(gramos, dias=30) :
     gramosMensual =gramos * dias
     kilosMensual = gramosMensual/1000
     return kilosMensual 

while (cantConsDia !=0 and precioEst !=0):
    print("En el mes, el animal va a consumir ", kilos(cantConsDia)," kilos ")
    print("En el mes, vas a gastar en el animal  ", costoKg(precioEst , kilos(cantConsDia)), "pesos")
    cantConsDia = float(input("cuanto consume por dia en gramos : "))
    precioEst = float(input("cuanto cuesta el kg de alimento : "))
    print("#"*60)
    print("Para terminar complete con 0 ambos ingresos de datos")
    print("#"*60)
print("#"*40)
print ("Fin programa Funciones alimento mascota")
print("#"*40)


# def nombreFincion(parametros):
# bloque de codigo a ejecutar
# 


def sumaEnteros (num1,num2): #parametros
#    print("hola como estas? los numeros que me pasaste son: ", num1, " y ", num2)
    suma= num1 + num2
    #return num1 + num2
    return suma

resultadoSuma = sumaEnteros(2,3) #argumentos posicionales
print("El resultado de la suma es: ", resultadoSuma)

#var1 = 67
#print("lo que hay en VAR1 es: ",var1)

print("la suma entre 3 y 3 es : ", sumaEnteros(3,3)) #6


#argumrnyod por valor y por referencia

#por valor(trabajamos con respresentaciones de esos valores cuando los valores son )
#int, str, boo,float

#cuando se trabaja con un argumento por valor no se modifica el dato como tal al ser porcesado por la lista

def triplicarNumero(numero):
    return numero *3

def triplicarNumero2(numero):
    numero= numero *3
    return numero

#num1 = 2

#print(triplicarNumero(num1))
#print(num1)

numero=2
print(triplicarNumero2(numero))
print (numero)

#Argumentos por referencia


def duplicarArray(array):
    for i in range(len(array)):
        array[i]=array[i] *2
    return array

miArray = [2,4,6]
print("mi array antes de la funcion : ", miArray)
print("mi array con la funcion :", duplicarArray(miArray))
print("como quedo mi array despues : ",miArray)    
