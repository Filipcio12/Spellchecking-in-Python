
def main():
    word1 = "replace"
    word2 = "delete"
    table = levensthein(word1, word2)
    for line in table:
        print(line)


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
    return table


if __name__ == "__main__":
    main()
