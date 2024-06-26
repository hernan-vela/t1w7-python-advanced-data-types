# # Creating a dictionary
# my_dict = {
#     'name': 'Alice',
#     'age': 25,
#     'city': 'Sydney'
# }

# # Access the values by keys
# print(my_dict['city'])
# print(my_dict['age'])

# # Adding a new key-pair value
# my_dict['email'] = 'alice@example.com'
# print(my_dict)

# # Adding an item with an existing key overwrites the original value
# my_dict['city'] = 'Alice'
# print(my_dict)

# # Removing a key-value pair
# del my_dict['age']
# print("-------")
# print(my_dict)

# # Alternatively, you can use .pop()
# print("*********")
# my_dict.pop('email')
# print(my_dict)

# # Checking for key existence
# print('email' in my_dict)
# print('name' in my_dict)

# list_of_keys = list(my_dict.keys())
# list_of_values = list(my_dict.values())


# print(list_of_values.index('Alice'))
# print(list_of_keys[0])

# # Interate through dictionary
# for key, value in my_dict.items():
#     print(f"{key}, {value}")

# # Nested dictionaries
# nested_dict = {
#     'city': {'name': 'Alice', 'age': 25},
#     'person2': {'name': 'Bob', 'age': 30}
# }

# print(nested_dict['person2']['name'])

# # Merging Dictionaries
# merged_dict = my_dict | nested_dict
# print(merged_dict)

# Practice of dictionaries after class:

buyer_details = {
    'store': 'Santeo Plaza',
    'day of purchase': '18th June',
    'name': 'Alan Britto',
    'item': 'Hoodie',
    'price': '$240',
    'reason of return': 'Fabric decoloration'  
}

# print('item' in buyer_details)
# print(buyer_details['item'])

buyer_details['item'] = 'Fisherman hat'

# print(buyer_details['item'])
# print(buyer_details)

# list_of_keys = list(buyer_details.keys())
# list_of_values = list(buyer_details.values())
# print(list_of_values.index('Fabric decoloration'))
# print(list_of_keys[1])

# for key, value in buyer_details.items():
#     print(f"{key}, {value}")

dicty = {
    'date': {'day of purchase': '18th June', 'store': 'Santeo Plaza'},
    'buyer': {'name': 'Alan Britto', 'item': 'Hoodie'}
}

print(dicty['date']['store'])

dictionaries_together = buyer_details | dicty
print(dictionaries_together)