def get_max(arr):
    """
    Returns max element in arr using divide and conquer
    :param arr:
    :return:
    """

    if len(arr) == 0:
        return -1

    if len(arr) == 1:
        return arr[0]

    mid = len(arr)//2
    return max(get_max(arr[:mid]), get_max(arr[mid:]))


if __name__ == '__main__':
    print(get_max([3, 1, 12, 7, -1, 5]))