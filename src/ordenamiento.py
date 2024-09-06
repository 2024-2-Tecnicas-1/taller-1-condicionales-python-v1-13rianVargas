def evaluar(numero1, numero2, numero3, numero4):
    n = [numero1,numero2,numero3,numero4]
    n.sort()
    return f'{n[0]} {n[1]} {n[2]} {n[3]}'
    return "";

if __name__ == '__main__':
    print("Número 1:", end="")
    numero1 = int(input())
    print("Número 2:", end="")
    numero2 = int(input())
    print("Número 3:", end="")
    numero3 = int(input())
    print("Número 4:", end="")
    numero4 = int(input())
        
    respuesta = evaluar(numero1, numero2, numero3, numero4)
    print(respuesta)
