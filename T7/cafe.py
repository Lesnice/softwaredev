menu = ["pasty", "coffee", "tea", "pie"]

stock ={"pasty": 30,
        "coffee": 40,
        "tea": 50,
        "pie":10}
price = {"pasty": 2.5,
        "coffee": 1.5,
        "tea": 1,
        "pie":5}

total_stock = sum(stock[item] * price[item] for item in menu)

# Print the results
print("Menu items:")
for item in menu:
    print(f"- {item}: Stock - {stock[item]}, Price - £{price[item]}")
print(f"\nTotal stock worth of the cafe: £{total_stock}")
