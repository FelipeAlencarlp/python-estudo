if __name__ == '__main__':
    pessoas = ['Felipe', 'Rafael', 'Douglas']

    pessoas.append('Ana')
    print(pessoas)

    pessoas.insert(0, 'Paty')
    print(pessoas)

    pessoas.remove('Felipe')
    print(pessoas)

    pessoas.sort()
    print(pessoas)

    quantidade = pessoas.count('Ana') # ou len(pessoas), retorna a quantidade total da lista
    print(quantidade)

    pessoas.clear()
    print(pessoas)