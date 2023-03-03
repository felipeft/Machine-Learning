from datetime import date   #importando o tipo date do modulo datetime
hoje = date.today()
print(hoje) #será exibido por ano-mes-dia

#definindo as proprias datas:
dia_primeiro = date(2023, 1, 1) #devem ser passados nessa ordem (atributos year, month, day)
print(dia_primeiro)
print(dia_primeiro.year)
print(dia_primeiro.month)
print(dia_primeiro.day, '\n')

#O formato de exibição das datas estudado até agora é chamado ISO 8601 e é um padrão internacional de exibição de datas. Nesse padrão, os elementos de datas e horas são exibidos do mais significativo para o menos significativo. Por exemplo: ano-mês-dia e hora-minuto-segundo. Pode parecer curioso agora, mas é muito fácil de organizar arquivos e informações seguindo esse formato.O formato de exibição das datas estudado até agora é chamado ISO 8601 e é um padrão internacional de exibição de datas. Nesse padrão, os elementos de datas e horas são exibidos do mais significativo para o menos significativo. Por exemplo: ano-mês-dia e hora-minuto-segundo. Pode parecer curioso agora, mas é muito fácil de organizar arquivos e informações seguindo esse formato.

#intervalos de tempo:
#data de inicio do bbb
data_inicio = date(2021, 1, 25)
data_fim = date(2021, 5, 4)
print(f'O bbb 21 teve inicio em {data_inicio} e se encerrou no dia {data_fim}')
print(data_inicio < data_fim)
print(data_inicio > data_fim, '\n')   #datas iniciais sao menores que datas futuras

#vamos ver o tamanho de um certo periodo de tempo
diferença_dias = data_fim - data_inicio
print(diferença_dias)
print(type(diferença_dias), '\n') #ao subtrairmos duas datas, o resultado será um objeto do tipo timedelta e nao mais date
# A duração de dias entre uma data d1 e uma data d2 é: (d2 - d1) + 1, logo:
duracao = diferença_dias.days + 1   #O objeto timedelta possui um atributo days que é a quantidade de dias de diferença entre duas datas
print(f'A duração do bbb 21 foi de {duracao} dias', '\n')

#nao faz sentido somar duas datas, mas somar uma data a uma quantidade x de dias é cotidianamente usado:
from datetime import timedelta
hoje = date.today()
intervalo_dias = timedelta(days=28)
dia_futuro = hoje + intervalo_dias
print(f'Daqui a 28 dias será {dia_futuro}', '\n')

#ordenando uma lista de datas de eventos cronologicamente:
datas = [date(2016, 7, 6), date(2012, 10, 24), date(2020, 3, 19), date(2021, 8, 24), date(2021, 8, 12), date(2013, 5, 29), date(2018, 9, 2), date(2019, 1, 19), date(2012, 7, 2), date(2018, 9, 5)]

print(sorted(datas),'\n')

#agora ordenando somente por meses:
print(sorted(datas, key=lambda d: d.month),'\n')

#agora por dia e por mes ao mesmo tempo
print(sorted(datas, key=lambda d: (d.month, d.day)),'\n')

#armazenando tambem a hora
from datetime import datetime
hora_atual = datetime.now()
print(hora_atual)
#declarando uma variavel do tipo datetime:
d1 = datetime(2021, 5, 15, 18, 1, 59, 123456)
d2 = datetime(2021, 5, 15, 18, 1, 59)
d3 = datetime(2021, 5, 15, 18, 1)
d4 = datetime(2021, 5, 15, 18)
d5 = datetime(2021, 5, 15)  #ele apenas zera os outros campos que nao foram declarados
print(d1, d2, d3, d4, d5)
print(d1.year, d1.microsecond, '\n')

#weekday e isoweekday
print(dia_primeiro.weekday(), dia_primeiro.isoweekday(),'\n')
#basicamente 6 representa domingo em weekday e 7 em isoweekday

#suponha que você gosta muito de estudar Python e decidiu colocar seus conhecimentos de datas e horas em prática. Então, você vai criar um programa que toca um alarme às 20:30h e um depois de 30 segundos. Só que você lembrou que tem um compromisso às terças e quintas. Portanto, você deve mudar a hora do alarme para às 21:30h. Como criar esse programa? 

inicio = datetime(2021, 5, 24, 20, 30)  #data inicial da segunda feira com alarme as 20:30
#vamos preencher uma lista com os dias
semana = [inicio]
for i in range(1, 7):
    dia_seguinte = inicio + timedelta(days = i)
    semana.append(dia_seguinte)

print(semana)
print(len(semana),'\n')

#queremos mudar apenas o horario dos dias dias 25 e 27
#vamos fazer uma funçao para isso:
def muda_horario(dia):
    if dia.weekday() == 1 or dia.weekday() == 3:
        return dia.replace(hour=21)
    else:
        return dia  #sem alterar nada

semana_atualizada = list(map(muda_horario, semana)) #vai fazer isso para todos os elementos da lista semana (uma varredura em tudo)
print(semana_atualizada)










