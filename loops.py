# while False:  # while == tant que
#     print("ce message ne sera pas affiché")

# while True:
#     print("Ce message sera affiché en boucle")

counter = 10

while counter:
    print(f"{counter = }")
    counter -= 1

counter = 0

while counter <= 10:
    print(f"{counter = }")
    counter += 1

for counter in range(0, 10):
    print(f"{counter = }")

for counter in range(0, 10, 2):
    print(f"{counter = }")


fruits = ['abricot' , 'baie' , 'cerise']
for i in range(0, len(fruits)):
    print(fruits[i])

for i in range(0, 10):
    for j in range(0,10):
        print(i, j)

my_array = [
    ['a' , 'c'],
    ['b' , 'd']
]

for i in range(0, len(my_array)): #len(my_array) me donne le nombre de ligne                    # inverser i et j pour inverser les colones et les lignes 
    for j in range(0, len(my_array[0])): #len(my_array[0]) me donne le nombre de colone
        print(i, j, my_array[i][j])