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
		pass

	def add_purchase(self, transaction: "Transaction") -> None:
		pass

	def get_purchase_history(self) -> list["Transaction"]:
		pass


class Item:
	def __init__(
		self,
		name: str,
		price: float,
		category: str,
		popularity_rating: float,
	):
		pass

	def get_price(self) -> float:
		pass


class ItemCatalog:
	def __init__(self):
		pass

	def add_item(self, item: Item) -> None:
		pass

	def filter_by_category(self, category: str) -> list[Item]:
		pass


class Transaction:
	def __init__(self):
		pass

	def add_item(self, item: Item) -> None:
		pass

	def calculate_total(self) -> float:
		pass
