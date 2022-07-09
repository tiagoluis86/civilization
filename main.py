import random

import facts
import base
import buildings
import techs
import units

# menu principal

print("TIAGOs CIVILIZATION")
print("Choose your civ: ")
civ_option = int(input("1 - Babilônia (Astronomia), 2 - Roma (Provincias), 3 - Egito (Religião)"))

if civ_option == 1:
    civ_name = "Babilônia"
    civ_lider = "Nabucodonosor"
elif civ_option == 2:
    civ_name = "Roma"
    civ_lider = "Júlio César"
elif civ_option == 3:
    civ_name = "Egito"
    civ_lider = "Cleópatra"    

#Start game

print("Começa uma nova era pra você, {}, líder da {}".format(civ_lider, civ_name))
print("Aperte '0' a qualquer momento para abrir o MENU")


turno = 1

while turno <= 100:
    print("Você está no turno {}".format(turno))
    print("Você tem as seguintes cidades: ")
    print("Voce tem as seguintes unidades: ")

    turno = turno + 1 # Mostra o turno atual e soma 1

    pesquisa = 0 #indica qual pesquisa é
    construcao = 0 #indica qual construção é

    tempo_pesquisa = 0 #quantos turnos demora pra terminar a pesquisa
    tempo_construcao = 0 #quantos turnos demora a construção
    tempo_acao = 0 #quantos turnos demora a ação

    lista_construcao = []
    lista_tecnologia = []

    # apresentar uma situação aleatória para o jogador lidar
    acontecimento = random.randint(0, 25)
    print("Aconteceu algo número {}".format(acontecimento))

    # o que o jogador quer fazer quanto a isso?
    

    # checar o que o jogador quer fazer

    #quanto a pesquisa
    if tempo_pesquisa == 0:
        print("Escolha a próxima pesquisa: ")
        for item in lista_tecnologia:
            print("{} - {}".format(item, tempo_pesquisa))
    else:
        print("Pesquisa em andamento: {}, {} turnos restantes.".format(lista_tecnologia, tempo_pesquisa))

    #quanto ao que construir
    if tempo_construcao == 0:
        print("O que você quer construir? ")
        for item in lista_construcao:
            print("{} - {}".format(item, tempo_construcao))
    else:
        print("Construção em andamento: {}, {} turnos restantes.".format(lista_construcao, tempo_construcao))

    #quanto ao movimento



    
