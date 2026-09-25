from models import Customer, Item, ItemCatalog, Transaction


def main() -> None:
    spicy_burger = Item("Spicy Burger", 8.50, "Meals", 4.8)
    large_soda = Item("Large Soda", 2.75, "Drinks", 4.2)
    chocolate_cake = Item("Chocolate Cake", 5.25, "Desserts", 4.9)
    iced_tea = Item("Iced Tea", 3.00, "Drinks", 4.6)

    sample_items = (spicy_burger, large_soda, chocolate_cake, iced_tea)
    print("Sample items (constructor fields and get_price):")
    for item in sample_items:
        print(
            f"- {item.name}: ${item.get_price():.2f}; "
            f"category={item.category}; popularity={item.popularity_rating}"
        )
    assert spicy_burger.name == "Spicy Burger"
    assert spicy_burger.get_price() == 8.50

    menu = ItemCatalog()
    assert menu.items == []
    for item in sample_items:
        menu.add_item(item)
    assert menu.items == list(sample_items)
    print(f"\nMenu contains {len(menu.items)} items.")

    for field, descending in (
        ("name", False),
        ("price", False),
        ("popularity_rating", True),
    ):
        sorted_items = menu.sort_items(field, descending=descending)
        assert sorted_items == sorted(
            sample_items,
            key=lambda item: getattr(item, field),
            reverse=descending,
        )
        print(f"\nMenu sorted by {field} ({'descending' if descending else 'ascending'}):")
        for item in sorted_items:
            if field == "name":
                print(f"- {item.name}")
            elif field == "popularity_rating":
                sort_value = f"rating {item.popularity_rating}"
                print(f"- {item.name}: {sort_value}")
            elif field == "price":
                sort_value = f"${item.get_price():.2f}"
                print(f"- {item.name}: {sort_value}")
    assert menu.items == list(sample_items)

    drinks = menu.filter_by_category("Drinks")
    assert drinks == [large_soda, iced_tea]
    assert menu.filter_by_category("Not on the menu") == []
    print("\nDrinks category:")
    for item in drinks:
        print(f"- {item.name}: ${item.price:.2f}")

    order = Transaction()
    assert order.items == []
    assert order.calculate_total() == 0.0
    order.add_item(spicy_burger)
    order.add_item(large_soda)
    total = order.calculate_total()
    assert total == 11.25
    print("\nOrder items:")
    for item in order.items:
        print(f"- {item.name}: ${item.get_price():.2f}")
    print(f"\nOrder contains {len(order.items)} items; total: ${total:.2f}")

    customer = Customer("Alex")
    assert customer.name == "Alex"
    assert customer.get_purchase_history() == []
    customer.add_purchase(order)
    assert customer.get_purchase_history() == [order]
    print(f"\n{customer.name}'s purchase history: {len(customer.get_purchase_history())} order")

    print("\nAll demo assertions passed.")


if __name__ == "__main__":
    main()
