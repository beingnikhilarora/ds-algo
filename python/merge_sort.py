def merge(arr, left, right):
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        k += 1
        i += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


def merge_sort(arr):
    size = len(arr)

    if size<=1:
        return
    mid = size//2

    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    merge(arr, left, right)


if __name__ == '__main__':
    arr = [3,2,1,1000,-1]
    merge_sort(arr)
    print(arr)