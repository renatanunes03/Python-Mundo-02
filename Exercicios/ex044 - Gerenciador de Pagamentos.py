print('{:^40}'.format('Exercício 44'))
print('Gerenciados de Pagamentos')
print('Elabore um programa que calcule o valor a ser pago por um produto,'
'considerando o seu preço normal e condição de pagamento:\n'
'Á vista dinheiro/cheque: 10% de desconto\n'
'Á vista no cartão: 5% de desconto\n'
'Em até 2x no cartão: preço normal\n'
'3x ou mais no cartão: 20% de juros')
while True:
    try:
        preco = float(input('Preço das compras: '))
        opcao = int(input('Formas de Pagamento: \n'
                          '[ 1 ] à vista dinheiro/cheque\n'
                          '[ 2 ] à vista cartão\n'
                          '[ 3 ] 2x no cartão\n'
                          '[ 4 ] 3x ou mais no cartão\n'
                          'Qual opção? '))
        if opcao == 1:
            total = preco - (preco * 0.10)
        elif opcao == 2:
            total = preco - (preco * 0.05)
        elif opcao == 3:
            preco = total
            print(f'A compra sera parcela em 2x de R${total / 2:,.2f} SEM JUROS.')
        elif opcao == 4:
            parcelas = int(input('Em quantas parcelas? '))
            total = preco + (preco * 0.20)
            print(f'Sua compra será parcelada em {parcelas}x de R${total / parcelas:,.2f} COM JUROS.')
        print(
            f'Sua compra de R${preco:,.2f} vai lhe custar R${total:,.2f}.')
    except:
        print('Digite campos válidos!')