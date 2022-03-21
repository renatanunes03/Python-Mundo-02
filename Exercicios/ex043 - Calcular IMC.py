print('{:^40}'.format('Exercício 43'))
print('Desenvolva uma lógica que leia o peso e a altura de uma pessoa,\n'
'calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:'
'Abaixo de 18.5: Abaixo do Peso\n'
'Entre 18.5 e 25: Peso ideial\n'
'25 até 30: Sobrepeso\n'
'30 até 40: Obesidade\n'
'Acima de 40: Obesidade Mórbida\n')
while True:
    try:
        p = float(input('Qual seu peso? '))
        a = float(input('Qual sua altura? '))
        imc = p / (a ** 2)
        print(f'Seu IMC é de {imc:,.1f}. ', end='')
        if imc < 18.5:
            print('Você está abaixo do peso!')
        elif imc >= 18.5 and imc <= 25:
            print('Seu peso está ideal!')
        elif imc >= 25 and imc < 30:
            print('Você está com sobrepeso!')
        elif imc 30 >= and imc < 40:
            print('Você está com obesidade!')
        elif imc >= 40:
            print('Cudiade! Obesidade Mórbida!')
    except:
        print('Digite um número válido!')