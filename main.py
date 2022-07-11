import random
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

year = -4000
christ = "a.C."

while year <= -3000:
    print("Você está no turno {} {}".format(year, christ))
    print("Você tem as seguintes cidades: ")
    print("Voce tem as seguintes unidades: ")


    year = year + 100 # Mostra o turno atual e soma 1

    pesquisa = 0 #indica qual pesquisa é
    construcao = 0 #indica qual construção é

    tempo_pesquisa = 0 #quantos turnos demora pra terminar a pesquisa
    tempo_construcao = 0 #quantos turnos demora a construção
    tempo_acao = 0 #quantos turnos demora a ação

    construcoes_feitas = []
    tecnologias_obtidas = []
    unidades_obtidas = []

    opcoes_tecnologia = []
    opcoes_construcao = []

     #recursos
    ouro = 0
    populacao = 0
    felicidade = 0
    ciencia = 0
    poder = 0

    # apresentar uma situação aleatória para o jogador lidar
    numero = random.randint(0, 10)
    civilizacao = "RANDOM"

    if numero == 1:
        print("Uma tribo bárbara foi avistada próximo ao seu reino!")
        print("O que você quer fazer???")
        quero_fazer = int(input("1 - Atacaaaaaar 2 - Se defender 3 - Vou tentar um contato diplomático"))
    elif numero == 2:
        print("Um pequeno exército bárbaro está invadindo sua cidade")
        print("O que você quer fazer???")
        quero_fazer = int(input("1 - ATAQUEEEEEE 2 - QUEM TEM UMA ESPADA QUE DEFENDA A CIDADE  3 - ABANDONEM A CIDADE"))
    elif numero == 3:
        print("UMA GRANDE HORDA BÁRBARA ESTÁ ATACANDO SUA CAPITAL")
        print("O que você quer fazer???")
        quero_fazer = int(input("1 - PRA CIMA DELEEEEES 2 - TODAS AS CRIANÇAS E MULHERES DEFENDAM A CIDADE 3 - EVACUAR"))
    elif numero == 4:
        print("Você encontrou um outro povo!")
        print("O que você quer fazer???")
        quero_fazer = int(input("1 - Mando uma comissão diplomática 2 - Declarar guerra 3 - Ignorar"))
    elif numero == 5:
        print("O povo {} deseja falar com você".format(civilizacao))
        print("O que você quer fazer???")
        quero_fazer = int(input("1 - Receber a comissão deles 2 - Matar o diplomata deles 3 - Rejeitar"))
    elif numero == 6:
        print("O povo {} te declarou guerra!!!".format(civilizacao))
        print("O que você quer fazer???")
        quero_fazer = int(input("1 - TERÃO SANGUE 2 - FORTIFICAR DEFESAS 3 - ATACAR CIDADE DELES!!!!"))
    elif numero == 7:
        print("Um vulcão nas proximidades entrou em erupção!!!")
        print("O que você quer fazer???")
        quero_fazer = int(input("1 - Evacuar cidadeeeeeeee 2 - Ninguem sai, juntos somos mais"))
    elif numero == 8:
        print("Uma seca sem precedentes está assolando a região!!")
        print("O que você quer fazer???")
        quero_fazer = int(input("1 - Se lamentar 2 - Chorar"))
    elif numero == 9:
        print("O tempo favorável tem feito as colheitas irem bem")
        print("O que você quer fazer???")
        quero_fazer = int(input("1 - Graças a Deus 2 - Que bom!!!"))
    elif numero == 10:
        print("Uma praga está tomando conta do seu reino")
        print("O que você quer fazer???")
        quero_fazer = int(input("1 - Decretar lockdown 2 - O comércio é mais importante!!!"))



    # o que o jogador quer fazer quanto a isso? 1 - opção agressiva, 2 - diplomática/pacífica, 3 - neutra
    

    # checar o que o jogador quer fazer

    #quanto a pesquisa
    if tempo_pesquisa == 0:
        print("Escolha a próxima pesquisa: ")
        for item in opcoes_tecnologia:
            print("{} - {}".format(item, tempo_pesquisa))
    else:
        print("Pesquisa em andamento: {}, {} turnos restantes.".format(tecnologias_obtidas, tempo_pesquisa))

    #quanto ao que construir
    if tempo_construcao == 0:
        print("O que você quer construir? ")
        for item in opcoes_construcao:
            print("{} - {}".format(item, tempo_construcao))
    else:
        print("Construção em andamento: {}, {} turnos restantes.".format(construcoes_feitas, tempo_construcao))

    #quanto ao movimento



    
