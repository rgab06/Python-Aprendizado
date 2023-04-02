arquivo = open('arqText.txt', 'w')

arquivo.write('Curso Python\n')
arquivo.write('Ryan Gabriel Andradede de Jesus\n')
arquivo.write('21/12/2006')
arquivo.close()

#leitura do arquivo texto

leitura=open('arqText.txt', 'r')
print(leitura.read())
leitura.close()

