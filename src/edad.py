from time import localtime

def evaluar(dia, mes, anno):
    year = anno

    t = localtime()
    a_day = t.tm_mday
    a_mes = t.tm_mon
    a_year = t.tm_year

    dif = a_year - year
    if(a_mes < mes and a_day < dia):
        dif-=1
    return f'Usted tiene {dif} años'

    return "";

if __name__ == '__main__':
    print("Ingrese su fecha de nacimiento")
    print("Día:", end="")
    dia = int(input())
    print("Mes:", end="")
    mes = int(input())
    print("Año:", end="")
    anno = int(input())
        
    respuesta = evaluar(dia, mes, anno)
    print(respuesta)
