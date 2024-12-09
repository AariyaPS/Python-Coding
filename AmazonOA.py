'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''

from collections import defaultdict

print("Enter string S")
s=(input())
print("Enter string T")
t=(input())


mp1=defaultdict(int)
mp2=defaultdict(int)


for char in s:
    mp1[char] += 1

for char in t:
    mp2[char] += 1
    
cnt = float('inf')

for char in t:
    if char not in mp1:
        # it means char is not present in s hence we will not get any subset
        exit(0)

    val = mp1[char] // mp2[char]
    cnt = min(cnt, val)

print(cnt)

