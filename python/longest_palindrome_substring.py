def longestPalindrome(s: str) -> str:
    table = [[False for _ in range(len(s))] for _ in range(len(s))]
    maxLen = -1
    start = -1

    # for string of length 1
    for i in range(len(s)):
        table[i][i] = True
        maxLen = 1
        start = i

    # for string of length 2
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            table[i][i + 1] = True
            maxLen = 2
            start = i

    # for string of length 3
    for k in range(3, len(s) + 1):
        for i in range(len(s) - k + 1):
            j = i + k - 1

            if s[i] == s[j] and table[i + 1][j - 1]:
                table[i][j] = True
                if maxLen < k:
                    maxLen = k
                    start = i

    return s[start:start + maxLen]