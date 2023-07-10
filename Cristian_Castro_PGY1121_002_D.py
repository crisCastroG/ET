import os
from datetime import date
os.system("cls")

listUbi = []
listVen = []
cantPlt = 0
cantGld = 0
cantSlv = 0
n = 1
f = 0
c = 0
vacio = "X"

for i in range(10):
    listUbi.append([])

for i in range(10):
    for j in range(10):
        listUbi[i].append(n)
        n = n+1

def mostrarAsientos():
    print("""
------------------------------------------
|               ESCENARIO                | 
------------------------------------------""")
    for i in range(10):
        if i != 0:
            print()
        for j in range(10):
            if listUbi[i][j] == 0:
                print(f"{vacio:>4s}", end = "")
            else:
                print(f"{listUbi[i][j]:4d}", end="")
    

def mostrarPrecios():
    print("""
    ° Platinum  $120.000 (1  a 20)
    ° Gold       $80.000 (21 a 50)
    ° Silver     $50.000 (51 a 100)
    """)

def comprarEntradas():
    global cantPlt
    global cantGld
    global cantSlv
    while True:
        try:
            cant = int(input("Ingrese cantidad de entradas (1 a 3): "))
            if cant < 1 or cant > 3:
                input("La cantidad de entradas es inválida, ingrese nuevamente.")
                os.system("cls")
            else:
                while cant > 0:
                    mostrarAsientos()
                    try:
                        print()
                        mostrarPrecios()
                        opc = int(input("Ingrese un asiento disponible para comprar: "))
                        f = (opc - 1) // 10
                        c = (opc - 1) % 10
                        if opc > 100 or opc < 1 or listUbi[f][c] == 0:
                            input("La ubicación seleccionada no está disponible, ingrese nuevamente.")
                        else:
                            listUbi[f][c] = 0
                            while True:
                                try:
                                    run = int(input("Ingrese el RUN de la persona para este asiento: "))
                                    if run < 0:
                                        input("RUN inválido, ingrese nuevamente")
                                    else:
                                        listVen.append([run, opc])
                                        if opc >= 1 and opc <= 20:
                                            cantPlt = cantPlt + 1
                                        elif opc >= 21 and opc <= 50:
                                            cantGld = cantGld + 1
                                        elif opc >=  51:
                                            cantSlv = cantSlv +1                                    
                                        cant = cant - 1     
                                        input("Operación exitosa.")
                                        os.system("cls")
                                        break                                                                   
                                except:
                                    input("Error, el RUN a ingresar solo debe contener números, sin puntos ni guión")
                                    os.system("cls")                   
                    
                    except:
                        input("EXCEPCION OPCION")
                        os.system("cls")
                break                           
        except:
            input("EXCEPCION DE CANTIDAD")
            os.system("cls")
    
        

def verAsistentes():
    listVen.sort()
    print("""
    LISTADO DE ASISTENTES
RUN                  ASIENTO""")
    for i in range(len(listVen)):
        print(f"{listVen[i][0]:<20d}    {listVen[i][1]:>5d}")
    

def mostrarGanancias():
    cantTot = cantPlt + cantGld + cantSlv
    total = cantPlt * 120000 + cantGld * 80000 + cantSlv * 50000
    print(f"""
    Tipo entrada          Cantidad          Total
 Platinum $120.000           {cantPlt:<12d}   ${cantPlt * 120000:<10d}
 Gold     $80.000            {cantGld:<12d}   ${cantGld * 80000:<10d}
 Silver   $50.000            {cantSlv:<12d}   ${cantSlv * 50000:<10d}
 TOTAL                       {cantTot:<12d}   ${total:<10d}
 """)
    
print("Bienvenido al sistema de venta de entradas.")
while True:
    print("""
1. Comprar entradas
2. Mostrar ubicaciones disponibles
3. Ver listado de asistentes
4. Mostrar ganancias totales
5. Salir
    """)
    try:
        opc = int(input("Ingrese una opción: "))
        if opc < 1 or opc > 5:
            input("Opción inválida, ingrese nuevamente")
            os.system("cls")
        elif opc == 1:
            os.system("cls")
            comprarEntradas()
        elif opc == 2:
            os.system("cls")
            mostrarAsientos()
            input()
            os.system("cls")
        elif opc == 3:
            os.system("cls")
            verAsistentes()
            input()
            os.system("cls")
        elif opc == 4:
            os.system("cls")
            mostrarGanancias()
            input()
            os.system("cls")
        elif opc == 5:
            input(f"Cerrando sistema... Hasta pronto Cristian Castro. {date.today()}")
            break     
    except:
        input("EXCEPCION OPCION")
        os.system("cls")

