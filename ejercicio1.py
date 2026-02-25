# Programa para saber cuando se va a pensionar una persona
nombre = input("Hola, cual es tu nombre?")
print("Hola", nombre)

edad = int(input("que edad tienes?"))
while edad <= 0:
    print("Edad invalida, ingresa edad mayor a 0")
    edad = int(input("que edad tienes?"))  

genero = input("Hombre o Mujer:").lower()
while genero != "hombre" and genero != "mujer":
    print ("Genero invalido")
    genero = input("Hombre o Mujer:").lower()

semanas_cotizadas = int(input("Cuantas semanas cotizadas tienes actualmente?"))
#Calcular semanas para pension 1300 semanas
#Mujer: 57 años Hombre: 62 años

if genero == "mujer": 
    edad_para_pension = 57 - edad 
    semanas_para_pension = 1300 - semanas_cotizadas
    print("En terminos de edad, te faltan", edad_para_pension,
          "años y en terminos de semanas, te faltan", semanas_para_pension, "semanas para pensionarte")

elif genero == "hombre":
    edad_para_pension = 63 - edad 
    semanas_para_pension = 1300 - semanas_cotizadas
    print("En terminos de edad, te faltan", edad_para_pension,
           "años y en terminos de semanas, te faltan",semanas_para_pension, "semanas para pensionarte")


