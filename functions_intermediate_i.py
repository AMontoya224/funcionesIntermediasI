x = [ [5,2,3], [10,8,9] ] 
estudiantes = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# 1. Actualizar valores en diccionarios y listas
print("#1")
x[1][0] = 15
print(x)
print(" ")

estudiantes[0]['last_name'] = 'Bryant'
print(estudiantes)
print(" ")

directorio_deportes['fútbol'][0] = 'Andrés'
print(directorio_deportes)
print(" ")

z[0]['y'] = 30
print(z)
print(" ")


# 2. Iterar a través de una lista de diccionarios
print("#2")
estudiantes = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(some_list):
    for i in range(0, len(some_list)):
        print(estudiantes[i])
    
    print(" ")
    print("Bonus:")
    for i in range(0, len(some_list)):
        nombre = estudiantes[i]['first_name']
        apellido = estudiantes[i]['last_name']
        print("first_name - " + nombre + ", last_name - " + apellido)

iterateDictionary(estudiantes)
print(" ")


# 3. Obtener valores de una lista de diccionarios
print("#3")
def iterateDictionary2(key_name, some_list):
    for i in range(0, len(some_list)):
        nombre = estudiantes[i][key_name]
        print(nombre)

iterateDictionary2('first_name', estudiantes)
print(" ")
iterateDictionary2('last_name', estudiantes)
print(" ")


# 4. Iterar a través de un diccionarios con valores de lista
print("#4")
def printInfo(some_dict):
    for i in some_dict:
        print("--------------")
        print(str(len(some_dict[i])) + " " + i.swapcase())
        for j in some_dict[i]:
            print(j)
        print(" ")

dojo = {
   'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

printInfo(dojo)