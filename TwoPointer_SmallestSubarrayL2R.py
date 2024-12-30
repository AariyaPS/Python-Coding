def main():
    n = int(input())  # size of array b[]
    b = [0] * (n + 1)  # array b[n+1]
    for i in range(1, n + 1):
        b[i] = int(input())
 
    l, r = map(int, input().split())  # given limits
 
    u = float('inf')
    i, j = 1, 1
    k = {}
 
    while i <= n and j <= n:
        # [i.....j]
        if l <= b[j] <= r:
            k[b[j]] = k.get(b[j], 0) + 1
 
        if len(k) == abs(r - l + 1):
            # [i.....j] is a valid subarray 
            length = abs(j - i + 1)
            u = min(length, u)
 
            if l <= b[i] <= r:
                k[b[i]] = k.get(b[i]) - 1
                if k[b[i]] == 0:
                    del k[b[i]]
 
            i = i + 1  # [i+1]........j]
 
            if l <= b[j] <= r:
                k[b[j]] = k.get(b[j]) - 1  # removing j for temporary basis!
                if k[b[j]] == 0:
                    del k[b[j]]
                # [i+1].....j-1]
        else:
            j = j + 1
 
    if u == float('inf'):
        print(-1)
    else:
        print(u)
 
if __name__ == "__main__":
    main()