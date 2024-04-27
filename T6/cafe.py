menu = ['latte', 'mocha', 'hot chocolate', 'americano']

stock = {'latte':3, 'mocha': 6, 'hot chocolate': 8, 'americano': 12 }

price = {'latte':5, 'mocha': 4, 'hot chocolate': 3, 'americano': 6}

def calculate_stock_worth(stock, price):
    total_worth = 0
    for product, quantity in stock.items():
        # Check if the product exists in both dictionaries
        if product in price:
            # Calculate the worth of the product (quantity * price)
            product_worth = quantity * price[product]
            # Add the product worth to the total worth
            total_worth += product_worth
        else:
            print(f"Price for {product} is not available.")
    return total_worth

total_stock_worth = calculate_stock_worth(stock, price)
print("Total stock worth:", total_stock_worth)