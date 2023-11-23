def somar(numero1, numero2):
    print(f'Realizando soma de {numero1} + {numero2}')
    return numero1 + numero2

def subtrair(numero1, numero2):
    print(f'Realizando subtração de {numero1} - {numero2}')
    return numero1 - numero2

def multiplicar(numero1, numero2):
    print(f'Realizando multiplicação de {numero1} * {numero2}')
    return numero1 * numero2

def divisao(numero1, numero2):
    print(f'Realizando divisão de {numero1} / {numero2}')
    return numero1 / numero2

if __name__ == '__main__':

    # exercício
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))

    op = input('Qual operação matemática você deseja? (+, -, /, *): ')

    resultado = 0

    if op == '+':
        resultado = somar(n1, n2)

    elif op == '-':
        resultado = subtrair(n1, n2)

    elif op == '*':
        resultado = multiplicar(n1, n2)

    elif op == '/':
        resultado = divisao(n1, n2)

    else:
        print('Operador incorreto')

    print(f'O resultado da operação é {resultado}')

