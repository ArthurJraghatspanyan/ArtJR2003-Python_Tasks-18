# Write a function to calculate the total price of items in a shopping cart.
#	Use positional-only arguments for item prices.
#	Use a keyword argument for the tax rate with a default value.
#	Return the total price including tax.

def total_price(*prices, tax = 0.5):
	price = 0
	for i in prices:
		price += i

	price_plus_tax = price + (price * tax / 100)
	return price_plus_tax

res1 = total_price(400, 600, 300)
print(res1)

res2 = total_price(500, 1000, 200, tax = 1.2)
print(res2)
