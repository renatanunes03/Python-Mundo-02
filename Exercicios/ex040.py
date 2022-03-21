#Crie um programa que leia duas notas de um aluno e calcule sua
#média, mostrando uma mensagem no final, de acordo com a média atingida:
nota = float(input("Qual sua primeira nota? "))
nota2 = float(input("Qual sua segunda nota? "))
m = (nota + nota2) / 2
if m < 5.0:
    print(f"Média {m}.\nREPROVADO")
elif m > 5.0 and m < 6.9:
    print(f"Média {m}.\nRECUPERAÇAO")
else:
    print(f"Média {m}.\nAPROVADO")