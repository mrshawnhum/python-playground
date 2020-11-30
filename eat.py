price = 20

if price > 22:
    print("That'll be " + str(price) + " please!")
    print("Thank you for your order!")
elif price < 22:
    print("Please add $" + str(int(22 - price )) + " to complete order!")