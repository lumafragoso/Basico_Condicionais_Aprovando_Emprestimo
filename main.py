valor = float(input('Valor da casa: R$ '))
salario = float(input('Salário do comprador: R$ '))
financiamento = int(input('Quantos anos de financiamento? '))
parcela = valor/(financiamento*12)
if 0.3*salario > parcela:
    print('Valor máximo para a prestação (margem de 20%) é de R${:.2f}'.format(0.3*salario))
    print(('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}.').format(valor, financiamento, parcela))
    print('Empréstimo pode ser CONCEDIDO!')
elif 0.3*salario < parcela:
    print('O valor máximo para prestação (margem de 30%) é R${:.2f}'.format(0.3*salario))
    print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(valor, financiamento, parcela))
    print('Empréstimo NEGADO!') 
