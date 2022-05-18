def año_bisiesto(year):
    if((year % 4 == 0) and (year % 400 == 0 or year % 100)):
        print(f"El año {year} es bisiesto")
    
    else:
        print(f"El año {year} no es bisiesto")


def main():
    isRunning = True;

    while(isRunning):
        year = input("Ingrese un año (-1 para finalizar): ")
        
        if(year.isnumeric()):
            año_bisiesto(int(year))

        elif(year == "-1"):
            isRunning = False
            print("Saliendo...")
            
        else:
            print("Debe ingresar un valor que sea numerico.")

main()