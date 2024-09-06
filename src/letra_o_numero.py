def evaluar(caracter):
    n = ord(caracter)

    if(n >= 65 and n <= 90):
        return "Es letra mayúscula"
    elif(n >= 97 and n <= 122):
        return "Es letra minúscula"
    elif(caracter.isdigit()):
        return "Es número"
    else:
        return "No es letra ni número"
    
    return "";

if __name__ == '__main__':
    print("Caracter:", end='')
    caracter = input()
        
    respuesta = evaluar(caracter)
    print(respuesta)
