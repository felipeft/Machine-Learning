import re

print('\tTabulação')
print(r'\tTabulação', '\n')

print('#search:')
palavra = r'otorrinolaringologista 816'
print(re.search('rino', palavra))   #encontramos a substring 'rino' em palavra
print(re.search('rino', palavra).group(0),'\n')

#extraindo dados de uma string
palavra = r"Laura Maria da Silva\n(46) 93201-6392\n(89) 42010-7411\n(61) 47405-4895\nRua José Geraldo\nlauramaria@hotmail.com\nLe@d Dell Technologies"

print(re.search(r'[0-9][0-9]', palavra))    #retorna o primeiro objeto que contem dois numeros entre 0 e 9, no caso o ddd 46

print(re.findall(r'[0-9][0-9]', palavra))   #retornará uma lista com todas as correspondencias encontradas

print(re.findall(r'\W[0-9][0-9]\W', palavra),'\n')   #o \W serve para encontrar apenas caracteres nao verbais, ou seja, vai pegar os () dos ddd's

#quantificadores
print(re.findall(r'\W[0-9][0-9]\W', palavra))
print(re.findall(r'\W[0-9]{2}\W', palavra))   #o quantificador {} explicita que queremos somente duas ocorrencias dessa expressao ([0-9])
print(re.findall(r'\W\d{2}\W', palavra),'\n')   #\d é equivalente a [0-9]

#buscando apenas o telefone
print(re.findall(r'\W\d{5}\W\d{4}', palavra))
print(re.findall(r'\W\d{2}\W\s\d{5}\W\d{4}', palavra),'\n')  #\s é para unir as expressoes e procurar uma ocorrencia só

#vamos supor que um ddd foi retirado da string, aqui vai uma maneira de juntar as strings mesmo sendo diferentes:
palavra = r"Laura Maria da Silva\n(46) 93201-6392\n42010-7411\n(61) 47405-4895\nRua José Geraldo\nlauramaria@hotmail.com\nLe@d Dell Technologies"   #string com um ddd faltando
print(re.findall(r'\d{5}\W\d{4}', palavra)) #sem ddd
print(re.findall(r'\W\d{2}\W\s\d{5}\W\d{4}', palavra)) #com ddd
#basta agora combinar as expressoes com 'ou' |
print(re.findall(r'\W\d{2}\W\s\d{5}\W\d{4}|\d{5}\W\d{4}', palavra))

#exercicio de extrair emails de um site:
emails = r'contato@dellead.com, franciscojose@yahoo.com.br, ana.julia@universidade.edu, francisca-321-aline@meu-trabalho.net, Le@d Dell Technologies'
#primeiro, vamos buscar expressoes até o @
print(re.findall(r'[a-zA-Z0-9_.-]+@', emails))
#segundo, expressoes após o @
print(re.findall(r'@+[a-zA-Z0-9_.-]+\.', emails))   #\. é para qualquer caractere menos nova linha
print(re.findall(r'@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', emails))    #para buscar caracteres .com, .net e etc
print('Juntando todas as expressoes: ')
print(re.findall(r'[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', emails))



