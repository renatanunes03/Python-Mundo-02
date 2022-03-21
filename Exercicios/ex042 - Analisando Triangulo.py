print('{:^40}'.format('Exercício 42'))
print('Analisando Triângulo')
print('Refaço o DESAFIO 035 dos triângulos, acrescentando o recurso\n'
    'de mostrar que tipo de triângulo será formado:\n'

    'EQUILÁTERO: todos os lados iguais\n'
    'Isósceles: dois lados iguais\n'
    'Escaleno: todos os lados diferentes\n')
while True:
    try:
        a = float(input('Primeiro segmento: '))
        b = float(input('Segundo segmento: '))
        c = float(input('Terceiro segmento: '))
        if a < b + c and b < a + c and c < a + b:
            print('Os segmentos acima podem formar um triângulo ', end='')
            if a == b == c:
                print('EQUILATERO!')
            elif a == b or b == c or c == a:
                print('ISÓSCELES!')
            elif a != b != c != a:
                print('ESCALENO!')
        else:
            print('Não temos um triângulo.')
    except:
        print('Digite um numero válido!')
