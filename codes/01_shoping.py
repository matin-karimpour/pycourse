shoping_list = ["oil", "potato", "tomato", "rice"]
prices = {
    "oil": 70,
    "potato":15,
    "tomato": 20,
    "rice": 300
}
budget = 400
basket = []

for item in shoping_list:
    price = prices[item]
    if price < budget:
        basket.append(item)
        budget = budget - price
    else:
        print("budget is not enough for this ", item)

print("your final basket is ", basket)
print("your final budget is ", budget)