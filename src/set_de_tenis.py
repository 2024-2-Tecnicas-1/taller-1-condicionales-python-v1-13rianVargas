def evaluar(num_victorias_a, num_victorias_b):
    a = num_victorias_a
    b = num_victorias_b

    if a >= 6 or b >= 6:
        if(a < 7 and b < 7 and a == b):
            return "Aún no termina"
        elif(a == 6 and b+2 <=a):
            return "Ganó A"
        elif(b == 6 and a+2 <= b):
            return "Ganó B"
        elif(b == 6 and a+1 == b) or (a == 6 and b+1 == a):
            return "Aún no termina"
        else:
            if(a == 7 and b == 6) or (a == 7 and b == 5):
                return "Ganó A"    
            elif (b == 7 and a == 5) or (b == 7 and a == 6):
                return "Ganó B"
            else:
                return "Inválido"
    else:
        return "Aún no termina"
    return "";

if __name__ == '__main__':
    print("Los juegos ganaddor por A:", end="")
    num_victorias_a = int(input())
    print("Los juegos ganaddor por B:", end="")
    num_victorias_b = int(input())

    respuesta = evaluar(num_victorias_a, num_victorias_b)
    print(respuesta)
