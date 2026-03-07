# ByteBites Models
#
# Customer: Represents a user with a name and purchase history (list of Orders).
#           Methods: verifyUser(), addOrder(), getPurchaseHistory()
#
# FoodItem: Represents a menu item with name, price, category, and popularityRating.
#
# Menu: Holds the full catalog of FoodItems.
#       Methods: filterByCategory()
#
# Order: Groups selected FoodItems into a transaction; total is derived (not stored).
#        Methods: addFoodItem(), computeTotal(), getItems()


class FoodItem:
    def __init__(self, name: str, price: float, category: str, popularity_rating: float):
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating


class Menu:
    def __init__(self, items: list = None):
        self.items: list[FoodItem] = items or []

    def filter_by_category(self, category: str) -> list:
        return [item for item in self.items if item.category.lower() == category.lower()]


class Order:
    def __init__(self):
        self.items: list[FoodItem] = []

    def add_food_item(self, item: FoodItem) -> None:
        self.items.append(item)

    def compute_total(self) -> float:
        return sum(item.price for item in self.items)

    def get_items(self) -> list:
        return list(self.items)

    @property
    def total(self) -> float:  # derived, not stored
        return self.compute_total()


class Customer:
    def __init__(self, name: str):
        self.name = name
        self.purchase_history: list[Order] = []

    def verify_user(self) -> bool:
        return bool(self.name)

    def add_order(self, order: Order) -> None:
        self.purchase_history.append(order)

    def get_purchase_history(self) -> list:
        return list(self.purchase_history)
