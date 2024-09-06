def evaluar(anno):
    year = anno

    if(year >= 1582):
        if(year%100==0) and (year % 400 != 0):
            return f'{year} no es bisiesto'
        elif(year % 4 == 0):
            return f'{year} es bisiesto'
        else:
            return f'{year} no es bisiesto'
    else:
        if(year % 4 == 0):
            return f'{year} es bisiesto'
        else:
            return f'{year} no es bisiesto'
    return "";

if __name__ == '__main__':
    print("Año:", end="")
    anno = int(input())

    respuesta = evaluar(anno)
    print(respuesta)
