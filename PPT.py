import random

escolhas = ["pedra", "papel", "tesoura"]

derrotas = 0
vitorias = 0
empate = 0 

while(True):
    computador = random.choice(escolhas)
    jogador = None

    while jogador not in escolhas:
        jogador = input("escolha Pedra, Papel ou Tesoura: ").lower()

        if jogador == computador:
            print("Computador: ", computador)
            print("Jogador: ", jogador)
            print("EMPATE!!")
            empate = empate + 1

        elif jogador == "pedra":
            if computador == "papel":
                print("Computador: ", computador)
                print("Jogador: ", jogador)
                print("VOCÊ PERDEU!!")
                derrotas = derrotas + 1 

            if computador == "tesoura":
                print("Computador: ", computador)
                print("Jogador: ", jogador)
                print("VOCÊ VENCEU!!")
                vitorias = vitorias + 1
                
        elif jogador == "tesoura":
            if computador == "pedra":
                print("Computador: ", computador)
                print("Jogador: ", jogador)
                print("VOCÊ PERDEU!!")
                derrotas = derrotas + 1 

            if computador == "papel":
                print("Computador: ", computador)
                print("Jogador: ", jogador)
                print("VOCÊ VENCEU!!")
                vitorias = vitorias + 1
                
        elif jogador == "papel":
            if computador == "tesoura":
                print("Computador: ", computador)
                print("Jogador: ", jogador)
                print("VOCÊ PERDEU!!")
                derrotas = derrotas + 1 

            if computador == "pedra":
                print("Computador: ", computador)
                print("Jogador: ", jogador)
                print("VOCÊ VENCEU!!")
                vitorias = vitorias + 1
    
    

    novamente = input("Você deseja jogar novamente? (Sim/Não): ").lower()
    if(novamente != "sim"):
        print(f"\nAo final do jogo você obteve:\n\n{vitorias} vitórias\n{derrotas} derrotas\ne {empate} empates !!\n")
        break
    
    
