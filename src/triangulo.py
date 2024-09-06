def evaluar(a, b, c):
    if(a+b)>c and (a+c)>b and (b+c)>a:
        ar = [a,b,c]
        pr = set(ar)
        t = len(pr)
        if(t == 1):
            return f'El triángulo es equilátero'
        elif(t == 2):
            return f'El triángulo es isósceles'
        else:
            return f'El triángulo es escaleno'
    else:
        return "No es un triángulo válido"

    return ""

if __name__ == '__main__':
    print("a:", end="")
    a = float(input())
    print("b:", end="")
    b = float(input())
    print("c:", end="")
    c = float(input())
        
    respuesta = evaluar(a, b, c)
    print(respuesta)
