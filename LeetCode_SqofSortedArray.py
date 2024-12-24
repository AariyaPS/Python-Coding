


def sortedSquares(nums):

    l = len(nums)-1
    left = 0
    right = len(nums)-1
    ans = [0]*len(nums)


    while left<=right:

        if abs(nums[left]) > abs(nums[right]):
            ans[l] = nums[left]*nums[left]
            left += 1
            l -=1

        else:
            ans[l] = nums[right]*nums[right]
            right -= 1
            l -= 1

    return ans
    
    
a = [-7,-3,2,3,11]
b = sortedSquares(a)

for i in range(len(b)):
    print(b[i],end="\n")