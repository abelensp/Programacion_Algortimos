sw=0
opc=0
opc2=0
carilla=250000
implante=475000
ortod=800000

trab=0
aux=0.15
adm=0.1
doc=0.05

contCa=0
contImp=0
contOrt=0

subtotal=0
desc=0

while opc!=3:
    
    print(35*"-")
    print("\tEL DIENTE DE ORO")
    print("\t      DUOC UC")
    print(35*"-")
    print("1. Cotización")
    print("2. Renunciar")
    print("3. Salir")
    print(35*"-")
    while True:
        try:
            opc=int(input("Seleccione: "))
            if 1<=opc<=3:
                break
            else:
                print("Seleccione una opción válida")
        except ValueError:
            print("Debe ingresar un valor numérico")
    
    if opc==1:
        while sw==0:
            try:
                trab=int(input("\nSeleccione que tipo de trabajador es:\n1) Auxiliar\n2) Administrativo\n3) Docente\n4) Otro\nSu opción: "))
                if 1<=trab<=4:
                    break
                else:
                    print("Seleccione una opción válida")
            except ValueError:
                print("Debe ingresar un valor numérico")

        while opc2!=4:
            print(40*"-")
            print("\tTratamientos disponible")
            print(40*"-")
            print("1. Carilla porcelana ($250 000)")
            print("2. Implantes dentales ($475 000)")
            print("3. Ortodoncia brackets ($800 000)")
            print("4. Listo")
            print(40*"-")
            while True:
                try:
                    opc2=int(input("Seleccione su tratamiento: "))
                    if 1<=opc2<=4:
                        break
                    else:
                        print("Seleccione una opción válida")
                except ValueError:
                    print("Debe ingresar un valor numérico")
            if opc2==1:
                contCa+=1
                print(f"{contCa} tratamiento(s) de Carilla de porcenala agregado!\n")
            elif opc2==2:
                contImp+=1
                print(f"{contImp} tratamiento(s) de Implantes dentales agregado!\n")
            elif opc2==3:
                contOrt+=1
                print(f"{contOrt} tratamiento(s) de Ortodoncia brackets agregado!\n")
            elif opc2==4:
                print("")
                print(60*"-")
                print("\t\t\tCotización")
                print(60*"-")
                print(f"--> {contCa} tratamiento(s) Carilla Porcelana\t\t${carilla*contCa}")
                print(f"--> {contImp} tratamiento(s) Carilla Porcelana\t\t${implante*contImp}")
                print(f"--> {contOrt} tratamiento(s) Carilla Porcelana\t\t${ortod*contOrt}")
                print(60*"-")
                subtotal=((carilla*contCa)+(implante*contImp)+(ortod*contOrt))
                print(f"Subtotal\t${subtotal}")
                if trab==1:
                    desc=subtotal*aux
                    print(f"Descuento 15%\t${desc}")
                elif trab==2:
                    desc=subtotal*adm
                    print(f"Descuento 10%\t${desc}")
                elif trab==3:
                    desc=subtotal*doc
                    print(f"Descuento 5%\t${desc}")
                else:
                    print("Descuento 0%\t$0")
                total=subtotal-desc
                print(60*"-")
                print(f"Total\t${total}")
                print(60*"-")
                print(f"Son 12 cuotas de:\t${round(total/12)}")
                print("\nSonría bonito!!!")
                opc2=0
                break
               
    elif opc==2:
        contCa=0
        contImp=0
        contOrt=0

        trab=0
        subtotal=0
        desc=0
        total=0

    else:
        print("Adiós!")
        opc=3
