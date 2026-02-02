import pprint

'''name_family = ["Paulo","Bruna"]
print(name_family)

name_family.append("Sebastian")
name_family.insert(4, "Floki")

print(name_family)
print(name_family[0])
print(len(name_family))
print(f"O pai chama: {name_family[0]}, a mãe: {name_family[1]}, o filho: {name_family[2]} e o pet chama: {name_family[3]}")'''

family = {
    "Paulo R. P. Silva":{
        "age": 31,
        "height": 1.91,
        "weight": 118
    },
    "Bruna Castro":{
        "age": 29,
        "height": 1.66,
        "weight": 76
    },
     "Sebastian P. Castro":{
        "age": 2,
        "height": 0.90,
        "weight": 14
    },
     "Floki P. Castro":{
        "age": 4,
        "height": 0.30,
        "weight": 8
    },
}

pp = pprint.PrettyPrinter(depth=4)
'''pp.pprint(family)
print(len(family))
'''
'''family["Paulo R. P. Silva"]["cor"] = "Parda"
pp.pprint(family)

print(f"Segue as informações do pai: {family['Paulo R. P. Silva']['age']} anos")'''


# Acrescentando outro elemento a lista
family["Neide P. Silva"] = {
    "age": 62,
    "heigth": 1.66,
    "weight": 60
}

# 1 - Retornar o primeiro item da lista
primeiro_item = next(iter(family.items()))
print(primeiro_item)

# 2 - Retornar o elemento da posição 1
position_one = list(family.items())[1]
print(position_one)

# 3 - Retorna último elemento da lista
last_position = list(family.items())[-1]
print(last_position)

family["Neide"] = {
    "age": 62,
    "heigth": 1.66,
    "weight": 60
}

print(f"Mebros: {list(family.keys())}")

del family["Neide"] # Deleta 1 elemento do dicionário python
print(family)
print(len(family)) #Mostra o tamanho da lista dicionário
