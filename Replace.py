import os
import glob
import numpy as np
import pandas as pd

seila = 'Informações protegidas por sigilo, nos termos da legislação, para garantia da segurança da sociedade e do Estado'

for fileName in glob.glob('*.csv'):
	print(" [->] Abrindo {}".format(fileName))
	dataFile = '00/' + fileName[4:6] + '/' + fileName[0:4]
	data = pd.read_csv(fileName, header=0, encoding='utf8', delimiter=',')
	data['Código Favorecido'] = data['Código Favorecido'].replace(seila, -1)
	data['Nome Favorecido'] = data['Nome Favorecido'].replace(seila, 'INFORMAÇÃO SIGILOSA')
	data['Número Documento'] = data['Número Documento'].replace(seila, -1)
	data['Gestão Pagamento'] = data['Gestão Pagamento'].replace(seila, -1)
	data['Data Pagamento'] = data['Data Pagamento'].replace(seila, dataFile)
	data.to_csv('Saida/' + fileName, sep='\t', encoding='utf8')
	print(" [->] Concluído {}".format(fileName))
