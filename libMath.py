import math

#conhecendo algumas constantes da biblioteca
print('pi: ', math.pi)
print('infinito positivo: ', math.inf)
print('infinito positivo', -math.inf)
print(math.inf > 100000000000)
print('Para saber se um elemento é infinito: ', math.isinf(100000000000))
print(math.isinf(math.inf))
print('Não é um numero (not a number): ', math.nan)
print('Para saber se um elemento é "nao numero" ou é numero: ', math.isnan(10))
print(math.isnan(math.nan),'\n') #math.nan nao é numerico

#metodos que fazem tratamento nos dados passados como argumento
print(math.ceil(9.24))  #ceil ou teto vai pegar sempre o maior valor inteiro
print(math.ceil(-9.40))
print(math.floor(9.24))  #contrario do ceil
print(math.floor(-9.40))
print(math.trunc(9.80)) #manter apenas a parte inteira, excluindo a parte decimal
print(math.trunc(-9.80))
print(math.fabs(2.3))   #usado para retornar o valor absoluto de um determinado numero passado como argumento
print(math.fabs(-2.3),'\n')  #tantos desvios positivos como negativos possuem o mesmo peso

#metodos para calculos
print(math.pow(10, 2))              
print(math.sqrt(100))
print(math.log(100, 10)) 
print(math.factorial(6))
print(math.isclose(10, 8, rel_tol=0.2)) #determinar se um numero está proximo do outro, rel_tol é em niveis percentuais, no caso 20% de proximidade (x-(x*0.2) <= y <= x+(x*0.2)) (8 está entre 8 e 12 entao = true)
print(math.isclose(10, 5, abs_tol=5))   #em vez de porcentagem, abs_tol é valor absoluto (|x-y| <= 5)
print(math.gcd(10, 15),'\n') #maior divisor comum

#Imagine que você decidiu comprar pizza para a família toda. Uma pizzaria oferece pizzas médias com raio de 30cm e grandes com raio de 45cm, ao preço de R$ 40,00 e R$ 50,00 cada uma, respectivamente. Você compraria duas pizzas médias ou uma grande?

area_pizza_media = math.pi * math.pow(30, 2) # piR²
area_pizza_grande = math.pi * math.pow(45, 2)

print(area_pizza_media * 2)
print(area_pizza_grande,'\n')
#a area da pizza grande é maior que a duas medias, logo se tratando de economia, melhor comprar uma grande apenas

#triângulo pitagórico
print(math.hypot(3, 4),'\n') #hipotenusa de um triangulo com catetos 3 e 4

#calcular a distancia entre dois pontos em um plano cartesiano
print(math.dist((1,3),(3,2)))

