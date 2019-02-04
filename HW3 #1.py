from math import sqrt

def is_pent(n):
    ans = any((x*((3*x)-1))/2 == n for x in range(int((n+1))))
    return ans

for i in range(100):
    if is_pent(i):
        print(str(i) + " is pentagonal")
