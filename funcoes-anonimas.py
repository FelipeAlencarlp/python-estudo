if __name__ == '__main__':

    notasDosAlunos = [80, 75, 88, 50, 95]

    mediaDasNotas = lambda notas : sum(notas) / len(notas)

    print(mediaDasNotas(notasDosAlunos))