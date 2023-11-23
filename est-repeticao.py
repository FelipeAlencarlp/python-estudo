if __name__ == '__main__':

    pessoas = ["Felipe", "Patricia", "Ana", "João"]

    for i, p in enumerate(pessoas, start=1):
        print(f'A pessoa é {p} está no index {i}')

    contador = 0

    while contador < 3:
        print(f'Lavando carro na posição {contador}')
        contador += 1
    else:
        print('Terminou de lavar os carros.')