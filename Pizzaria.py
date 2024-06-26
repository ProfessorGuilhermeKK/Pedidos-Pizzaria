#INICIO
subtotal= 0
acumulatexto= ''
print('Bem vindo a pizzaria do Guilherme Klein Klug')
while True:
    print('-'*20,'Cardápio','-'*20 )
    print('|Código| Descrição | Pizza Média | Pizza Grande |')
    print('|   21 | Napolitana| R$20,00     | R$26,00      |')
    print('|   22 | Margherita| R$20,00     | R$26,00      |')
    print('|   23 | Calabresa | R$25,00     | R$32,50      |')
    print('|   24 | Toscana   | R$30,00     | R$39,00      |')
    print('|   25 | Portuguesa| R$30,00     | R$39,00      |')
    print('-'*50)
    Código= input('Entre com o código do sabor desejado (21-25): ') #Codigo do pedido
    Tamanho= input('Entre com o Tamanho de pizza desejado (M/G): ') #Tamanho do pedido
    if Código== '21'and Tamanho== 'M':
        subtotal = subtotal + 20
        acumulatexto= acumulatexto+'Pizza Napolitana M R$20,00'
    elif Código == '21' and Tamanho == 'G':
        subtotal = subtotal + 26
        acumulatexto = acumulatexto + 'Pizza Napolitana G R$26,00'
    elif Código== '22'and Tamanho== 'M':
        subtotal = subtotal + 20
        acumulatexto = acumulatexto + 'Pizza Margherita M R$20,00'
    elif Código== '22'and Tamanho== 'G':
        subtotal = subtotal + 26
        acumulatexto = acumulatexto + 'Pizza Margherita G R$26,00'
    elif Código== '23'and Tamanho== 'M':
        subtotal = subtotal + 25
        acumulatexto = acumulatexto + 'Pizza Calabresa M R$25,00'
    elif Código== '23'and Tamanho== 'G':
        subtotal = subtotal + 32.5
        acumulatexto = acumulatexto + 'Pizza Calabresa G R$32,50'
    elif Código== '24'and Tamanho== 'M':
        subtotal = subtotal + 30
        acumulatexto = acumulatexto + 'Pizza Toscana M R$30,00'
    elif Código== '24'and Tamanho== 'G':
        subtotal = subtotal + 39
        acumulatexto = acumulatexto + 'Pizza Toscana G R$39,00'
    elif Código== '25'and Tamanho== 'M':
        subtotal = subtotal + 30
        acumulatexto = acumulatexto + 'Pizza Portuguesa M R$30,00'
    elif Código== '25'and Tamanho== 'G':
        subtotal = subtotal + 39
        acumulatexto = acumulatexto + 'Pizza Margherita G R$39,00'
    else:
        print('Opção Inválida')
        continue
    continuar = input('Deseja continuar ? (S/N)')
    if continuar == 'S':
        continue
    else:
        print('As pizzas encomendadas foram ' +acumulatexto)
        print('Valor final é: {:.2f}'.format(subtotal))
        break
#FIM 
