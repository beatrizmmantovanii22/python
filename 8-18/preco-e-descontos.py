
preco = 100
desconto = 0.1

def calculo_desconto(preco:float, desconto:float)->float:
    aux = preco*desconto
    return preco - aux

print(f'O preço de R${preco} com o desconto de {desconto*100}%, cai pra R${calculo_desconto(preco, desconto)}')


#desafio
precos = [100.0, 250.0, 39.90]
descontos = [0.1, 0.2, 0.05]


precos_com_desconto = list(map(lambda preco, desconto: preco* (1-desconto), precos,descontos))
print(precos_com_desconto)

