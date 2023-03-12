arq_escrita = open('escrita.txt' ,'w', encoding='cp1252')
#'w' é para o modo de abertura do arquivo, no caso write

arq_escrita.write('Minha terra tem palmeiras\n')
arq_escrita.write('Onde canta o Sabiá')
arq_escrita.close()

#diferente do modo leitura em que o ponteiro arquivo indicava a posiçao do proximo caractere a ser lido, em escrita o ponteiro arquivo indica a proxima posiçao a ser escrita

#podemos resposicionar esse ponteiro utilizando o metodo seek
arquivo = open('restos.txt', 'w')
arquivo.write('0123456789')
arquivo.seek(0)
arquivo.write('abcd')
arquivo.close()

#caso quisessemos descartar o restante do arquivo e nao escrever por cima, bastaria utilizar o parametro truncate (bastaria adicionar o arquivo arquivo.truncante() entre as linhas 4 e 5 para ficar com resultado final abcd)
#truncate(0) apaga completamente o arquivo

# arquivo = open('restos.txt', 'w')
# arquivo.truncate(0)
# arquivo.close()

#modos de abertura de arquivo:
# 'r' 	Abre para leitura, falhando se o caminho não existir.
# 'w' 	Abre para escrita, apagando se o caminho existir e criando se não existir.
# 'a' 	Abre para escrita, começando do final se existir, criando se não existir.
# 'r+' 	Abre para leitura/escrita, falhando se o caminho não existir.
# 'w+' 	Abre para leitura/escrita, apagando se o caminho existir e criando se não existir.
# 'a+' 	Abre para leitura/escrita, começando do final se existir, criando se não existir.

#Os modos de leitura e de escrita são mutuamente excludentes. Em outras palavras, quando o segundo parâmetro de open é 'r', usar o método write gera um erro do tipo UnsupportedOperation. Abrir com modo 'w' só permite escrever, assim como modo 'r' só permite ler. Em ambos os casos, tentar realizar a outra operação gera um erro do tipo indicado. Isso previne erros de lógica porque o mais comum é abrir um arquivo só para ler ou só para escrever. Ou seja, para fazer os dois, é preciso deixar isso explícito.

# Porém, caso você queira realmente fazer isso, pode usar os modos de abertura 'r+' ou 'w+'. A diferença entre eles é que 'r+' irá falhar caso o arquivo indicado não exista, enquanto 'w+' irá apagá-lo caso ele exista. Em outras palavras, estes novos modos de abertura se comportam de forma similar aos já conhecidos 'r' e 'w', mas tornam possível leitura e escrita alternadas.

# Há ainda dois modos de abertura adicionais: 'a' e 'a+', onde a letra “a” vem do verbo inglês append, que significa acrescentar. Estes modos são similares a 'w' e 'w+', pois permitem escrever e criá-los no arquivo caso não existam. A diferença é que nesse modo os dados não são apagados do arquivo após a sua abertura e o ponteiro de arquivo é posicionado ao fim desse arquivo automaticamente. Estes modos são particularmente úteis para arquivos que crescem durante longos períodos de tempo antes de serem apagados, como registros de login ou históricos de atividades

