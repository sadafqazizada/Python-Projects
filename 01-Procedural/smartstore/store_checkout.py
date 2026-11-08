
print("Welcome to the Smart Store!")
print("1. Notebook - 70 AFN")
print("2. Pen Pack - 40 AFN")
print("3. USB Flash Drive - 250 AFN")

product = int(input("What product do you want?"))
price = 0
if product == 1:
    price = 70
elif product == 2:
    price = 40
elif product == 3:
    price = 250

quantity = int(input("What quantity do you want?"))
subtotal = quantity * price

member = input("Are you a member (yes/no?): ")
discount = 0
if subtotal > 300 and member == "yes":
    discount = subtotal * 0.10

final_total = subtotal - discount

money = float(input("How much money do you have?"))
if money >= final_total:
    print("Purchase successful!")

    remaining = money - final_total
    print("Remaining money: ", remaining, "AFN")

else:
    print("Purchase unsuccessful!")

    need = final_total - money
    print("Need: ", need, "AFN")

print("--------RECEIPT--------")
print("Product : ", product)
print("Quantity : ", quantity)
print("Subtotal: ", subtotal, "AFN")
print("Discount: ", discount, "AFN")
print("final total: ", final_total, "AFN")
