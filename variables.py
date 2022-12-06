# l'operateur d'affection = permet d'injecter une valeur dans une variable 
# Avec Python on doit utiliser le snake case ma_variable pas de majuscule et pas de chiffre au debut.

# integer, nombre entier

my_number1 = 123
my_number2 = -42
my_number6 = 0

print(my_number1)
print(my_number2)
print(my_number6)
print(type(my_number1))

# float, nombre à virgule flottante

my_number3 = 3.14
my_number4 = -2.71
my_number5 = 0.0

# 0 = integer 0.0 .0 0. = float

print(my_number3)
print(my_number4)
print(my_number5)
print(type(my_number3))

# boolean = True / False

my_boolean1 = True
my_boolean2 = False
print(my_boolean1)
print(my_boolean2)
print(type(my_boolean1))

# None,valeur nulle

my_none= None
print(my_none)
print(type(my_none))

# string, chaîne de caractères "", ''

my_text1 = "Ceci est une chaîne de caractères"
my_text2 = "Ceci est aussi une chaîne de caractères"

print(my_text1)
print(my_text2)

# \n = saut de ligne

my_text3 = "abc\ndef\nghi"
my_text4 = "\\"
my_text5 = 'John "Foo" Doo'
# ou my_text5 = "John \"Foo\" Doo"
my_text6 = """abc
def
ghi"""

print(my_text3)
print(my_text4)
print(my_text5)
print(my_text6)
print(type(my_text1))

# affectation d'une variable à partir d'une variable

foo = "Lorem Ipsum"
bar = foo
print(bar)

# permutation de la valeur des variables

a = 123
b = 42
a, b = b, a

print(a, b)

a = 123
b = 42
c = b
b = a
a = c
print(a,b)

# variante qui fonctionne qu'avec des nombres

c = a + b
a = c - a 
b = c - b
print(a, b)

# à vous de jouer

# transtypage

foo = "123"
foo = int(foo)
print(type(foo))

foo = "123"
foo = float(foo)
print(type(foo))

# supprime les chiffres derrière la virgule.

foo = 3.14
foo = int(foo)
print(type(foo))
print(foo)

foo = 3.14
foo = str(foo)
print(type(foo))
#
foo = 2.71
# récupérer la partie entière
a = int(foo)
print(a)
# récupérer la partie après virgule
b = foo - a
print(b)

# transtypage == tyoe casting == conversion d'un type de données

my_number7 = 10
print(bool(my_number7))
if bool(my_number7):
    print("L'utilisateur a mis autre chose que 0")
else :
    print("L'utilisateur a mis 0")

my_text7 = "salut"
if bool(my_text7):
    print("L'utilisateur a mis du texte")
else :
    print("L'utilisateur n'a mis aucun texte")

# listes 

fruits = ['ananas' , 'bananes' , 'cerise']
result = 'ananas' in fruits
print(result)
result = 'fraise' in fruits
print(result)

# conversion explicite
result = bool(fruits)
print(result)

# implicite 
if fruits:
    print("La liste contient des éléments")
else :
    print("La liste ne contient pas d'éléments")