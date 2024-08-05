# loop
while True:
    nome = input('Informe seu nome: ')
    peso = str(input('informe seu peso em kg: ')).replace(',', '.')
    altura = str(input('Informe sua altura em m: ')).replace(',', '.')

    # convesão
    peso = float(peso)
    altura = float(altura)

    # Cálculo do imc
    imc = peso / (altura ** 2)

    # mostrar o valor do imc
    print(f' IMC de {nome}: {imc:,.2f}.')

    # diagnostico do imc:
    if imc <= 16.9: 
        print(f'{nome} está muito abaix do peso.')
        print('Fvaor procurar um médico urgente!')
    elif imc < 18.5:
       print(f'{nome} está abaixo do peso. ')
    elif imc < 25:
        print(f'{nome} está no peso ideal.')
        print('Parabéns!')
    elif imc < 30:
        print(f'{nome} esta acima do peso ideal.')
    elif imc < 35:
        print(f'{nome} está obeso.')
    elif imc < 40:
        print(f'{nome} está com obesidade nivel 2.')
    else:
        print(f'{nome} está com obesidade mórbida.')
        print('Favor procurar um médico urgente.')
   
   # veificar se quer continuar
    continuar = input('Deseja continuar (s/n)?')

    if continuar == 's':
        continue
    else:
        break
    
   
   
   
   
   
   
   
   
   