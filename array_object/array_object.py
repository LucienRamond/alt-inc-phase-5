def filter_by_property(users, property, property_state):
    response = list(filter(lambda x: x[property] == property_state, users))

    return response

def group_by(products, category):
    response = {}

    for product in products :
        if response.get(product[category]):
           response.get(product[category]).append(product)
        else:
            response.update({product[category]: [product]})

    return response

def find_intersection(library1, library2, property):
    response = []

    for book_1 in library1:
        for book_2 in library2:
            if book_1[property] == book_2[property]:
                response.append(book_1)

    return response

def transform_array(employees, transformer):
    response = []
    
    for employee in employees:
        response.append(transformer(employee))

    return response

def aggregate_data(transactions, category, amount):
    response = {}

    for transaction in transactions :

        if response.get(transaction[category]):        
            response[transaction[category]] += transaction[amount]
        else:
            response.update({transaction[category]: transaction[amount]})

    return response