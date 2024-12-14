
print("Enter the total no. of lamps:")
n=int(input())


a=[0]*1000

print("Enter the number of ranges:")
q=int(input())


for i in range(q):
    
    print("Enter the lower bound of range:")
    l=int(input())
    
    print("Enter the upeer bound of range:")
    r=int(input())
    
    a[l]=a[l]+1
    
    if r+1 <=n:
        a[r+1]=a[r+1]-1
        

for i in range(1,n+1):
    a[i]=a[i]+a[i-1]
    
    
print("Enter the queries:")
p=int(input())


for i in range(p):
    
    print("Enter the number of the lamp :")
    y=int(input())
    
    print("Number of times the lamp :",y," will lit up ",a[y]," times.")