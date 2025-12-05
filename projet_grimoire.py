import json
with open("inventory.json","r") as f:
    inventory = json.load(f)


# for items_id, (items_name,price) in inventory.items():
#     nb_item = items_id
#     print(items_id," : ",items_name)


# item_chosed = []
# choice = input("Quel objet voulez vous choisir : ").split(" ")
# for i in choice :
#     if i in inventory:
#         item_name = inventory[i][0]
#         item_chosed.append(item_name)
#     else :
#         print("L'objet",i," n'est pas disponible")

# print("Vous avez choisi : ",end=" ")
# for j in item_chosed:
#     print(j,end=", ")


#print(F"name : {inventory('name')}")
# def tuple_function():
#     a,b = eval(input("entrez un tuple"))
#     t=(a,b)
#     return(str(t))
# print(tuple_function())
S = ((54,76,87,98,76,87,76))
for inte in S:
    S_l = list(S)
    S_t = tuple(S)
print(S_l,S_t)