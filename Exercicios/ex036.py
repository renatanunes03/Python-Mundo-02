print('{:^40}'.format('Exercício 036'))
#Escreva um programa para aprovar um empréstimo bancário para
#a compra de uma casa. O programa vai perguntar o valor da casa, o salário
# do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder
#30% do salário ou entâo o empréstimo será negado.

imovel = int(input("Qual o valor total do imóvel? R$"))
renda = float(input("Qual seu salário líquido? R$"))
prazo = int(input("Quantos anos de financiamento? ")) * 12
anos = prazo / 12
parcela = imovel / prazo
trinta = renda * 30 / 100
print(f"Pra comprar uma casa no valor de {imovel:.2f} mil em {prazo} meses ({anos:.0f} anos) a prestação será"
      f" de {parcela:.2f}.")
if parcela <= trinta:
    print("Seu emprestimo foi aprovado!")
else:
    print("Seu emprestimo foi negado!")