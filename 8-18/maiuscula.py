def para_maiuscula(texto:str)->str:
    return texto.upper()

nomes= ["ana", "bruno", "carla"]

nomes_maiusculos = list(map(para_maiuscula,nomes))
print(nomes_maiusculos)

nomes_maiusculos2 = list(map(lambda nome:nome.upper(),nomes))
print(nomes_maiusculos2)