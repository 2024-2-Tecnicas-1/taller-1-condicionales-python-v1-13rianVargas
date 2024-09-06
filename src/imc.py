def evaluar(peso, estatura, edad):
    op = peso/(estatura**2)

    if(edad < 45):
        if(op < 22.0):
            return "bajo"
        else:
            return "medio"
    else:
        if(op < 22):
            return "medio"
        else:
            return "alto"

    return "";

if __name__ == '__main__':
    print("Peso:", end="")
    peso = int(input())
    print("Estatura:", end="")
    estatura = float(input())
    print("Edad:", end="")
    edad = int(input())
        
    respuesta = evaluar(peso, estatura, edad)
    print(respuesta)
