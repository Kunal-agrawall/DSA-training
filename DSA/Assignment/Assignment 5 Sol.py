# Q1
def sort_by_1st(a):
    for i in range(len(a)-1):
        for j in range(len(a)-i-1):
            if a[j][0] > a[j+1][0]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

# Q2
def sort_by_sum(a):
    for i in range(len(a)-1):
        for j in range(len(a)-i-1):
            if a[j][0]+a[j][0] > a[j+1][0]+a[j+1][1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

# Q3
def sort_by_1st_rev(a):
    for i in range(len(a)-1):
        for j in range(len(a)-i-1):
            if a[j][0] < a[j+1][0]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

# Q4
# Not Yet

# Q5
def sort_by_len(a):
    for i in range(len(a)-1):
        for j in range(len(a)-i-1):
            if len(a[j]) > len(a[j+1]):
                a[j], a[j+1] = a[j+1], a[j]
    return a
    
# Q6
def sort_by_1st_then_2nd(a):
    for i in range(len(a)-1):
        for j in range(len(a)-i-1):
            if a[j][0] > a[j+1][0]:
                a[j], a[j+1] = a[j+1], a[j]
            elif a[j][0] == a[j+1][0]:
                if a[j][1] > a[j+1][1]:
                    a[j], a[j+1] = a[j+1], a[j]
    return a

# Q7
def find_maxSum_tuple(a):
    m = a[0][0]+a[0][1]
    index = 0
    for i in range(1, len(a)):
        if m < a[i][0]+a[i][1]:
            m = a[i][0]+a[i][1]
            index = i
    return a[index]

# Q8
def find_min_by_1st(a):
    m = a[0][0]
    index = 0
    for i in range(1, len(a)):
        if m > a[i][0]:
            m = a[i][0]
            index = i
    return a[index]
    
# Q9
def sort_by_2nd_then_1st(a):
    for i in range(len(a)-1):
        for j in range(len(a)-i-1):
            if a[j][1] > a[j+1][1]:
                a[j], a[j+1] = a[j+1], a[j]
            elif a[j][1] == a[j+1][1]:
                if a[j][0] > a[j+1][0]:
                    a[j], a[j+1] = a[j+1], a[j]
    return a
    
# Q10
# Difference b/w Q2 & Q10

a = [(1, 2), (2, 3), (3, 1), (4, 2)]
print(sort_by_2nd_then_1st(a))