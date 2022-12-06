import random
import math

# = affectation
foo = 123

# + addition
foo = 123 + 42
foo = foo + 42 # foo +=42 opérateur d'indcrémentation

# - soustraction 
foo = 123 - 42
foo = foo - 42 # foo -=42 opérateur de décrémentation

# / division 
foo = 123 / 42
foo = foo / 42 # foo /=42
print(foo)
print(type(foo))

# // division entière 
foo = 123 // 42
foo = foo // 42 # foo //=42
print(foo)
print(type(foo))

# % modulo
foo = 4 % 3
print(foo)
foo = random.randint(1, 100)
print(foo)
print(foo % 2)

# * multiplication


# ** puissance
foo = 2 ** 2
foo = 2 ** 3
foo = 2 ** 4
foo = 2 ** 5
foo = 2 ** 6
print(foo)
foo = math.sqrt(4)

# sqrt() racine carré

# les opérateurs de comparaison

# l'égalité ==
result = 1 == 1
print(result)

# les grandeurs 
result = 123 < 42
print(result)

# plus petit ou égal à
result = 123>=42
print(result)

#  l'inégalité 
result = 123 != 42
print(result)

# les encadrements 
# <> <= >=
my_number = random.randint(0, 100)
print(my_number)
result = 0 <= my_number <= 50
print(result)

# operateur and (et)
result = True and False
print(result)
result = False and True
print(result)
result = True and True
print(result)
result = False and False
print(result)

a =random.randint(0, 1)
b = random.randint(0, 1)
result = bool(a) and bool(b)
print(a, b)
print(result)

# utilisations un peu spéciales des comparaisons de grandeur
result = "abc" > "bcd" # une lettre a un chiffre définie par rapport au ascii (voir sur internet)
print(result)

# operateur or (ou)
result = True or False
print(result)
result = False or True
print(result)
result = True or True
print(result)
result = False or False
print(result)

# opérateur not (négation)
result = not True
print(result)
result = not False
print(result)
