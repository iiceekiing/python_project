students = {
    "John": 85,
    "Grace": 58,
    "Michael": 47,
    "Sarah": 91,
    "David": 73,
}

for name, score in students.items():
    if score >= 90:
        classification = "Excellent"
    elif score >= 70:
        classification = "Good"
    elif score >= 50:
        classification = "Fair"
    else:
        classification = "Fail"

    print(f"{name} scored {score} and is classified as '{classification}'")



prices = {
    "Apple": 300,
    "Banana": 150,
    "Orange": 250,
    "Pineapple": 500,
}

for item, price in prices.items():
    status = "Expensive" if price >= 300 else "Affordable"
    print(f"Item: {item}, Price: ₦{price}, Status: {status}")




students = {
    "Zainab": 78,
    "Kelechi": 45,
    "Bashir": 89,
    "Ada": 62,
    "Tunde": 33
}

for name, score in students.items():
    remark = "Pass" if score >= 50 else "Fail"
    print(f"Name: {name}, Score: {score}, Remark: {remark}")






inventory = {
    "apple": 25,
    "banana": 0,
    "orange": 10,
    "mango": 0,
    "pineapple": 7
}

for fruit, quantity in inventory.items():
    if quantity > 0:
        print(f"Item: {fruit} is in stock: {quantity}")
    else:
        print(f"Item: {fruit} is OUT OF STOCK!")

