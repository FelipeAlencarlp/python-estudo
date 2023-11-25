from Animal import Animal

class Reptil(Animal):
    def __init__(self, nome, tamanho):
        super().__init__(nome, tamanho)
    
    def botarOvo(self):
        print(f'O animal {self.nome} está botando um ovo.')