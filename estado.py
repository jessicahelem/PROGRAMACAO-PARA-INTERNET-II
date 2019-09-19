import requests

def main():
	print('********************************************************')
	print('***** QUANTIDADE DE LICITAÇÕES MENSAL POR ESTADO *******')
	print('********************************************************')

	print("AC; AL; AP; AM; BA; CE; DF; ES; GO; MA; MT; MS; MG; PA; PB; PR; PE; PI; RR; RO; RJ; RN; RS;SC; SP; SE; TO.")

	estado = input('DIGITE A SIGLA DO ESTADO (Ex. Piauí = PI) >>> ')

	if len(estado) != 2:
		print('Sigla inválida, a sigla contem apenas 2 digitos, Ex. PI!')
		print('{}: Sigla inválida.'.format(estado))
		print('---------------------------------')
		option = int(input('Deseja realizar uma nova consulta ?\n1. Sim\n2. Sair\n'))	
		if option == 1:
			main()
	else:			
		request = requests.get('https://alertalicitacao.com.br/api/v1/licitacoesAbertas/?uf={}'.format(estado))
		address_data = request.json()

		if 'erro' not in address_data:
				print()
				print('>>TOTAL DE LICITAÇÕES ENCONTRADAS: {}'.format(address_data['totalLicitacoes']))
				print('---------------------------------')
				option = int(input('Deseja realizar uma nova consulta ?\n1. Sim\n2. Sair\n'))
				
				if option == 1:
					main()
				
				else:
					print('Saindo...')

if __name__ == '__main__':
	main()