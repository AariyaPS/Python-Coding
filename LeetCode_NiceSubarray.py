'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''

print("Enter the no. of elements in an array:")
n=int(input())

nums=[]

for i in range(n):
    print("Enter the element in an array:")
    ele =int(input())
    nums.append(ele)
    
print("Enter the value of k")
k=int(input())
    
def numberOfSubarrays(nums, k):
        curr_sum = 0
        subarrays = 0
        prefix_sum = {curr_sum: 1}

        for i in range(len(nums)):
            curr_sum += nums[i] % 2
            # Find subarrays with sum k ending at i
            if curr_sum - k in prefix_sum:
                subarrays = subarrays + prefix_sum[curr_sum - k]
            # Increment the current prefix sum in hashmap
            prefix_sum[curr_sum] = prefix_sum.get(curr_sum, 0) + 1

        print(subarrays)
        
numberOfSubarrays(nums,k)