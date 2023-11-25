class Animal:
    def __init__(self, nome, tamanho):
        self.nome = nome,
        self.tamanho = tamanho

    def respirar(self):
        print(f'O Animal {self.nome} está respirando. O tamanho dele é {self.tamanho}')