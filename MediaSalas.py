from MediaAluno import mediaAluno
def mediaSalas(quantidade):
    i = 0

    notaAlunos = [0.0] * quantidade
    nomeAlunos = [""] *  quantidade

    notaAlunoMaior = 0
    nomeAlunoMaior = ""
    while i < quantidade:
        nomeAluno = input("Digite o nome do aluno: ")
        nomeAlunos[i] = nomeAluno
        notaAlunos[i] = mediaAluno()

        if notaAlunos[i] > notaAlunoMaior:
            notaAlunoMaior = notaAlunos[i]
            nomeAlunoMaior = nomeAluno
        i += 1

    i = 0

    while i < quantidade:
        print("O aluno", nomeAlunos[i], f"tirou {notaAlunos[i]:,.2}")
        i+=1

    print("O aluno", nomeAlunoMaior, "Tirou a naior nota, que foi de", notaAlunoMaior          )