def get_values(data):
    response = []

    for value in data.values():
        response.append(value)

    return response

def transform_values(prices, to_currency):
    response = {}

    for key, value in prices.items() :
        response.update({key : to_currency(value)})

    return response

def merge_objects(value_1, value_2):
    response = {**value_1, **value_2}

    for key in value_2.keys():
        if key in value_1 and key in value_2:
            response[key] = value_1[key] + value_2[key]

    return response

def filter_object(object, condition):
    response = {}

    for key, value in object.items() :
        if condition(value):
            response.update({key : value})

    return response

def flat_to_nested(object):
    response = {}
    for key, value in object.items() :
        new_key = key.split('.')

        if response.get(new_key[0]):
            response.get(new_key[0]).update({new_key[1] : value})
        else :
            response.update({new_key[0]: {new_key[1] : value}})            

    return response

def find_keys_by_values(object, in_stock):
    response = []

    for key, value in object.items():
        if value == in_stock:
            response.append(key)

    return response

def create_object_from_arrays(array_1, array_2):
    response = {}

    for key, value in zip(array_1, array_2):
        response.update({key : value})

    return response

def count_values(object):
    response = {}
    
    for value in object.values():

        if response.get(value):
           response[value] += 1
        else :
            response.update({value: 1})  

    return response

def extract_properties(object, properties):
    response = {}

    for key, value in object.items():
        if key in properties:
            response.update({key: value})

    return response

def sort_object_by_value(object):
    response = dict(sorted(object.items(), key=lambda item: item[1]))

    return response

def find_max_value(object):
    response = max(object.items(), key=lambda item: item[1])[1]

    return response

def create_object_from_pairs(list):
    response = {}

    for el in list:
        response.update({el[0]: el[1]})

    return response