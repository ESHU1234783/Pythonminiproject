# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 190
}

total_investment = 0
portfolio = {}

print(" Stock Portfolio Tracker")
print("Available Stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("\nEnter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print(" Stock not found!")
        continue

    quantity = int(input(f"Enter quantity of {stock}: "))

    portfolio[stock] = quantity
    investment = stock_prices[stock] * quantity
    total_investment += investment

print("\n------ Portfolio Summary ------")

for stock, quantity in portfolio.items():
    value = stock_prices[stock] * quantity
    print(f"{stock}: {quantity} shares × ${stock_prices[stock]} = ${value}")

print(f"\n Total Investment Value: ${total_investment}")

# Save result to a text file
with open("portfolio.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    file.write("----------------------\n")

    for stock, quantity in portfolio.items():
        value = stock_prices[stock] * quantity
        file.write(f"{stock}: {quantity} shares = ${value}\n")

    file.write(f"\nTotal Investment Value: ${total_investment}")

print("\n Portfolio saved to 'portfolio.txt'")