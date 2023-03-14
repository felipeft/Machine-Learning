#vamos lidar com dados invalidos em um array
import numpy as np
import numpy.ma as ma   #esse modulo permite criar arrays mascarados

dados_invalidos = np.array([1, 2, 3, np.nan, 5])
#vamos mascarar somente o valor nan

dados_mascarados = ma.masked_array(dados_invalidos, mask=[False, False, False, True, False])
print(dados_mascarados,'\n')

#mostrando a pratica disso:
print(dados_invalidos.mean())
print(dados_mascarados.mean())
print(np.ma.median(dados_mascarados))   #mediana
print(dados_invalidos.min())
print(dados_mascarados.min())
print(dados_invalidos.argmin()) #vai pegar o indice do np.nan
print(dados_mascarados.argmin(),'\n')

#identificado o(s) elemento(s) sem saber o idice
from random import sample
array_invalido = np.arange(20)
indices = sample(array_invalido.data, k=5)  #vai selecionar 5 indices aleatorios do array_invalido
array_invalido[indices] = -999  #os valores do vetor foram trocados por -999 (este é o valor invalido)
print(array_invalido,'\n')

#agora vamos mascarar esse array
array_mascarado = np.ma.masked_where(array_invalido == -999, array_invalido)    #o segundo argumento é o array que queremos mascarar
print(array_mascarado,'\n')

#o mesmo se aplica para o caso de queremos pegar todos os valores menores que zero por exemplo
array_mascarado2 = np.ma.masked_where(array_invalido < 0, array_invalido)
print(array_mascarado2,'\n')

#preenchendo os valores invalidos
media = array_mascarado.mean()
print(media) 
array_preenchido = array_mascarado.filled(media)    #o argumento é o valor que será utilizado para preencher
print(array_preenchido)