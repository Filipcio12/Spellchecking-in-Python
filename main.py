def main():
    word1 = "car"
    word2 = "apple"
    print(f"levensthein:    {levensthein(word1, word2)}")
    print(f"hamming:        {hamming(word1, word2)}")
    print(f"indel:          {indel(word1, word2)}")


def indel(word1, word2):
    """Indel is a variation of levensthein that
    only allows insertions and deletions but no
    replacements"""
    # Table creation
    a, b = len(word1) + 1, len(word2) + 1
    table = [[0 for _ in range(a)]
             for _ in range(b)]
    for x in range(1, a):
        table[0][x] = x
    for y in range(1, b):
        table[y][0] = y

    def C(c1, c2):
        if c1 == c2:
            return 0
        return float('inf')

    # Filling the table
    for i in range(1, b):
        for j in range(1, a):
            table[i][j] = min(table[i - 1][j] + 1, table[i][j - 1] + 1,
                              table[i - 1][j - 1] + C(word1[j - 1], word2[i - 1]))
    return table[b - 1][a - 1]


def hamming(word1, word2):
    a, b = len(word1), len(word2)
    if a > b:
        for _ in range(a - b):
            word2 += " "
    elif b > a:
        for _ in range(b - a):
            word1 += " "

    distance = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            distance += 1
    return distance


def levensthein(word1, word2):
    # Table creation
    a, b = len(word1) + 1, len(word2) + 1
    table = [[0 for _ in range(a)]
             for _ in range(b)]
    for x in range(1, a):
        table[0][x] = x
    for y in range(1, b):
        table[y][0] = y

    def C(c1, c2):
        if c1 == c2:
            return 0
        return 1

    # Filling the table
    for i in range(1, b):
        for j in range(1, a):
            table[i][j] = min(table[i - 1][j] + 1, table[i][j - 1] + 1,
                              table[i - 1][j - 1] + C(word1[j - 1], word2[i - 1]))
    return table[b - 1][a - 1]


if __name__ == "__main__":
    main()
