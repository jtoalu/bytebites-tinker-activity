from models import Item, ItemCatalog, Transaction


def test_calculate_total_with_multiple_items():
	transaction = Transaction()
	transaction.add_item(Item("Spicy Burger", 8.50, "Meals", 4.8))
	transaction.add_item(Item("Large Soda", 2.75, "Drinks", 4.2))
	transaction.add_item(Item("Chocolate Cake", 5.25, "Desserts", 4.9))

	total = transaction.calculate_total()

	assert total == 16.50
	assert transaction.total_cost == 16.50


def test_order_total_is_zero_when_empty():
	transaction = Transaction()

	total = transaction.calculate_total()

	assert total == 0.0
	assert transaction.total_cost == 0.0


def test_filter_menu_items_by_category():
	catalog = ItemCatalog()
	burger = Item("Spicy Burger", 8.50, "Meals", 4.8)
	soda = Item("Large Soda", 2.75, "Drinks", 4.2)
	iced_tea = Item("Iced Tea", 3.00, "Drinks", 4.6)
	catalog.add_item(burger)
	catalog.add_item(soda)
	catalog.add_item(iced_tea)

	assert catalog.filter_by_category("Drinks") == [soda, iced_tea]
	assert catalog.filter_by_category("Desserts") == []
