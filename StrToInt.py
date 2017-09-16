import glob
import optparse
import os
import pandas as pd

def str2int(_str, mapeamento):
	result = ''
	for c in str(_str):
		if c in mapeamento:
			result += str(mapeamento[c])
	return result

def main():

	parser = optparse.OptionParser()
	parser.add_option('-f', '--folder', type='string', dest='folderName', default='./', help='Pasta de arquivos .csv que serão divididos')
	parser.add_option('-e', '--encoding', type='string', dest='encoding', default='utf-8', help='Codificação dos arquivos .csv')
	parser.add_option('-s', '--sep', type='string', dest='separador', default=',', help='Separador dos arquivos .csv')

	(options, args) = parser.parse_args()

	mapeamento = {}

	n = 10
	for i in range(ord('a'), ord('z')+1):
		mapeamento[chr(i)] = str(n)
		n += 1

	for i in range(ord('A'), ord('Z')+1):
		mapeamento[chr(i)] = str(n)
		n += 1

	for i in range(ord('0'), ord('9')+1):
		mapeamento[chr(i)] = str(n)
		n += 1

	for fileName in glob.glob(options.folderName + '*.csv'):
		print("\t[->] Abrindo arquivo {}".format(fileName))
		data = pd.read_csv(fileName, sep=options.separador, header = 0, encoding=options.encoding, low_memory=False)
		for i, row in data.iterrows():
			print('Código Favorecido: {}'.format(data.loc[i,'Código Favorecido']))
			data.loc[i, 'Id Favorecido'] = str2int(data.loc[i,'Código Favorecido'], mapeamento)
			print('Substituído por: {}'.format(data.loc[i,'Id Favorecido']))
			print(70*"=")
			print('Código Ação: {}'.format(data.loc[i,'Código Ação']))
			data.loc[i,'Id Ação'] = str2int(data.loc[i,'Código Ação'], mapeamento)
			print('Substituído por: {}'.format(data.loc[i,'Id Ação']))

			print('ARQUIVO: {} -> {}% concluído...'.format(fileName, (i*100)/len(data)))
			os.system('clear')

		data.to_csv('Result/{}'.format(fileName), sep=',', encoding='utf-8', index=False)

if __name__ == '__main__':
	main()
