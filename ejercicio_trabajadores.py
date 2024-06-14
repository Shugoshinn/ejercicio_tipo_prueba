import os, time

trabajadores = []
while True:
    print("MENÚ TRABAJADORES")
    print("1. Registrar trabajador")
    print("2. Listar todos los trabajadores")
    print("3. Imprimir planilla de sueldos")
    print("4. Salir del programa")
    opc = int(input("Ingrese opción: "))
    os.system('cls')
    if opc==1:
        print("REGISTRAR TRABAJADOR")
        nombre_apellido = input("Ingrese su nombre y apellido: ")
        cargo = int(input("Ingrese cargo(1:CEO, 2:DESARROLLADOR, 3:ANALISTA): "))
        sueldo_bruto = int(input("Ingrese sueldo bruto: "))
        desc_salud = int(7/100 * sueldo_bruto)
        desc_afp = int(0.12 * sueldo_bruto)
        sueldo_liquido = sueldo_bruto-desc_salud-desc_afp
        trabajador = [nombre_apellido,cargo,sueldo_bruto,desc_salud,desc_afp,sueldo_liquido]
        trabajadores.append(trabajador)
        print("TRABAJADOR REGISTRADO CON ÉXITO!")
    elif opc==2:
        pass
    elif opc==3:
        pass
    else:
        print("Gracias por usar el programa, adios!")
        break
    time.sleep(3)