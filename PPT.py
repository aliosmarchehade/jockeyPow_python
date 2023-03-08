import random

escolhas = ["pedra", "papel", "tesoura"]

computador = random.choice(escolhas)
jogador = None

while jogador not in escolhas:
    jogador = input("escolha Pedra, Papel ou Tesoura: ").lower()

    if jogador == computador:
        print("Computador: ", computador)
        print("Jogador: ", jogador)
        print("EMPATE!!")
    elif jogador == "pedra":
        if computador == "papel":
            print("Computador: ", computador)
            print("Jogador: ", jogador)
            print("VOCÊ PERDEU!!")
        if computador == "tesoura":
            print("Computador: ", computador)
            print("Jogador: ", jogador)
            print("VOCÊ VENCEU!!")
            
    elif jogador == "tesoura":
        if computador == "pedra":
            print("Computador: ", computador)
            print("Jogador: ", jogador)
            print("VOCÊ PERDEU!!")
        if computador == "papel":
            print("Computador: ", computador)
            print("Jogador: ", jogador)
            print("VOCÊ VENCEU!!")
            
    elif jogador == "papel":
        if computador == "tesoura":
            print("Computador: ", computador)
            print("Jogador: ", jogador)
            print("VOCÊ PERDEU!!")
        if computador == "pedra":
            print("Computador: ", computador)
            print("Jogador: ", jogador)
            print("VOCÊ VENCEU!!")

       
    