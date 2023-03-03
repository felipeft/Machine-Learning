from datetime import datetime, timedelta
hoje = datetime.today()
intervalo_dias = timedelta(weeks=12)    #o tempo de intervalo entre 1 dose e outra é de 12 semanas
#basicamente uma variavel de tempo para armazenar o intervalo apenas
dia_futuro =  hoje + intervalo_dias
diff = dia_futuro - hoje    
days = diff.days    #basicamente, convertendo um objeto do tipo 'timedelta' para 'int'
months , days = days // 30, days % 30   #meses é dias / por 30, e dias é o resto dessa divisão
print('Desde {}, Passaram {} meses e {} dias'.format(dia_futuro, months, days))




