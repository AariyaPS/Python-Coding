def is_subsequence(A, B):
    global p
    n = len(A)
    m = len(B)
    i, j, count = 0, 0, 0
    
    while i < m and j < n:
        if A[j] == B[i]:
            if count == 0:
                p = j
            i += 1
            j += 1
            count += 1
        else:
            j += 1
    
    return count == m

def main():
    global p
    t = int(input())
    for _ in range(t):
        a = input()
        b = input()
        answer = -1
        for i in range(1, len(b)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                r = b
                r = r[:i] + c + r[i+1:]
                p = -1
                if is_subsequence(a, r):
                    answer = p + 1
        print(answer)

if __name__ == "__main__":
    p = -1
    main()