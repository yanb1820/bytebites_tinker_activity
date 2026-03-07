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
