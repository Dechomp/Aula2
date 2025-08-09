from MediaSalas import mediaSalas
def main():
    nomeEscola = input("Digite o nome da escola: ")

    numeroSalas = 0

    while numeroSalas <= 0:
        numeroSalas = int (input ("Digite a quantidade de salas: "))

        if numeroSalas <= 0:
            print("Valor inválido, digite novamente!\n")
    
    mediasSalas = [0.0] * numeroSalas 
    nomeSalas = [""] * numeroSalas 
    i = 0

    while i < numeroSalas:
        quantidadeAlunos = 0

        nomeSala = input ("Digite o nome da sala: ")

        nomeSalas[i] = nomeSala

        while quantidadeAlunos <= 0:
            quantidadeAlunos = int ( input ("Digite a quantidade de alunos desta sala: "))
            if quantidadeAlunos <=0:
                print("Número inválido, digite novamente")
        
        mediaSalas(quantidadeAlunos)
        i+=1

        





    return 0
main()