def recortar(numero_recortar, limite_inferior, limite_superior):
    if(numero_recortar < limite_inferior):
        return limite_inferior
    
    elif(numero_recortar > limite_superior):
        return limite_superior

    else:
        return numero_recortar
        
def main():
    print(recortar(15, 0, 10))

main()