daily_Sales = [100, 200, 300, 400, 500]

total_cups = sum(milan for milan in daily_Sales if milan > 100)
# total_cups = [milan for milan in daily_Sales if milan >100]
print(total_cups)
