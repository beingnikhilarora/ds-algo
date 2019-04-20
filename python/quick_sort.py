def partition(arr, lo, hi):
    pivot = hi

    p = lo
    for i in range(lo, hi):
        if arr[i] <= arr[pivot]:
            arr[i], arr[p] = arr[p], arr[i]
            p += 1
    arr[p],arr[pivot] = arr[pivot],arr[p]
    return p


def quick_sort(arr, lo, hi):
    if lo >= hi:
        return
    p = partition(arr, lo, hi)

    quick_sort(arr, lo, p-1)
    quick_sort(arr, p+1, hi)


if __name__ == '__main__':
    arr = [3, 2, 5, -1, 1, 7, -1, 100, 19]
    quick_sort(arr, 0, len(arr)-1)
    print(arr)