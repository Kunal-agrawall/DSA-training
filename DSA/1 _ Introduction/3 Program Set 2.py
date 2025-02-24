a = 5
if a<0:
    print("It's Negative")
else:
    print("It's Positive")


print("It's Odd") if a%2 else print("It's Even")



# For 2 Variables
x, y = 1,2
print("x > y") if x>y else print("x < y") if x<y else print("x = y")



# For 3 Variables
def check3(x,y,z):
    # To check equal number 
    if x==y==z:
        print("All are Equal")

    # To check Greater number
    if x>=y and x>=z:
        print("x is Greater")
    elif y>=x and y>=z:
        print("y is Greater")
    else:
        print("z is Greater")

    # To check Smaller number
    if x<=y and x<=z:
        print("x is Smaller")
    elif y<=x and y<=z:
        print("y is Smaller")
    else:
        print("z is Smaller")

x = int(input("Enter x : "))
y = int(input("Enter y : "))
z = int(input("Enter z : "))
check3(x,y,z)


# Leap Year
a = 1900
if a%100==0 and a%400==0:
    print("Leap Year")
elif a%4==0 and a%100!=0:
    print("Leap Year")
else:
    print("Not a Leap Year")


# For Loop
n = 10
for i in range(0,n+1):
    print(f"{i} is odd") if i%2 else print(f"{i} is even")

# Table of 2
i=2
for j in range(1,10+1):
        print(f'{i}x{j} = {i*j}')


for i in range(2,20+1):
    print(f'Table of {i}->')
    for j in range(1,10+1):
        print(f'{i}x{j} = {i*j}')
    print()

# Digit Sum
a = 187
b = 0
while a:
    b += a%10
    a = a//10
print(b)


# Armstrong
a = b = org = 153
count = 0
while b:
    count += 1
    b = b//10

while a:
    b += pow(a%10,count)
    a = a//10

if org == b:
    print(f"{b} is Armstrong.")
else:
    print(f"{b} is not Armstrong")