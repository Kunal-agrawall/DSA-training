
# How to print expression without print()
def add(a,b):
    return a+b

# Lambda
sum = lambda a,b : a+b
print(sum(1,2))


# 
def co(str):
    a = []
    for i in range(len(str)-2):
        a.append(str[i:i+3])
    if a.count('cat') == a.count('hat'):
        return True
    else:
        return False

str = "catinahat"
c = co(str)
print(c)