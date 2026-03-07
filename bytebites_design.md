# ByteBites UML Class Diagram

## Diagram

```
┌──────────────────────────────┐         ┌──────────────────────────────┐
│           Customer            │         │           FoodItem            │
├──────────────────────────────┤         ├──────────────────────────────┤
│ - name: String                │         │ - name: String               │
│ - purchaseHistory: List<Order>│         │ - price: Float               │
├──────────────────────────────┤         │ - category: String           │
│ + verifyUser(): Boolean       │         │ - popularityRating: Float    │
│ + addOrder(order): void       │         │                              │
│ + getPurchaseHistory(): List  │         │                              │
└──────────────────────────────┘         └──────────────────────────────┘
           │                                            ▲
           │ places                                     │ contains
           ▼                                            │
┌──────────────────────────────┐         ┌──────────────────────────────┐
│            Order              │         │             Menu              │
├──────────────────────────────┤         ├──────────────────────────────┤
│ - items: List<FoodItem>       │ browses │ - items: List<FoodItem>      │
│ / total: Float (derived)      │◄────────├──────────────────────────────┤
├──────────────────────────────┤         │ + filterByCategory(cat):List │
│ + addFoodItem(item): void     │         └──────────────────────────────┘
│ + computeTotal(): Float       │
│ + getItems(): List<FoodItem>  │
└──────────────────────────────┘
```

## Relationships

- `Customer` **places** an `Order` (one-to-many)
- `Customer.purchaseHistory` is typed as `List<Order>` to link history to real transactions
- `Customer` **browses** the `Menu` to select items into an `Order`
- `Menu` **contains** `FoodItem` objects and supports filtering by category
- `Order.items` is `List<FoodItem>` — items chosen from the Menu catalog
- `total` is marked as derived (`/`) — computed by `computeTotal()`, never stored independently

## Classes

### Customer
| Member | Type | Notes |
|---|---|---|
| name | String | Customer's display name |
| purchaseHistory | List\<Order\> | Links to past Order objects |
| verifyUser() | Boolean | Confirms the customer is a real user |
| addOrder(order) | void | Adds an order to purchase history |
| getPurchaseHistory() | List\<Order\> | Returns all past orders |

### FoodItem
| Member | Type | Notes |
|---|---|---|
| name | String | e.g. "Spicy Burger" |
| price | Float | Cost of the item |
| category | String | e.g. "Drinks", "Desserts" |
| popularityRating | Float | Ranking/rating value |

### Menu
| Member | Type | Notes |
|---|---|---|
| items | List\<FoodItem\> | Full catalog of all items |
| filterByCategory(cat) | List\<FoodItem\> | Returns items matching the given category |

### Order
| Member | Type | Notes |
|---|---|---|
| items | List\<FoodItem\> | Items selected from the Menu |
| total | Float | Derived — computed, not stored independently |
| addFoodItem(item) | void | Adds a FoodItem to the order |
| computeTotal() | Float | Sums the price of all items in the order |
| getItems() | List\<FoodItem\> | Returns all selected items |
