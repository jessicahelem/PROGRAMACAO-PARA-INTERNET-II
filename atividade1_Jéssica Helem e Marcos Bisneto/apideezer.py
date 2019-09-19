# coding: utf-8
import requests



localizador_album = input('Qual o id/localizador do album que você quer encontrar: ')
response = requests.get("https://api.deezer.com/album/302127".format(localizador_album))
address_data = response.json()

#playlist
#print(" Titulo: %s \n duration: %s" %(response['data'][0]['title'], response['data'][0]['duration']))

if 'erro' not in address_data:
    print('==> DADOS DO ALBUM <==')

    print(" Titulo: {}".format(address_data['title']))
    print("Duração:{}".format(address_data['duration']))
    print("Link:{}".format(address_data["link"]))

else:
    print('{}:  - Sigla do estado  inválido.'.format(localizador_album))

