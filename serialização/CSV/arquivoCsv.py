# Considere a seguinte situação: você precisa obter informações dentro e fora de seus programas através de outros meios possíveis, além do teclado e do console. Trocar informações por arquivos de texto é uma maneira comum de compartilhar informações entre programas. Um dos formatos mais populares para a troca de dados é o formato Comma Separated Values (CSV), podendo ser traduzido para “valores separados por vírgula”. Saiba que a grande vantagem de um arquivo CSV é o fato de ele possibilitar a importação e a exportação de arquivos com grandes quantidades de dados de uma linguagem que vários aplicativos podem ler.

# Um arquivo CSV é um tipo de arquivo de texto simples que usa estruturação específica para organizar dados tabulares. Por ser um arquivo de texto simples, ele pode conter apenas dados de texto reais — em outras palavras, caracteres ASCII ou Unicode imprimíveis, certo? Normalmente, os arquivos CSV usam uma vírgula para separar cada valor específico de dados, sem espaço entre eles.

import csv

with open('aniversarios_funcionarios.txt', encoding='utf8') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv, delimiter=',') #lista com os arquivos do txt
    print(leitor_csv)
    for linha in leitor_csv:
        print(linha)

print()
#agora lendo os dados em um dicionario, para separar tudo e nao ter que entender a logica por tras da lista

with open('aniversarios_funcionarios.txt', encoding='utf8') as arquivo_csv:
    leitor_csv = csv.DictReader(arquivo_csv, delimiter=',')
    print(type(leitor_csv))
    for linha in leitor_csv:
        print(linha)

print()
#escrevendo um arquivo csv novo:
with open('aniversarios_funcionarios_novo.txt', encoding='utf8', mode='w', newline='') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv, delimiter=';')
    escritor_csv.writerow(['nome', 'departamento', 'mês de aniversário'])
    escritor_csv.writerow(['Pedro Lima', 'RH', 'Novembro'])
    escritor_csv.writerow(['Gabriela Silva', 'TI', 'Março'])

print()
#fazendo o mesmo para dicionarios
with open('aniversarios_funcionarios_novo_dict.txt', encoding='utf8', mode='w', newline='') as arquivo_csv:
    fieldnames = ['nome', 'departamento', 'mês de aniversário'] #uma lista para delimitar os campos de nomes que será passada como argumento no escritor de dicionarios
    escritor_csv = csv.DictWriter(arquivo_csv, delimiter=';', fieldnames=fieldnames)
    escritor_csv.writeheader()  #pula a primeira linha do arquivo ja que essa ha o nome das colunas definidas na linha anterior
    escritor_csv.writerow({'nome': 'Pedro Lima', 'departamento': 'RH', 'mês de aniversário': 'Novembro'})
    escritor_csv.writerow({'nome': 'Gabriela Silva', 'departamento': 'TI', 'mês de aniversário': 'Março'})
    escritor_csv.writerow({'mês de aniversário': 'Agosto', 'nome': 'Marcelo Oliveira'})
                                        

