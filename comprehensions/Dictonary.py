tea_prices_inr = {
    "Masala Chai": 50,
    "Green Tea": 40,
    "Lemon Tea": 45,
}
""
"All Prices need to be converted to USD with a conversion rate of 1 INR = 0.012 USD"
""
tea_prices_usd = {tea:price * 80 for tea,price in tea_prices_inr.items() }
print(tea_prices_usd)