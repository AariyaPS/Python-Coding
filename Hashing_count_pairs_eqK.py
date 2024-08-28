"""Count All ((i,j) pairs such that b[i] - b[j] == k (count of such pairs.) [i<j] """

from collections import defaultdict


def count_pairs_optimized(b, k):
    count = 0
    freq_map = defaultdict(int)
    for num in b:
        target = num + k
        count += freq_map[target]
        freq_map[num] += 1
    return count


def main():
    b = [1, 5, 3, 4, 2]
    k = 2
    print("Count of pairs:", count_pairs_optimized(b, k))


if __name__ == "__main__":
    main()