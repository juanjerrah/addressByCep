import requests;
import json;

def searchAddress():
    while True:
        cep = str(input("Digite seu CEP: "))

        if(cep.find('-') == -1):
            cepFormat = f'{cep[:5]}-{cep[5:]}'
            
        request = requests.get(f'https://ws.apicep.com/cep/{cepFormat}.json')
        result = json.loads(request.content)

        if(result['status'] == 200):
            print(f'Cep {cepFormat} válido!')
            print('Endereço:', result['address'])
            print('Bairro: ', result['district'])
            print('Cidade: ', result['city'])
            print('Estado: ', result['state'])    
            opc = str(input('Deseja tentar um outro Cep? [S/N]: '))
            if(opc.upper() == 'S'):
                continue
            else:
                print('Até a próxima!')
                break
        else:
            print(f'Cep {cepFormat} inválido!')
            opc = str(input('Deseja tentar Novamente? [S/N]: '))
            if(opc.upper() == 'S'):
                continue
            else:
                print('Até a próxima!')
                break

print(searchAddress())

