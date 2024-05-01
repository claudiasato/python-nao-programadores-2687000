# Crie uma lista apenas com elementos numéricos
lista_itens = [1,3,5,7]

# Crie uma lista contendo todos os tipos e estrutura de dados que você aprendeu até agora
lista_2 = [1,4,7, 'ana', ['x','y',99]]

# Imprima na tela apenas os 5 primeiros elementos da lista
print(lista_2[2])
# Crie um slice na lista para que imprima na tela os elementos de índice par
lista_itens[0:-1:2]
print(lista_itens)

# Remova da lista o último item

# Insira na lista um novo item
lista_itens.append('teste')
print(lista_itens)

lista_itens.extend(lista_2)
print(lista_itens)
# Remova da lista um item específico
lista_itens.remove('teste')
print(lista_itens)
