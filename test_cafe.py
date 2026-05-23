from cafe import Cafe

def test_calculate_profit():
    # Initial cafe should be running at a loss before any changes
    cafe = Cafe("Test Cafe")
    profit = cafe.calculate_profit()
    assert profit < 1000, f"Initial profit seems too high: {profit}"
    print("test_calculate_profit passed")

def test_price_affects_sales():
    # Raising price above base should reduce sales volume
    cafe = Cafe("Test Cafe")
    item = cafe.menu[0]
    sales_before = cafe.calculate_item_sales(item)
    cafe.update_item_price(0, item["base_price"] + 2)
    sales_after = cafe.calculate_item_sales(item)
    assert sales_after < sales_before, "Higher price should reduce sales"
    print("test_price_affects_sales passed")

def test_fire_last_barista():
    # Should never be allowed to fire the only remaining barista
    cafe = Cafe("Test Cafe")
    cafe.baristas = 1
    cafe.fire_barista(1)
    assert cafe.baristas == 1, "Should not be able to fire last barista"
    print("test_fire_last_barista passed")


# Run all tests
test_calculate_profit()
test_price_affects_sales()
test_fire_last_barista()

print("\nAll tests passed!")