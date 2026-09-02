users = {'John': 500, 'Sam': 5874, 'Dave': 560,
         'Cat': 400, 'Jack': 5874, 'Michael': 20}


def custom_function(list):
    list = sorted(list.keys(), key=lambda item: item[1])
    return list[-3:]


print(custom_function(users))
