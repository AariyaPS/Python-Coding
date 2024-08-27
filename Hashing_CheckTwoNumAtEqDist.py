def Hashing_CheckTwoNumAtEqDist(nums, k):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if j <= i + k and nums[i] == nums[j]:
                return True
    return False


def main():
    nums = [1, 1, 3, 1, 2, 3]
    k = 2
    if Hashing_CheckTwoNumAtEqDist(nums, k):
        print("There are two equal numbers within distance", k)
    else:
        print("No two equal numbers found within distance", k)


if __name__ == "__main__":
    main()
