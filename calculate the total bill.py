items = [
    {"name": "apple","price":2.4,"Quantity":4},
    {"name":"orange","price":3.0,"Quantity":5},
    {"name":"lemon","price":2.0,"Quantity":10}
]

#intilize total cost
total_cost=0.0

#calculate the cost
for item in items:
    item_total=item["price"]*item["Quantity"]
    total_cost+=item_total
    print(f"{item['name']}: {item['Quantity']}*${item['price']} =${item_total:.2f}")

print(f"\ntotal bill: ${total_cost:.2f}")
