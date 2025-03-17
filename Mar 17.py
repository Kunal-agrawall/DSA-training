# Restaurant Order System

print("WELCOME TO OUR RESTAURANT !!!")
print("Are you interested to eat different items ")
print("Type 1 for: 'Yes' and type 2 for 'No'")

choice = int(input(" enter number here: "))
if choice != 1:
    print("Thank you for visiting Our Restaurant!")
    exit()

print("\nWhich item You Order?")
print("item price")
print("1. Pizza  Rs. 499")
print("2. Burger     Rs. 99")
print("3. Spring Roll    Rs. 599")
print("4. Momos    Rs. 599")
print("5. Veg Thali    Rs. 999")
print("Type 1 for 'Pizza', 2 for 'Burger', and 3 for 'Spring Roll', 4 for 'Momos, 5 for 'Veg Thali'.")
choices=[]
total_price=0
item = int(input("Enter item No. from the menu here: "))
if item == 1:
    item_name = "Pizza"
    item_price = 499

elif item == 2:
    item_name = "Burger"
    item_price = 99

elif item == 3:
    item_name = "Spring Roll"
    item_price = 599

elif item == 4:
    item_name = "Momos"
    item_price = 599

elif item == 5:
    item_name = "Veg Thali"
    item_price = 999
else:
    print("Invalid choice. Exiting.")
    exit()

choices.append(item_name)
total_price += item_price
print(f"Selected item: {item_name}, Price: Rs. {item_price}")

print("\nWhich dish choose from the menu and can select optional add-ons")
print("OPTIONAL EXTRA              PRICE")
print("1. Cold Drink         Rs 199")
print("2. Ice Cream         Rs 150")
print("3. Energy Drink             Rs 199")
print("4. Rosogulla       Rs 99")
print("5. Gulab Jamun                 Rs 149")
print("Type 1 for 'Cold Drink', 2 for 'Ice Cream',")
print("3 for 'Energy Drink', 4 for 'Rosogulla', 5 for 'Gulab Jamun', and 6 for 'none'.")

optional = int(input("Enter option no. here: "))
optional_name = "None"
optional_price = 0

if optional == 1:
    optional_name = "Cold Drink"
    optional_price = 199

elif optional == 2:
    optional_name = "Ice cream"
    optional_price = 150

elif optional == 3:
    optional_name = "Energy Drink"
    optional_price = 299

elif optional == 4:
    optional_name = "Rosogulla"
    optional_price = 99

elif optional == 5:
    optional_name = "Gulab Jamun"
    optional_price = 149

elif optional == 6:
    optional_name = "None"
    optional_price = 0
else:
    print("Invalid choice. Exiting.")
    exit()

choices.append(optional_name)
total_price += optional_price
print(f"Selected Add-on: {optional_name}, Price: Rs. {optional_price}")
print(f"Total Price: Rs. {total_price}")

print("\nChoose payment method")
print("1. Full Payment for 5% cashback")
print("2. Installment Payment")
payment_method = int(input("Enter payment method number here: "))

if payment_method == 1:
        cashback = total_price * 0.05
        total_price -= cashback
        print("You get a 5% cashback!")
        print(f"Total Price after cashback: Rs. {total_price}")
        print("Thank you for visiting Our Restaurant!")
        print("\nAre you a repeat customer? Type 1 for 'Yes' and type 2 for 'No'")
        
        repeat_customer = int(input("Enter number here: "))
        if repeat_customer == 1:
            total_price *= 0.95
            print("You get a 5% discount!")
            print(f"Total Price after discount: Rs. {total_price}")
            print("Thank you for visiting Our Restaurant!")
            if total_price > 1000:
                print("Congratulations! You qualify for a special offer!")
                print("You get a free dessert!")
                print(f"Total Price after special offer: Rs. {total_price}")
                print("Thank you for visiting Our Restaurant!")
                exit()
        elif repeat_customer == 2:
            print(f"Total Price after cashback: Rs. {total_price}")
            if total_price > 1000:
                print("Congratulations! You qualify for a special offer!")
                print("You get a free dessert!")
                print("Thank you for visiting Our Restaurant!")
                exit()
                 
elif payment_method == 2:
        installment = int(input("Enter number of installments here: "))
        monthly_payment = total_price / installment
        print(f"Total Amount to be paid: Rs. {total_price}")
        print(f"Monthly Payment: Rs. {monthly_payment}")
        print("Thank you for visiting Our Restaurant!")
        exit()
