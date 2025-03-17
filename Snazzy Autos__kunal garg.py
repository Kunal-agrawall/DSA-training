model = ["Hatchback", "Saloon", "Estate"]
price = [535000, 495000, 625000]

extra_option = ["Luxury Seats Set", 
                              "Satellite Navigation",
                              "Parking Sensors",
                              "Bluetooth Connectivity",
                              "Sound System"]
price_option = [45000, 5500, 10000, 350, 1000]


print("Are you Inetrested in Buying a Car :")
print("\t-- Press 1 for Yes")
print("\t-- Press 2 for No")
option = int(input("\tEnter : "))

if option == 1:
        a = " "
        print("\nWhich model are you Interested in to buy?\n")
        print(f"\t{a*10}Model{a*10}Price")
        for i in range(len(model)):
            print(f"\t{i+1}{a*9}{model[i]:15}Rs.{price[i]}")
        
        model_of_car = int(input("\tEnter : "))
        p1 = None
        if model_of_car == 1:
            p1 = price[0]
        elif model_of_car == 2:
            p1 = price[1]
        elif model_of_car == 3:
            p1 = price[2]
        else:
            print("Incorrect Input")
            exit()
        
        print("\nWhich add-on feature are you interested to use?")    
        print(f"\t{a*10}Option{a*19}Price")
        for i in range(len(extra_option)):
            print(f"\t{i+1}{a*9}{extra_option[i]:25}Rs.{price_option[i]}")
            
        car_i = int(input("\tEnter : "))
        p2 = None
        if car_i == 1:
            p2 = price_option[0]
        elif car_i == 2:
            p2 = price_option[1]
        elif car_i == 3:
            p2 = price_option[2]
        elif car_i == 4:
            p2 = price_option[3]
        elif car_i == 5:
            p2 = price_option[4]
        else:
            print("Incorrect Input")
            exit()
        
        print("\nAre you an existing member?")
        print("\t-- Press 1 for Yes (Eligible for 10% discount)")
        print("\t-- Press 2 for No  (Eligible for 5% discount)")
        disc = int(input("Enter : "))
        
        p3 = None
        if disc == 1:
            disc = 10
            p3 = (p1+p2)*0.90
        elif disc == 2:
            disc = 5
            p3 = (p1+p2)*0.95
            
        print("\nDo you have any old car for exchange?")
        print("\t-- Press 1 for Yes")
        print("\t-- Press 2 for No")
        old_car = int(input("\tEnter : "))
        
        if old_car == 1:
            old_car_price = int(input("\tEnter Old Car Price : "))
            if 10000 <= old_car_price and old_car_price <= 100000:
                p3 -= old_car_price
            else:
                print("\tWe can not reduce new car price.")
        elif old_car == 2:
            print("Not a big deal.")
        else:
            print("Incorrect Input")
            exit()
        
        print("\nPlease enter your payment way.")
        print("\tPress 1 for Full Amount at 1% cashback")
        print("\tPress 2 for Equal monthly payments for 4 years at no charge")
        print("\tPress 3 for Equal monthly payments over a period of 7 years at a surcharge of 5% on total price of the car")
        payment = int(input("\tEnter : "))
        
        install = 0
        if payment == 1:
            install = p3*0.01
        elif payment == 2:
            t = 48
            install = p3/t
        elif payment == 3:
            t = 84
            install = p3/t + p1*0.05
 
        print("\nYour Purchase Details:")
        print(f"Car Model    : {model[model_of_car-1]}")
        print(f"Car Add-On   : {extra_option[car_i-1]}")
        print(f"Have old car : ", end="")
        print("Yes") if old_car==1 else print("No")
        print(f"Discount     : {disc}%")
        print(f"Total        : {p3}")
        print(f"Installment  : ", end='')
        if payment == 1:
            print(f"One Time Payment with Rs.{install} cashback.")
        elif payment == 2:
            print("Rs.{install}/month for 48 months.")
        else:
            print("Rs.{install}/month for 84 months with 5% sub-charge.")
        
            
else:
    print("Thank You for your Time. This is Kunal Garg, your service provider.")