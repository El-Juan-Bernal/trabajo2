

personas=[]


def agregar_persona():
    while True:
        nombre=input("Ingrese su nombe: ")
        if len(nombre)>=3 and nombre.isalpha:
            break
        else:
            print("Nombre inválido")

    while True:
        apellido=input("Ingrese su apellido: ")
        if len(apellido)>=3 and apellido.isalpha:
            break
        else:
            print("Apellido inválido")

    while True:
        rut=(input("Ingrese su Rut: "))
        if len(rut)>8 and ("-") in rut:
            break
        else:
            print("Rut inválido")

    while True:
        edad=int(input("Ingrese su edad: "))
        if edad >=18 and edad <120:
            break
        else:
            print("Edad inválida")
            
    while True:
        estado_civil=input("Ingrese su estado civil:\n C: Casado/a\n S: Soltero/a\n V: Viudo/a\n : ")
        if "c" in estado_civil or "s" in estado_civil or "v" in estado_civil:
            break
        else:
            print("Opción no válida")

    while True:
        correo_electronico=input("Ingrese su correo: ")
        if len(correo_electronico)>=5 and '@' in correo_electronico and '.' in correo_electronico:
            break
        else:
            print("Correo electrónico no válido")

    while True:
        fecha_afiliacion=(input("Ingrese su fecha de nacimiento en formato DD MM AA: "))
        if len(fecha_afiliacion)>=4 and fecha_afiliacion .isnumeric:
            break
        else:
            print("Fecha no válida")
    
    persona = {
        "Nombre":nombre,
        "Apellido":apellido,
        "Rut":rut,
        "Edad":edad,
        "Estado civil":estado_civil,
        "Correo electronico":correo_electronico,
        "Fecha afiliacion":fecha_afiliacion
    }
    personas.append(persona)

#    print(personas)



# En esta parte me enrredo un poco de como escribir bien para hacer la busqueda...

def buscar():
    for persona in personas:
        if (personas[4]=="c"):
            print(personas)
        if (personas[4]=="s"):
            print(personas)
        if (personas[4]=="v"):
            print(personas)
        else:
            print("No hay personas para mostrar")



def imprimir_certificado():
    rut_buscar=int(input("Ingrese Rut a buscar: "))
    if rut_buscar in personas:
        print("CERTIFICADO AFILIACIÓN ISAPRE VIDA Y SALUD")
        print("Se otorga el presente certificado de afiliación a: ")
        print(personas)
        print("Se otorga este certificado de afiliación para los fines que estime conveniente.\n Sin otro particular\n Isapre Vida y Salud")





while True:
    print("-"*30)
    print("Isapre Vida y Salud")
    print("-"*30)

    print("""
    1. Registrar una persona
    2. Buscar una persona
    3.Imprimir certificado afiliación

    0. Salir

    """)
    op=input("Seleccione una opción: ")
    match op: 
        case "1":
            agregar_persona()

        case "2":
            buscar()
        

        case "3":
            imprimir_certificado()



        case "0":
            break

