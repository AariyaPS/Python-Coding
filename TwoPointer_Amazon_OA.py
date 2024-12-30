n = int(input())
b = list(map(int, input().split()))
 
def calculate(k):
    count = 0
    j = n - 1
    for i in range(n):
        d = b[j] + b[i]  
        while d > k and i != j:
            j -= 1
            d = b[j] + b[i]
        if i == j:
            break
        count += (j - i)
    return count
 
l, r = map(int, input().split())
b.sort()
print(calculate(r) - calculate(l - 1))