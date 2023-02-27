#Você trabalha para a Netflix e quer analisar quantos filmes ruins, médios e bons há no catálogo. Porém, o seu chefe te deu somente uma média da avaliação dos usuários
#É possível classificar filmes da seguinte maneira: filmes com nota menor que 5 são classificados como ruim; entre 5 e 7 são classificados como médio; e filmes com nota acima de 7 são classificados como bons.

def categoria(nota):
    if nota < 5.0:
        return 'ruim'
    elif 5.0 <= nota <= 7.0:
        return 'médio'
    else:
        return 'bom'             

notas = [9.87, 3.15, 7.53, 6.17, 0.53, 9.55, 7.7, 1.88, 7.9, 6.01]
classificação = list(map(categoria, notas))
print(classificação)                           

#agora dividindo os resultados em grupos:
filmes_ruins = list(filter(lambda x: x == 'ruim', classificação))   #se x for ruim, fica nessa lista
filmes_medios = list(filter(lambda x:x == 'médio', classificação))
filmes_bons = list(filter(lambda x:x == 'bom', classificação))

print(filmes_ruins)
print(filmes_medios)
print(filmes_bons)

#contando o total de filmes de acordo com suas devidas classificações:
print('temos um total de {}, Sendo {} considerados ruins, {} filmes médios e {} filmes bons'.format(len(notas), len(filmes_ruins), len(filmes_medios), len(filmes_bons)))


#a função all recebe uma estrutura de dados como argumento e retorna verdadeiro se todos os valores são verdadeiros
#a função any recebe uma estrutura de dados como argumento e retorna verdadeiro se, pelo menos, um elemento da lista for verdadeiro

#dado uma nova lista de filmes, desejamos saber se existe algum ruim e tambem saber se todas as notas sao boas
novas_categorias = ['bom', 'bom', 'bom', 'ruim', 'bom']
filmes_ruins_booleano = list(map(lambda x: x == 'ruim', novas_categorias)) #ve o tipo dos filmes e retorna uma lista [true, false, true...]
print(any(filmes_ruins_booleano))   #se houver um ruim, vai cair aqui

filmes_bons_booleano = list(map(lambda x: x == 'bom', novas_categorias))
print(all(filmes_bons_booleano))    #nem todos os filmes serao bons
