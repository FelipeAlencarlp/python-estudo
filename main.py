if __name__ == '__main__':

    # tipo str
    nome = 'Felipe'

    print(type(nome))

    nome = 123

    print(type(nome))

    # tipo list
    professores = ['Felipe', 'Fabiano', 'Fabio', 'Patricia']

    print(type(professores))

    # tipo dict
    professor = {
        'nome' : 'Felipe',
        'estado' : 'Rio de Janeiro' 
    }

    print(type(professor))
    print(professor['nome'])

    # tipo complex
    n = 3 + 6j

    print(type(n))

    # interação com usuário
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))

    resultado = n1 + n2

    print(f'O resultado da soma é {resultado}')