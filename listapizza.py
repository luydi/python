pizzas = ['frango', 'calabresa','barreado']
friends_pizzas = pizzas[:]

friends_pizzas.append('4 queijos')

print("minhas pizzas favoritas são:")
for pizza in pizzas:
    print(pizza)

print("essas são as pizzas favoritas dos meus amigos:")
for friendspiz in friends_pizzas:
    print(friendspiz)



