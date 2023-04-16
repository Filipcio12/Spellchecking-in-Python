import ast
import distance as ds


def suggest_word(misspell, dictionary):
    if misspell in dictionary:
        return misspell

    best_word = ""
    best_distance = float('inf')

    for word in dictionary:
        distance = ds.levensthein_mod(misspell, word)
        if distance < best_distance:
            best_word = word
            best_distance = distance

    return best_word


def hash_words(dictionary):
    hash_table = {}
    for word in dictionary:
        c = frequent_char(word)
        if c not in hash_table:
            hash_table[c] = [word]
        elif word not in hash_table[c]:
            hash_table[c].append(word)
    return hash_table


def frequent_char(word):
    frequency = {}
    for c in word:
        if c in frequency:
            frequency[c] += 1
        else:
            frequency[c] = 1
    chars = frequency.items()
    max_char = max(chars, key=lambda c: c[1])
    return max_char[0]


def suggest_word_mod(misspell, hash_table):
    dictionary = hash_table[frequent_char(misspell)]
    suggest_word(misspell, dictionary)


def main():
    "Create hash_table"

    '''file = open("words_alpha.txt", "r")
    dictionary = file.readlines()
    for i in range(len(dictionary)):
        dictionary[i] = dictionary[i][:-1]
    file.close()'''

    # Creating a hash_table
    '''hash_table = hash_words(dictionary)
    file = open("hash_table.txt", "w")
    file.write(str(hash_table))
    file.close()'''

    file = open("hash_table.txt", "r")
    data = file.read()
    file.close()

    hash_table = ast.literal_eval(data)
    print(hash_table["a"])


if __name__ == "__main__":
    main()
