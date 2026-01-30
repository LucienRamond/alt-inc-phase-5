from array_object import filter_by_property, group_by, find_intersection, transform_array, aggregate_data

def test_filter_by_property():
    users = [
        {"id": 1, "name": "Alice", "age": 25, "active": True},
        {"id": 2, "name": "Bob", "age": 30, "active": False},
        {"id": 3, "name": "Charlie", "age": 35, "active": True}
    ]
    assert filter_by_property(users, 'active', True) == [{"id": 1, "name": "Alice", "age": 25, "active": True}, {"id": 3, "name": "Charlie", "age": 35, "active": True}]

def test_group_by():
    products = [
        {"id": 1, "name": "Laptop", "category": "Electronics", "price": 999},
        {"id": 2, "name": "Smartphone", "category": "Electronics", "price": 699},
        {"id": 3, "name": "T-shirt", "category": "Clothing", "price": 29}
    ]
    assert group_by(products, 'category') == {"Electronics": [{"id": 1, "name": "Laptop", "category": "Electronics", "price": 999}, {"id": 2, "name": "Smartphone", "category": "Electronics", "price": 699},], "Clothing": [{"id": 3, "name": "T-shirt", "category": "Clothing", "price": 29}]}

def test_find_intersection():
    library1 = [
        {"id": 1, "title": "1984", "author": "Orwell", "available": True},
        {"id": 2, "title": "Dune", "author": "Herbert", "available": False}
    ]
    library2 = [
        {"id": 3, "title": "1984", "author": "Orwell", "available": True},
        {"id": 4, "title": "Foundation", "author": "Asimov", "available": True}
    ]
    assert find_intersection(library1, library2, 'title') == [{"id": 1, "title": "1984", "author": "Orwell", "available": True}]

def test_transform_array():
    employees = [
        {"id": 1, "firstName": "John", "lastName": "Doe", "salary": 50000},
        {"id": 2, "firstName": "Jane", "lastName": "Smith", "salary": 60000}
    ]
    transformer = lambda emp: {
        "id": emp["id"],
        "fullName": f"{emp['firstName']} {emp['lastName']}",
        "annualSalary": emp["salary"] * 12
    }
    assert transform_array(employees, transformer) == [{'id': 1, 'fullName': 'John Doe', 'annualSalary': 600000}, {'id': 2, 'fullName': 'Jane Smith', 'annualSalary': 720000}]

def test_aggregate_data():
    transactions = [
        {"id": 1, "type": "debit", "amount": 100, "category": "Food"},
        {"id": 2, "type": "debit", "amount": 50, "category": "Food"},
        {"id": 3, "type": "credit", "amount": 75, "category": "Income"}
    ]
    assert aggregate_data(transactions, 'category', 'amount') == {"Food": 150, "Income": 75}

test_filter_by_property()
test_group_by()
test_find_intersection()
test_transform_array()
test_aggregate_data()