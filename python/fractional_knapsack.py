def compare_ratio(ratio):
    return ratio[0]


def fractional_knapsack(wt, val, capacity):
    """
    :param wt: (list) weights of items
    :param val: (list) values of items
    :param capacity: (int) capacity of knapsack
    :return: (int) maximum amount that can be filled
    """

    ratio = [(val[i]/wt[i], wt[i]) for i in range(len(wt))]
    max_value = 0
    filled = 0

    for ratio in sorted(ratio, key=compare_ratio, reverse=True):
        if filled + ratio[1] < capacity:
            max_value += ratio[0] * ratio[1]
            filled += ratio[1]
        else:
            max_value += ratio[0] * (capacity-filled)
            break

    return max_value


if __name__ == '__main__':
    print(fractional_knapsack([10, 20, 30], [60, 100, 120], 50))
