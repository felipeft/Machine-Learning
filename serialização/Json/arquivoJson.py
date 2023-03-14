#Desde a sua criação, JavaScript Object Notation (JSON) tornou-se rapidamente o padrão de fato para a troca de informações, por exemplo, para coletar informações através da internet ou armazenar seus dados em um banco de dados de documentos.

import json
arquivo_json = open('exemplo_json.txt', encoding='utf8')
pessoa = json.load(arquivo_json)
arquivo_json.close()
print(type(pessoa))
print(pessoa,'\n')

#agora vamos converter o dicionario pessoa em um objeto json:
#vamos serializar o objeto novamente
json.dumps(pessoa)
json.dumps(pessoa, ensure_ascii=False)  #para nao ter carcteres no padrao ascii

print()
#agora serialiazando em um objeto com extensao .json:

#Imagine que você precisa fazer um algoritmo de Machine Learning que recomende filmes. Para isso, você primeiro precisa dos dados do filme e serializá-lo em alguma estrutura de dados. Aqui, será usado o filme Toy Story como exemplo

filme = {}
filme['Nome'] = 'Toy Story'
filme['Direção'] = 'John Lasseter'
filme['Produção executiva'] = ['Edwin Catmull','Steve Jobs']
filme['Gênero'] = ['animação','aventura','comédia']
filme['Produtora'] = ['Walt Disney Pictures','Pixar Animation Studios']
filme['Lançamento'] = [{'País': 'Estados Unidos','Data': '22/11/1995'},
    {'País': 'Brasil','Data': '22/12/1995'},
    {'País': 'Portugal','Data': '29/03/1996'}]
filme['Orçamento (US$)'] = 30000000
filme['Receita (US$)'] = 406594102

#vai serializar o dicionario filme em arquivo .txt no padrao json
arquivo_json = open('exemplo_2_json.txt', mode='w', encoding='utf8')
json.dump(filme, arquivo_json, ensure_ascii=False)
arquivo_json.close()

#o mesmo so que em arquivo .json:
arquivo_json = open('exemplo_2_json.json', mode='w', encoding='utf8')
json.dump(filme, arquivo_json, ensure_ascii=False)
arquivo_json.close()


