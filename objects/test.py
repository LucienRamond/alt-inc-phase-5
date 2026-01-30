from objects import get_values, transform_values, merge_objects, filter_object, flat_to_nested, find_keys_by_values, create_object_from_arrays, count_values, extract_properties, sort_object_by_value, find_max_value, create_object_from_pairs, find_value_in_object

def test_get_values():
    scores = {
        "level1": 100,
        "level2": 85,
        "level3": 95
    }
    assert get_values(scores) == [100, 85, 95]

def test_transform_values():
    prices_in_euros = {
        "book": 20,
        "pen": 5,
        "notebook": 10
    }
    to_dollars = lambda euros: euros * 1.1
    assert transform_values(prices_in_euros, to_dollars) == { "book": 22.0, "pen": 5.5, "notebook": 11.0 }

def test_merge_objects():
    store1_sales = { "january": 1000, "february": 1200, "march": 900 }
    store2_sales = { "january": 800, "february": 950, "march": 1100 }
    merge_objects(store1_sales, store2_sales)

    assert merge_objects(store1_sales, store2_sales) == { "january": 1800, "february": 2150, "march": 2000 }

def test_filter_object():
    inventory = {
        "laptop": 0,
        "smartphone": 5,
        "tablet": 0,
        "headphones": 8
    }
    assert filter_object(inventory, lambda stock: stock == 0) == { "laptop": 0, "tablet": 0 }

def test_flat_to_nested():
    flat_config = {
        'app.name': 'MyApp',
        'app.version': '1.0.0',
        'database.host': 'localhost',
        'database.port': 5432
    }
    assert flat_to_nested(flat_config) ==  { 'app': { 'name': 'MyApp', 'version': '1.0.0' }, 'database': { 'host': 'localhost', 'port': 5432 } }

def test_find_keys_by_values():
    product_stock = {
        "laptop": 0,
        "mouse": 5,
        "keyboard": 0,
        "monitor": 3
    }
    assert find_keys_by_values(product_stock, 0) ==  ["laptop", "keyboard"]

def test_create_object_from_arrays():
    player_names = ["Alice", "Bob", "Charlie"]
    scores = [100, 85, 90]
    assert create_object_from_arrays(player_names, scores) ==  { "Alice": 100, "Bob": 85, "Charlie": 90 }

def test_count_values():
    order_statuses = {
        "order1": "pending",
        "order2": "delivered",
        "order3": "pending",
        "order4": "cancelled",
        "order5": "pending"
    }
    assert count_values(order_statuses) ==  { "pending": 3, "delivered": 1, "cancelled": 1 }

def test_extract_properties():
    user_profile = {
        "name": "Jean Martin",
        "email": "jean@email.com",
        "password": "secret123",
        "age": 35,
        "address": "123 rue Principal"
    }
    public_info = ["name", "age"]
    assert extract_properties(user_profile, public_info) ==  { "name": "Jean Martin", "age": 35 }

def test_sort_object_by_value():
    player_scores = {
        "Alice": 85,
        "Bob": 92,
        "Charlie": 78,
        "David": 95
    }
    assert sort_object_by_value(player_scores) ==  { "Charlie": 78, "Alice": 85, "Bob": 92, "David": 95 }

def test_find_max_value():
    game_scores = {
        "level1": 850,
        "level2": 920,
        "level3": 880,
        "level4": 1020
    }
    assert find_max_value(game_scores) ==  1020

def test_create_object_from_pairs():
    product_pairs = [
        ["pommes", 2.5],
        ["bananes", 1.8],
        ["oranges", 2.2]
    ]
    assert create_object_from_pairs(product_pairs) ==  { "pommes": 2.5, "bananes": 1.8, "oranges": 2.2 }

test_get_values()
test_transform_values()
test_merge_objects()
test_filter_object()
test_flat_to_nested()
test_find_keys_by_values()
test_create_object_from_arrays()
test_count_values()
test_extract_properties()
test_sort_object_by_value()
test_find_max_value()
test_create_object_from_pairs()