fruits =['ananas' , 'banane' , 'cerise']

# accès en lecture d'un ou des élément(s) de la liste
print(fruits)
print(fruits [0])

my_fruit = fruits [0]
print(my_fruit)


# accès en écriture d'un ou des élément(s) de la liste
fruits[0] = 'abricot'
print(fruits)
print(fruits [0])

my_count = len(fruits)

index = 0
if index < my_count:
    print(fruits[index])
    print(f'{index = }')

index += 1
if index < my_count:
    print(fruits[index])
    print(f'{index = }')
index += 1
if index < my_count:
    print(fruits[index])
    print(f'{index = }')
index += 1
if index < my_count:
    print(fruits[index])
    print(f'{index = }')

