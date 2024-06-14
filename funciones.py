trabajadores = []
cargos = ("CEO","DESARROLLADOR","ANALISTA")

def opcion_1():
    print("REGISTRAR TRABAJADOR")
    nombre_apellido = input("Ingrese su nombre y apellido: ")
    cargo = int(input("Ingrese cargo(1:CEO, 2:DESARROLLADOR, 3:ANALISTA): "))
    sueldo_bruto = int(input("Ingrese sueldo bruto: "))
    desc_salud = int(7/100 * sueldo_bruto)
    desc_afp = int(0.12 * sueldo_bruto)
    sueldo_liquido = sueldo_bruto-desc_salud-desc_afp
    trabajador = [nombre_apellido,cargos[cargo-1],sueldo_bruto,desc_salud,desc_afp,sueldo_liquido]
    trabajadores.append(trabajador)
    print("TRABAJADOR REGISTRADO CON ÉXITO!")

def opcion_2():
    if len(trabajadores)==0:
        print("No existen trabajadores, elija la opción 1")
    else:
        print("\tLISTA DE TRABAJADORES")
        print("Trabajador\tCargo\tSueldo Bruto\tDesc. Salud\tDesc. AFP\tLíquido a pagar")
        for t in trabajadores: #t: sería cada trabajador de la lista, t es una lista
            print(f"{t[0]}\t{t[1]}\t{t[2]}\t\t\t{t[3]}\t\t{t[4]}\t\t{t[5]}")

def opcion_3():
    if len(trabajadores)==0:
        print("No existen trabajadores, elija la opción 1")
    else:
        opc2 = int(input("¿Qué cargo desea imprimir?(1:CEO, 2:DESARROLLADOR, 3:ANALISTA, 4: TODOS)"))
        if opc2==4: 
            with open("todos_trabajadores.txt","w", newline="\n") as archivo:
                for t in trabajadores:
                    texto = f"{t[0]} {t[1]} {t[2]} {t[3]} {t[4]} {t[5]}\n"
                    archivo.write(texto)
            print("ARCHIVO CREADO CON ÉXITO!")
        else:
            with open("trabajadores_por_cargo.txt","w") as archivo:
                for t in trabajadores:
                    if cargos[opc2-1]==t[1]:
                        texto = f"{t[0]} {t[1]} {t[2]} {t[3]} {t[4]} {t[5]}\n"
                        archivo.write(texto)
        print("ARCHIVO CREADO CON ÉXITO!")

def opcion_4():
    print("Gracias por usar el programa, adios!")
    exit()