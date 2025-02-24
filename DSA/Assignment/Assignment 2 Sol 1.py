# Q1
a = '''Twinkle, twinke, little star, How i wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinke little star, How i wonder what you are'''
b = [chr(i) for i in range(65, 91)]
count, flag0, flag3 = 0, 0, 0

for i in a:
    if flag0 == 0:
        print(i, end='')
        flag0 = 1
        count += 1
    elif i in b:
        if count == 4:
            count = 0
        if flag3 == 0 and count == 3:
            print()
            print('\t'*(count-1), end='')
            print(i, end='')
            flag3 = 1
            count += 1
            continue
        print()
        print('\t'*count, end='')
        print(i, end='')
        count += 1
    else:
        print(i, end='')


# Q2
from datetime import datetime
date = datetime.now()
print(date.strftime("%Y-%m-%d %H:%M:%S"))


# Q3
CArea = lambda r : 22/7*r*r
ans = CArea(1.1)
print(f'Area : {ans}')


# Q4
def MyInput():
    first = input("Enter First Name : ")
    last = input("Enter Last Name : ")
    return first + " " + last

def RName():
    name = MyInput()
    for i in name[::-1]:
        if i == " ":
            continue
        print(i, end=" ")

RName()


# Q5
a = ['Red','Green','White','Black']
print(f"First : {a[0]}")
print(f"Last  : {a[-1]}")


# Q6
a = '''A string that you "don't" have to escape
This
is a ....... multi-line
heredoc string -------> example'''
print(a)


# Q7
def Sum(a,b,c):
    if a==b and b==c:
        return 9*a
    return a+b+c
ans = Sum(1,2,3)
print(f'Sum : {ans}')