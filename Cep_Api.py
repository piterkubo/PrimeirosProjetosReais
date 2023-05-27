import requests

print('############')
print("Consulta CEP")
print('############')
print()


def main():
    cep = input('Digite o Cep para consulta: ')

    if len(cep) != 8:
        print('Quantidade de digitos invalidos')

    retorne_cep = requests.get(f'https://viacep.com.br/ws/{cep}/json/')

    retornou = retorne_cep.json()

    if 'erro' not in retornou:
        print('#### CEP econtrado ####')
        print(retornou['cep'], retornou['logradouro'], retornou['complemento'], retornou['bairro'],
              retornou['localidade'])

    else:
        print(f'{cep} invalido')

    print('Deseja realizar uma nova consulta? ')
    opcao = int(input('Deseja continuar a pesquisa ? Digite 1 para sim ou 2 para não: '))

    if opcao == 1:
        main()

    else:
        exit()


main()

