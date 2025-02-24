model = ["Hatchback", "Saloon", "Estate"]
price = [535000, 495000, 625000]

opt_extra = ["Luxury Seats Set", 
                              "Satellite Navigation",
                              "Parking Sensors",
                              "Bluetooth Connectivity",
                              "Sound System"]
opt_price = [45000, 5500, 10000, 350, 1000]


print("Are you Inetrested in Buying Car :")
print("\t-- Press 1 for Yes")
print("\t-- Press 2 for No")
ask = int(input("\tEnter : "))

if ask == 1:
        a = " "
        print("\nWhich model are you Interested in to buy?\n")
        print(f"\t{a*10}Model{a*10}Price")
        for i in range(len(model)):
            print(f"\t{i+1}{a*9}{model[i]:15}Rs.{price[i]}")
        
        car_m = int(input("\tEnter : "))
        p1 = None
        if car_m == 1:
            p1 = price[0]
        elif car_m == 2:
            p1 = price[1]
        elif car_m == 3:
            p1 = price[2]
        else:
            print("Wrong Input")
            exit()
        
        print("\nWhich add-on feature are you interested to use?")    
        print(f"\t{a*10}Option{a*19}Price")
        for i in range(len(opt_extra)):
            print(f"\t{i+1}{a*9}{opt_extra[i]:25}Rs.{opt_price[i]}")
            
        car_i = int(input("\tEnter : "))
        p2 = None
        if car_i == 1:
            p2 = opt_price[0]
        elif car_i == 2:
            p2 = opt_price[1]
        elif car_i == 3:
            p2 = opt_price[2]
        elif car_i == 4:
            p2 = opt_price[3]
        elif car_i == 5:
            p2 = opt_price[4]
        else:
            print("Wrong Input")
            exit()
        
        print("\nAre you an existing member?")
        print("\t-- Press 1 for Yes (Eligible for 10% discount)")
        print("\t-- Press 2 for No  (Eligible for 5% discount)")
        disc = int(input("\tEnter : "))
        
        p3 = None
        if disc == 1:
            disc = 10
            p3 = (p1+p2)*0.90
        elif disc == 2:
            disc = 5
            p3 = (p1+p2)*0.95
            
        print("\nDo you have an old car for exchange?")
        print("\t-- Press 1 for Yes")
        print("\t-- Press 2 for No")
        car_o = int(input("\tEnter : "))
        
        if car_o == 1:
            car_op = int(input("\tEnter Old Car Price : "))
            if 10000 <= car_op and car_op <= 100000:
                p3 -= car_op
            else:
                print("\tWe can't reduce new car price.")
        elif car_o == 2:
            print("No Worries.")
        else:
            print("Wrong Input")
            exit()
        
        print("\nPlease enter your payment option.")
        print("\tPress 1 for Full Amount at 1% cashback")
        print("\tPress 2 for Equal monthly payments for 4 years at no charge")
        print("\tPress 3 for Equal monthly payments over a period of 7 years at a surcharge of 5% on total price of the car")
        pay = int(input("\tEnter : "))
        
        install = 0
        if pay == 1:
            install = p3*0.01
        elif pay == 2:
            t = 48
            install = p3/t
        elif pay == 3:
            t = 84
            install = p3/t + p1*0.05
 
        print("\nYour Purchase Details:")
        print(f"Car Model    : {model[car_m-1]}")
        print(f"Car Add-On   : {opt_extra[car_i-1]}")
        print(f"Have old car : ", end="")
        print("Yes") if car_o==1 else print("No")
        print(f"Discount     : {disc}%")
        print(f"Total        : {p3}")
        print(f"Installment  : ", end='')
        if pay == 1:
            print(f"One Time Payment with Rs.{install} cashback.")
        elif pay == 2:
            print("Rs.{install}/month for 48 months.")
        else:
            print("Rs.{install}/month for 84 months with 5% sub-charge.")
        
            
else:
    print("Thank You for your Time.")