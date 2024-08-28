def count_noOf_pairs():
    arr = [1, 2, 3, 4, 5]
    k = 5
    hmap = {}
    count = 0
    for i in range(len(arr)):
        comp = k - arr[i]
        if comp in hmap.keys():
            count += hmap[comp]

        if arr[i] in hmap.keys():
            hmap[arr[i]] += 1

        else:
            hmap[arr[i]] = 1

    print("Count = ", count)


count_noOf_pairs()
