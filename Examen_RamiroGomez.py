import csv
import time
import os
import random

trabajadores=[
    ["Juan Pérez",random.randint(300000, 2500000)],
    ["María García", random.randint(300000, 2500000)],
    ["Carlos López", random.randint(300000, 2500000)],
    ["Ana Martínez", random.randint(300000, 2500000)],
    ["Pedro Rodríguez", random.randint(300000, 2500000)],
    ["Laura Hernández", random.randint(300000, 2500000)],
    ["Miguel Sánchez", random.randint(300000, 2500000)],
    ["Isabel Gómez", random.randint(300000, 2500000)],
    ["Francisco Díaz", random.randint(300000, 2500000)],
    ["Elena Fernández", random.randint(300000, 2500000)]]

def asignar_sueldos(trabajadores):
    for i in range(len(trabajadores)):
        print(trabajadores[i])
    print("="*40)
    print("Sueldos agregados de forma satisfactoria !!")    
    input(">> PRECIONE ENTER PARA VOLVER AL MENU PRINCIPAL")   
    
def claisficar_sueldos(trabajadores):
    for i in range(len(trabajadores)):
        if trabajadores[i][1]<=800000:
            rango="Sueldos menores a $800.000"
        elif trabajadores[i][1]<=2000000:
            rango="Sueldos entre $800.000 y $2.000.000"
        else:
            rango="Sueldos superiores a $2.000.000"
            
        print(f"NOMBRE DEL TRABAJADOR: {trabajadores[i][0]} | SUELDO: ${trabajadores[i][1]} {rango}\n")        
        
def ver_estadisticos(trabajadores):
    sueldo_alto=1
    for i in range(len(trabajadores)):
        if trabajadores[i][1]>sueldo_alto:
            sueldo_alto=trabajadores[i][1]
    print(f"EL SUELDO MAS ALTO ES DE: ${sueldo_alto}")   
    
    sueldo_bajo=2500000
    for i in range(len(trabajadores)):
        if trabajadores[i][1]>sueldo_bajo:
            sueldo_bajo=trabajadores[i][1]
    print(f"EL SUELDO MAS BAJO ES DE: ${sueldo_bajo}")
         
    suma_total=0
    for i in range(len(trabajadores)):
        suma_total=trabajadores[i][1]+suma_total
    promedio=suma_total/10
    print(f"EL PROMEDIO DE TODOS LOS SUELDOS ES DE: ${promedio} ")
    
    media_geometrica=1
    for i in range(len(trabajadores)):
        media_geometrica=trabajadores[i][1]*media_geometrica
    media_geometrica=media_geometrica**(1/len(trabajadores))
    print(f"LA MEDIA GEOMETRICA DE TODOS LOS SUELDOS ES: ${media_geometrica}")        

def reporte_de_sueldos(trabajadores):
    with open("PLANTILLA_SUELDOS.CSV", "w", newline="", encoding="utf-8") as archivo:
        escribir=csv.writer(archivo)
        
        print("DESEA APLICAR LOS DESCUENTOS DE AFP Y SALUD ?")
        descuentos=input("SI/NO: ").lower()
        if descuentos=="si":
            for i in range (len(trabajadores)):
                des_afp=trabajadores[i][1]*0.12
                des_salud=trabajadores[i][1]*0.07
                sueldo_liquido=trabajadores[i][1]-des_afp-des_salud
                escribir.writerow([f"NOMBRE EMPLEADO: {trabajadores[i][0]} | SUELDO BRUTO: ${trabajadores[i][1]} | DESCUENTO SALUD: ${des_salud} | DESCUENTO AFP: ${des_afp} | SUELDO LIQUIDO: ${sueldo_liquido}"])
                print(f"NOMBRE EMPLEADO: {trabajadores[i][0]} | SUELDO BRUTO: ${trabajadores[i][1]} | DESCUENTO SALUD: ${des_salud} | DESCUENTO AFP: ${des_afp} | SUELDO LIQUIDO: ${sueldo_liquido}\n")
            print("SE A CREADO UN ARCHICO CSV LLAMADO PLANILLA_SUELDOS.CSV")
        else:
            for i in range (len(trabajadores)):
                des_afp=trabajadores[i][1]*0.12
                des_salud=trabajadores[i][1]*0.07
                sueldo_liquido=trabajadores[i][1]-des_afp-des_salud
                escribir.writerow([f"NOMBRE EMPLEADO: {trabajadores[i][0]} | SUELDO BRUTO: ${trabajadores[i][1]} | DESCUENTO SALUD: $ 0 | DESCUENTO AFP: $ 0 | SUELDO LIQUIDO: $ 0"])
                print(f"NOMBRE EMPLEADO: {trabajadores[i][0]} | SUELDO BRUTO: ${trabajadores[i][1]} | DESCUENTO SALUD: $ 0 | DESCUENTO AFP: $ 0 | SUELDO LIQUIDO: $ 0\n")
            print("SE A CREADO UN ARCHICO CSV LLAMADO PLANILLA_SUELDOS.CSV")
            

while True:
    print("="*30)
    print("Base de datos trabajadores")
    print("="*30)
    print("1.- Asignar sueldos aleatorios")
    print("2.- Clasificar sueldos")
    print("3.- Ver estadisticos")
    print("4.- Reporte sueldos")
    print("5.- Salir del programa")
    print("="*30)
    try:
        opc=int(input("Seleccione la opcion que desee ejecutar: "))
    except ValueError:
        print(">> Recuerde solo ingresar numeros y sin decimales <<")
    time.sleep(2)
    os.system("cls")  
       
    match opc:
        case 1:
            asignar_sueldos(trabajadores)
        case 2:
            claisficar_sueldos(trabajadores)   
        case 3:
            ver_estadisticos(trabajadores)   
        case 4:
            reporte_de_sueldos(trabajadores)
        case 5:
            print("DESEA CERRAR EL PROGRAMA ?")
            sino=input("SI/NO: ").lower()
            if sino=="si":
                print("CERRANDO EL PROGRAMA")
                time.sleep(0.5)
                print("....")
                time.sleep(0.5)
                print("...")
                time.sleep(0.5)
                print("..")
                time.sleep(0.5)
                print(".")
                time.sleep(0.5)
                os.system("cls")
                print("="*30)
                print("Desarrollado por Ramiro Gomez")
                print("Rut: 18.974.701-2")
                print("="*30)
                break
                 
        case _:
            print(">> OPCION FUERA DE RANGO <<")