import requests

def main():
	print('**********************************************')
	print('************ LOCALIZAR FUNCIONARIO ***********')
	print('**********************************************')
	print()

	localizador_funcionario = input('Qual o id/localizador do Funcionario que você quer encontrar: ')
	request = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(localizador_funcionario))
	address_data = request.json()

	if 'erro' not in address_data:
			print('==> DADOS DO FUNCIONARIO <==')
			
			print('CODIGO CONSULTADO: {}'.format(address_data['id']))
			print('NOME: {}'.format(address_data['name']))
			print('E-MAIL: {}'.format(address_data['email']))
			print('TELEFONE: {}'.format(address_data['phone']))
			
	else:
		print('{}:  - Sigla do estado  inválido.'.format(localizador_funcionario))

		print('---------------------------------')
		option = int(input('Deseja realizar uma nova consulta ?\n1. Sim\n2. Sair\n'))
		
		if option == 1:
			main()
		else:
			print('Saindo...')

if __name__ == '__main__':
	main()