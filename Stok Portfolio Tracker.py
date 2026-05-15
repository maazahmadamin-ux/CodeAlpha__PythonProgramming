# Dictionary containing stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 330,
    "AMZN": 145
}

portfolio = {}

total_investment = 0

print("\n Stock Portfolio Tracker")
print("Available Stocks:")

for stock, price in stock_prices.items():
    print(f"{stock} : ${price}")

# Input number of stocks
num = int(input("\nHow many stocks do you want to add? "))

for i in range(num):
    stock_name = input("Enter stock name: ").upper()

    if stock_name not in stock_prices:
        print(" Stock not available.")
        continue

    quantity = int(input("Enter quantity: "))

    portfolio[stock_name] = quantity

# Calculate investment
print("\n Portfolio Summary")

for stock, quantity in portfolio.items():
    investment = stock_prices[stock] * quantity
    total_investment += investment

    print(f"{stock} -> {quantity} shares × ${stock_prices[stock]} = ${investment}")

print(f"\n Total Investment Value = ${total_investment}")

# Save result in file
save = input("\nDo you want to save the report? (yes/no): ").lower()

if save == "yes":
    with open("portfolio_report.txt", "w") as file:
        file.write("Stock Portfolio Report\n")
        file.write("========================\n")

        for stock, quantity in portfolio.items():
            investment = stock_prices[stock] * quantity
            file.write(f"{stock} -> {quantity} shares = ${investment}\n")

        file.write(f"\nTotal Investment = ${total_investment}")

    print(" Report saved as portfolio_report.txt")