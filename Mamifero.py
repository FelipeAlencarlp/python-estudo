from Animal import Animal


class Mamifero(Animal):
    def __init__(self, nome, tamanho):
        super().__init__(nome, tamanho)

    def alimentar(self):
        print(f'O animal {self.nome} está se alimentando.')