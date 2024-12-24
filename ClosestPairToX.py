'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''

# Initialize a SortedList which allows us to maintain a sorted collection of numbers
def printClosest (arr, brr, n, m, x) : 
        #code here
    v = 0
    first = 0
    second = 0
    bv = 100000000
    j = m - 1
    i = 0
    kk8 = 0
    kk5 = 0
    g5 = 0
    g8 = 0
    while i < n and j >= 0:
        if arr[i] + brr[j] <= x:
            sum_val = arr[i] + brr[j]
            if sum_val > v:
                v = sum_val
                first = arr[i]
                second = brr[j]
                g5 = 1
            i = i + 1
        else:
            if arr[i] + brr[j] < bv:
                bv = arr[i] + brr[j]
                kk5 = arr[i]
                kk8 = brr[j]
                g8 = 1
            j = j - 1

    r = []
    dv = 100000000
    if g5 == 1:
        dv = abs(x - v)
        if g8 == 1:
            dy = abs(x - bv)
            if dy < dv:
                r.append(kk5)
                r.append(kk8)
            else:
                r.append(first)
                r.append(second)
        else:
            r.append(first)
            r.append(second)
    else:
        r.append(kk5)
        r.append(kk8)

    return r
    
    
arr = [1, 4, 5, 7]
brr = [10, 20, 30, 40]
x = 30
n = 4
m = 4

a = printClosest(arr,brr,n,m,x)

for i in a:
    print(i,end="\n")