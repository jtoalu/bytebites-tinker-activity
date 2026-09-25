'''
Four models (classes) are defined in this file.

Implementation Plan

Implement Item
- Add name, price, category, and popularity_rating.
- Validate required names, numeric prices, and non-negative prices.
- Add get_price() returning the current price.

Implement Transaction
- Initialize an ordered list of Item objects and total_cost.
- Add add_item(item) with type validation.
- Implement calculate_total() by summing each item’s current price.
- Ensure empty transactions calculate to 0.0.

Implement Customer
- Store the customer’s name and an ordered purchase history.
- Add add_purchase(transaction) to append completed transactions.
- Add get_purchase_history() returning the history.

Implement ItemCatalog
- Store items in insertion order.
- Add add_item(item).
- Implement exact-match filter_by_category(category).
- Return an empty list when no items match.

Add focused validation
- Test normal construction and method behavior.
- Test empty catalogs and transactions.
- Test invalid names, prices, and incorrect object types.
- Verify transaction totals reflect current item prices.
'''

class Customer:
	def __init__(self, name: str):
		if not isinstance(name, str):
			raise TypeError("name must be a string")
		if not name.strip():
			raise ValueError("name must not be empty")
		self.name = name
		self.purchase_history: list[Transaction] = []

	def add_purchase(self, transaction: "Transaction") -> None:
		if not isinstance(transaction, Transaction):
			raise TypeError("transaction must be a Transaction")
		self.purchase_history.append(transaction)

	def get_purchase_history(self) -> list["Transaction"]:
		return self.purchase_history


class Item:
	def __init__(
		self,
		name: str,
		price: float,
		category: str,
		popularity_rating: float,
	):
		if not isinstance(name, str):
			raise TypeError("name must be a string")
		if not name.strip():
			raise ValueError("name must not be empty")
		if isinstance(price, bool) or not isinstance(price, (int, float)):
			raise TypeError("price must be numeric")
		if price < 0:
			raise ValueError("price must not be negative")
		if not isinstance(category, str):
			raise TypeError("category must be a string")
		if not category.strip():
			raise ValueError("category must not be empty")
		self.name = name
		self.price = float(price)
		self.category = category
		self.popularity_rating = popularity_rating

	def get_price(self) -> float:
		return self.price


class ItemCatalog:
	def __init__(self):
		self.items: list[Item] = []

	def add_item(self, item: Item) -> None:
		if not isinstance(item, Item):
			raise TypeError("item must be an Item")
		self.items.append(item)

	def filter_by_category(self, category: str) -> list[Item]:
		return [item for item in self.items if item.category == category]

	def sort_items(self, by: str, descending: bool = False) -> list[Item]:
		if by not in ("name", "price", "popularity_rating"):
			raise ValueError("by must be 'name', 'price', or 'popularity_rating'")
		return sorted(self.items, key=lambda item: getattr(item, by), reverse=descending)


class Transaction:
	def __init__(self):
		self.items: list[Item] = []
		self.total_cost = 0.0

	def add_item(self, item: Item) -> None:
		if not isinstance(item, Item):
			raise TypeError("item must be an Item")
		self.items.append(item)

	def calculate_total(self) -> float:
		self.total_cost = sum((item.get_price() for item in self.items), 0.0)
		return self.total_cost
