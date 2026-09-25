from models import FoodItem, Menu, Order, Customer


def make_item(name="Item", price=1.0, category="Entrees", rating=4.0):
    return FoodItem(name, price, category, rating)


# --- FoodItem ---

def test_food_item_stores_attributes():
    item = make_item("Spicy Burger", 9.99, "Entrees", 4.2)
    assert item.name == "Spicy Burger"
    assert item.price == 9.99
    assert item.category == "Entrees"
    assert item.popularity_rating == 4.2


# --- Menu: filtering ---

def test_filter_returns_matching_category():
    soda  = make_item("Large Soda",  2.49, "Drinks",  3.8)
    shake = make_item("Mango Shake", 4.99, "Drinks",  4.7)
    cake  = make_item("Choc Cake",   5.99, "Desserts", 4.9)
    menu  = Menu([soda, shake, cake])
    result = menu.filter_by_category("Drinks")
    assert len(result) == 2
    assert all(item.category == "Drinks" for item in result)

def test_filter_is_case_insensitive():
    soda = make_item("Large Soda", 2.49, "Drinks", 3.8)
    menu = Menu([soda])
    assert len(menu.filter_by_category("drinks")) == 1
    assert len(menu.filter_by_category("DRINKS")) == 1

def test_filter_returns_empty_for_no_match():
    burger = make_item("Spicy Burger", 9.99, "Entrees", 4.2)
    menu   = Menu([burger])
    assert menu.filter_by_category("Desserts") == []


# --- Menu: sorting ---

def test_sort_by_popularity_descending():
    low  = make_item("Fries",      3.49, "Entrees", 3.5)
    mid  = make_item("Burger",     9.99, "Entrees", 4.2)
    high = make_item("Choc Cake",  5.99, "Desserts", 4.9)
    menu = Menu([low, mid, high])
    sorted_items = menu.sort_by_popularity()
    ratings = [item.popularity_rating for item in sorted_items]
    assert ratings == sorted(ratings, reverse=True)

def test_sort_by_price_ascending():
    items = [
        make_item("Burger", 9.99, "Entrees",  4.2),
        make_item("Soda",   2.49, "Drinks",   3.8),
        make_item("Cake",   5.99, "Desserts", 4.9),
    ]
    menu = Menu(items)
    sorted_items = menu.sort_by_price()
    prices = [item.price for item in sorted_items]
    assert prices == sorted(prices)

def test_sort_does_not_mutate_menu():
    burger = make_item("Burger", 9.99, "Entrees",  4.2)
    soda   = make_item("Soda",   2.49, "Drinks",   3.8)
    menu   = Menu([burger, soda])
    original_order = [item.name for item in menu.items]
    menu.sort_by_popularity()
    menu.sort_by_price()
    assert [item.name for item in menu.items] == original_order


# --- Order: totals ---

def test_order_total_with_multiple_items():
    order = Order()
    order.add_food_item(make_item("Burger", 9.99, "Entrees", 4.2))
    order.add_food_item(make_item("Soda",   2.49, "Drinks",  3.8))
    assert round(order.compute_total(), 2) == 12.48
    assert round(order.total, 2) == 12.48

def test_order_total_is_zero_when_empty():
    order = Order()
    assert order.compute_total() == 0.0
    assert order.total == 0.0

def test_order_total_with_single_item():
    order = Order()
    order.add_food_item(make_item("Cake", 5.99, "Desserts", 4.9))
    assert round(order.total, 2) == 5.99

def test_get_items_returns_all_added():
    order = Order()
    burger = make_item("Burger", 9.99, "Entrees", 4.2)
    soda   = make_item("Soda",   2.49, "Drinks",  3.8)
    order.add_food_item(burger)
    order.add_food_item(soda)
    items = order.get_items()
    assert len(items) == 2
    assert items[0].name == "Burger"
    assert items[1].name == "Soda"


# --- Customer ---

def test_verify_user_true_for_named_customer():
    customer = Customer("Alex")
    assert customer.verify_user() is True

def test_verify_user_false_for_empty_name():
    customer = Customer("")
    assert customer.verify_user() is False

def test_add_order_appears_in_history():
    customer = Customer("Alex")
    order = Order()
    order.add_food_item(make_item("Burger", 9.99, "Entrees", 4.2))
    customer.add_order(order)
    history = customer.get_purchase_history()
    assert len(history) == 1
    assert round(history[0].total, 2) == 9.99

def test_purchase_history_tracks_multiple_orders():
    customer = Customer("Alex")
    customer.add_order(Order())
    customer.add_order(Order())
    assert len(customer.get_purchase_history()) == 2
