def knapsack(wt, val, capacity):
    K = [[0 for _ in range(capacity+1)] for _ in range(len(wt)+1)]

    for i in range(1, len(wt)+1):
        for j in range(1, capacity+1):
            if j >= wt[i-1]:
                K[i][j] = max(K[i-1][j-wt[i-1]]+val[i-1], K[i-1][j])
            else:
                K[i][j] = K[i-1][j]

    return K[len(wt)][capacity]


if __name__ == '__main__':
    wt = [1, 2, 3]
    val = [6, 10, 12]
    capacity = 5
    ans = knapsack(wt, val, capacity)
    print(ans)
