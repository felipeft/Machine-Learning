verso = 'Minha terra tem palmeiras'
verso_bytes = verso.encode('ascii')
print(verso_bytes)  #é uma string de bytes e nao de caracteres do tipo str, logo se fizermos verso_byte[0] teremos como resposta 77

#utilizando outras codificaçoes

verso = 'Onde canta o sabiá'

print(verso.encode('cp1252'))
print(verso.encode('utf8'))

#apesar de existirem muitas codificações de caracteres, apenas duas são diferentes: a 'com sinal' e 'sem sinal'

