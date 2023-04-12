
def main():
    word1 = "apple"
    word2 = "car"
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
    
    # Filling the table
    for i in range(1, b):
        for j in range(1, a):
            pass
    

if __name__ == "__main__":
    main()