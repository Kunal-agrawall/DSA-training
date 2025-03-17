import random
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Function to generate a random invoice number
def generate_invoice_number():
    return f"INV{random.randint(1000, 9999)}"

# Function to generate the invoice PDF
def generate_pdf(invoice_number, customer_name, customer_email, customer_contact, order_items, discount, total_price, emi_option):
    pdf_filename = f"Invoice_{invoice_number}.pdf"
    c = canvas.Canvas(pdf_filename, pagesize=letter)
    
    # Title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(200, 750, f"Invoice Number: {invoice_number}")
    
    # Customer Information
    c.setFont("Helvetica", 12)
    c.drawString(30, 730, f"Customer Name: {customer_name}")
    c.drawString(30, 715, f"Customer Email: {customer_email}")
    c.drawString(30, 700, f"Customer Contact: {customer_contact}")
    
    # Order List
    c.setFont("Helvetica-Bold", 14)
    c.drawString(30, 670, "Order List:")
    
    y_position = 650
    for item in order_items:
        c.setFont("Helvetica", 12)
        c.drawString(30, y_position, f"{item['name']} - Rs. {item['price']}")
        y_position -= 15  # Move down for the next item
    
    # Discount Applied and Total
    c.setFont("Helvetica-Bold", 12)
    c.drawString(30, y_position - 20, f"Discount Applied: Rs. {discount}")
    c.drawString(30, y_position - 35, f"Total Amount After Discount: Rs. {total_price}")
    
    # EMI Option
    emi_text = "EMI Option Selected: Yes" if emi_option else "EMI Option Selected: No"
    c.drawString(30, y_position - 50, emi_text)
    
    # Footer
    c.setFont("Helvetica", 10)
    c.drawString(30, y_position - 80, "Thank you for visiting Our Restaurant!")
    
    # Save the PDF
    c.save()

# Main order logic
print("WELCOME TO OUR RESTAURANT !!!")
print("Are you interested to eat different items?")
print("Type 1 for: 'Yes' and type 2 for 'No'")

choice = int(input("Enter number here: "))
if choice != 1:
    print("Thank you for visiting Our Restaurant!")
    exit()

# Collect customer details
customer_name = input("\nEnter your name: ")
customer_email = input("Enter your email: ")
customer_contact = input("Enter your contact number: ")

# Menu for food items
print("\nWhich item would you like to order?")
print("item price")
print("1. Pizza  Rs. 499")
print("2. Burger     Rs. 99")
print("3. Spring Roll    Rs. 599")
print("4. Momos    Rs. 599")
print("5. Veg Thali    Rs. 999")
print("Type 1 for 'Pizza', 2 for 'Burger', and 3 for 'Spring Roll', 4 for 'Momos', 5 for 'Veg Thali'.")

order_items = []
total_price = 0

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

order_items.append({"name": item_name, "price": item_price})
total_price += item_price
print(f"Selected item: {item_name}, Price: Rs. {item_price}")

# Optional add-ons
print("\nWhich dish would you like to choose from the menu and can select optional add-ons?")
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

order_items.append({"name": optional_name, "price": optional_price})
total_price += optional_price
print(f"Selected Add-on: {optional_name}, Price: Rs. {optional_price}")
print(f"Total Price: Rs. {total_price}")

# Payment method
print("\nChoose payment method:")
print("1. Full Payment for 5% cashback")
print("2. Installment Payment")
payment_method = int(input("Enter payment method number here: "))

discount = 0
emi_option = False
if payment_method == 1:
    cashback = total_price * 0.05
    total_price -= cashback
    discount = cashback
    print("You get a 5% cashback!")
    print(f"Total Price after cashback: Rs. {total_price}")

    print("\nAre you a repeat customer? Type 1 for 'Yes' and type 2 for 'No'")
    repeat_customer = int(input("Enter number here: "))
    if repeat_customer == 1:
        total_price *= 0.95
        discount += total_price * 0.05
        print("You get a 5% discount!")
        print(f"Total Price after discount: Rs. {total_price}")
        print("Thank you for visiting Our Restaurant!")
elif payment_method == 2:
    installment = int(input("Enter number of installments here: "))
    monthly_payment = total_price / installment
    print(f"Total Amount to be paid: Rs. {total_price}")
    print(f"Monthly Payment: Rs. {monthly_payment}")
    emi_option = True
    print("Thank you for visiting Our Restaurant!")
else:
    emi_option = False

# Generate invoice number
invoice_number = generate_invoice_number()

# Generate the invoice PDF
generate_pdf(invoice_number, customer_name, customer_email, customer_contact, order_items, discount, total_price, emi_option)

print(f"Invoice has been generated as 'Invoice_{invoice_number}.pdf'")
