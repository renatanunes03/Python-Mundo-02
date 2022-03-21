#Faça um programa que leia o ano de nascimento de um jovem e informe,
#de acordo com sua idade:

#Se ele ainda vai se alistar ao serviços militar.
#Se é a hora de se alistar
#Se já passou do tempo do alistamento.

#Seu programa também deverá mostrar quanto tempo falta ou quanto
#tempo passou do prazo
i = int(input("Qual sua idade? "))
if i < 18:
    print(f"Ainda não chegou sua hora, restam {18-i} anos para o alistamento")
elif i == 18:
    print("Está na hora de se alistar!")
else:
    print(f"Você tem {i}, já passou {i-18} anos da idade de alistamento obrigatório. Você se alistou?")