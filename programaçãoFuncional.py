
def filtrar(lista, limiar):
    nova_lista = []
    for elemento in lista: 
        if elemento > limiar:
            nova_lista.append(elemento)
    return nova_lista
#temos uma função pura pois nenhuma variavel externa é modificada

a = 2
def soma(b):
    b = b + a
    return b
print(soma(1))
#a funçao é impura pois depende de valores externos a função para seu funcionamento


class A:
    atributo = 0
    def mudar_valor(self, x):
        self.atributo = x

objeto = A()
objeto.mudar_valor(5)
print(objeto.atributo)
#O metódo mudar_valor é impuro pois modifica uma variavel que nao pertence ao escopo da funçao (atributo)

#convertendo a funçao soma para uma função pura:

def soma(a, b):
    b = b + a
    return b

print(soma(2, 1))

#uma variavel tambem pode receber uma funçao:
def soma(a, b):
    return a + b

f = soma
print(type(f))