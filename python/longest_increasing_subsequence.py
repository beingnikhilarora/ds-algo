def lis(arr):
    table = [1] * len(arr)
    max_len = -1

    for i in range(len(arr)):
        for j in range(i):
            if arr[i] > arr[j] and table[i] < table[j] + 1:
                table[i] = table[j]+1

    for i in range(len(arr)):
        max_len = table[i] if max_len < table[i] else max_len

    return max_len


if __name__ == '__main__':
    arr = [50, 3, 10, 7, 40, 80]
    print(lis(arr))


