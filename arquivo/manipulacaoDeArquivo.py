#Arquivos de texto são considerados um dos arquivos mais simples que existem, pois utilizam bytes consecutivos para representar caracteres. Assim, ao ler um arquivo de texto, você estará essencialmente lendo strings.

arq = open('poesia1.txt')   #arq recebe o caminho de um arquivo como argumento, retorna um objeto que nos permite fazere a manipulaçao, dentre elas a leitura
texto = arq.read()
print(texto,'\n')
arq.close() #fechar arquivos é fundamental, ja que arquivos abertos que não serão mais utilizados podem causar erros de lógica e esgotar os recursos

#leitura linha a linha:
arq = open('poesia1.txt')
linha1 = arq.readline()
linha2 = arq.readline()
#o objeto readline tem uma especie de memória, cada vez que le uma linha ele avança para outra
print('linha 1:', linha1)
print('linha 2:', linha1, '\n')

#se tentassemos ler com read novamente, teriamos impresso na tela o resto das linhas, porem se tentassemos denovo, iriamos ter uma string vazia indicando que o final do arquivo foi atingido
#por esse motivo, uma forma comum de ler um arquivo de texto é utilizando um laço while


#agora lendo caracteres:
arq = open('poesia1.txt')
texto1 = arq.read(5)
arq.read(1) #o caractere seguinte (espaço em branco) é descartado
texto2 = arq.read(5)
print(texto1)
print(texto2)

# ponteiro de arquivo é um número inteiro, não negativo, análogo ao índice em uma lista ou string, que corresponde à próxima posição do arquivo que será lido, em relação ao início do arquivo. O valor do ponteiro de arquivo pode ser recuperado usando o método tell, sem parâmetros. Após as operações de leitura no programa acima, 11 caracteres foram lidos, então arq.tell() retornaria 11.



