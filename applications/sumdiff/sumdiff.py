"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def Sum(x,y):
    return f(x) + f(y)

def f(x):
    return x * 4 + 6

def Dif(x,y):
    return f(y) - f(x)

sums = {}
combos = []

def all_combos(set):
    #find the sum values for all combos
    #
    for i in range(0,len(set)):
        for j in range(i,len(set)):
            if Sum(set[i], set[j]) not in sums:
                sums[Sum(set[i],set[j])] = []
                sums[Sum(set[i],set[j])].append([set[i],set[j]])
            else:
                sums[Sum(set[i],set[j])].append([set[i],set[j]])
    for i in range(0, len(set)):
        for j in range(i, len(set)):
            if Dif(set[i], set[j]) in sums:
                for pair in sums[Dif(set[i], set[j])]:
                    combos.append([pair[0], pair[1], set[j], set[i] ])
    return combos


# Your code here

