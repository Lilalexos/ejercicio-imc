
def calcular_imc(peso, estatura):
    return peso / (estatura ** 2)

def clasificar_riesgo(imc):
    if imc < 18.5:
        return "peso por debajo del recomendado"
    elif 18.5 <= imc < 24.9:
        return "peso dentro del rango saludable"
    elif 25 <= imc < 29.9:
        return "por encima del peso ideal"
    elif 30 <= imc < 39.9:
        return "en el rango de obesidad"
    else:
        return "obesidad extrema, se recomienda atención médica"

cantidad_personas = int(input("cantidad de personas a registrar"))

for i in range(cantidad_personas):
    print(f"persona {i+1}")
    
    nombre = input("nombre")
    apellidos = input("apellidos")
    peso = float(input("peso en kg"))
    estatura = input("estatura en metros")
    
    estatura = float(estatura)

    imc = calcular_imc(peso, estatura)

    riesgo = clasificar_riesgo(imc)

    nombre_completo = f"{nombre} {apellidos}"
    print(f"{nombre_completo} tiene un imc de {imc:.2f}, lo que indica {riesgo}")

