# 2. Entiers consécutifs
# 198, 199, 200, 201 et 202 sont des entiers consécutifs dont la somme est égale à 1000.
# Trouvez d'autres entiers consécutifs dont la somme vaut 1000.


result = []
for i in range(1, 1001):
    for j in range(i, 1001):
        calcul = sum(range(i, j))
        if calcul == 1000:
            result.append(list(range(i, j)))
print(result)

    


# dividende = 10
# diviseur = 3
# quotient = dividende // diviseur
# reste = dividende % diviseur 
# print(f'{quotient = }' f'{ reste = }')


# Étape     Reste       Test
# 1         10 - 3 = 7  Reste >= Diviseur
# 2         7 - 3 = 4   Reste >= Diviseur
# 3         4 - 3 = 1   Reste < Diviseur


dividende = 10
diviseur = 3
reste = dividende
quotient = 0

while reste >= diviseur:
    reste -= diviseur
    quotient += 1

print(f'quotient = {quotient}' f' reste = {reste}')


