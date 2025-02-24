a = ['Jatin', 'Jatin', 'Sharma']
for i in set(a):
    b = a.count(i)
    print(f'Freq of {i} = {b}')


# Product of max 2
a = [10,20,30,40,50,60]
a = set(a)
lar1 = max(a)
a.remove(lar1)
lar2 = max(a)
a.add(lar1)
print(f'{lar1} x {lar2} = {lar1*lar2}')


# Unique Combination
a = [1,2,3]
b = {}

for i in a:
    for j in a:
        for k in a:
            b.update({i,j,k})
