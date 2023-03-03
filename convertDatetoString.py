from datetime import date

data_inicio = date(2021, 1, 5)
print(data_inicio.strftime("%d/%m/%Y")) #strftime converte uma data para uma string composta
print(data_inicio.strftime("%m %Y"))
print(data_inicio.strftime("%m - %d - %Y")) #padrao americano
# %A 	Nome do dia da semana completo 	Monday, Tuesday, …, Sunday
# %d 	Número do dia da semana 	01, 02, …, 31
# %b 	Nome do mês de forma abreviada 	Jan, Feb, Mar, ... , Dec
# %B 	Nome do mês completo 	January, February, …, December
# %m 	Número do mês 	01, 02, …, 12
# %y 	Dois últimos dígitos do ano 	01, 02, …, 99
# %Y 	Número do ano completo 	0001, 0002, …, 2021, ...,
# %H 	Número da hora 	01, 02, …, 24
# %M 	Número do minuto 	01, 02, …, 59
# %S 	Número do segundo 	01, 02, …, 59
# %j 	Número do dia do ano 	001, 002, …, 365, 366
# %W 	Número da semana do ano 	00, 01, …, 53

#escrevendo uma data por extenso
print(data_inicio.strftime("%m of %B of %Y is a %A"))
print(data_inicio.strftime("É o dia %j da semana %w do ano"))

#para nao exibirmos informaçoes em ingles e sim em pt-BR basta:
# import locale
# locale.setlocale(locale.LC_ALL, 'pt_BR')
# print(data_inicio.strftime("%m de %B de %Y é %A"))

#coletando dados de uma string digitada pelo usuario
from datetime import datetime
print("Digite sua data de nascimento: ")
data_nascimento = input()
data = datetime.strptime(data_nascimento, "%d/%m/%Y")
print(data)

data_string1 = "02 de April de 1900"
data1 = datetime.strptime(data_string1, "%d de %B de %Y")
print(data1)  #  1900-04-02 00:00:00
data_string2 = "O alarme toca monday às 20:30:05"
data2 = datetime.strptime(data_string2, "O alarme toca %A às %H:%M:%S")
print(data2)  # 1900-01-01 20:30:05
                                        
