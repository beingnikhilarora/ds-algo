def binary_search(arr, val):
    """
    perform binary search on array arr and return True or False if val is found.
    :param arr:
    :param val:
    :return: (Boolean) returns True if val is found else False
    """

    size = len(arr)

    if size <= 0:
        return False

    lo = 0
    hi = size-1

    while lo <= hi:
        mid = lo + (hi-lo)//2

        if arr[mid] == val:
            return True

        elif val < arr[mid]:
            hi = mid-1

        else:
            lo = mid+1

    return False


if __name__ == '__main__':
    print(binary_search([1, 2, 3, 4, 5], 4))
    print(binary_search([2, 4, 67, 89], 100))
    print(binary_search([],  8))
    print(binary_search([1], 1))