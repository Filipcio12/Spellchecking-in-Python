import distance as ds
from tqdm import tqdm


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


def main():
    word1 = "car"
    word2 = "cat"
    print(f"levensthein:        {ds.levensthein(word1, word2)}")
    print(f"hamming:            {ds.hamming(word1, word2)}")
    print(f"indel:              {ds.indel(word1, word2)}")
    print(f"levensthein_mod:    {ds.levensthein_mod(word1, word2)}")
    print(f"hamming_mod:        {ds.hamming_mod(word1, word2)}")
    print()

    file = open("words_alpha.txt", "r")
    dictionary = file.readlines()
    file.close()
    for i in range(len(dictionary)):
        dictionary[i] = dictionary[i][:-1]

    file = open("misspelled.txt", "r")
    text = file.readlines()
    file.close()

    file = open("corrected.txt", "w")

    word, new_text = "", ""

    for line in text:
        word = ""
        for c in line:
            if c == ' ' or c == '\n':
                if len(word) > 0:
                    word = suggest_word(word, dictionary)
                    new_text += word + c
                    word = ""
                else:
                    new_text += c
            else:
                word += c

    word = suggest_word(word, dictionary)
    new_text += word

    file.write(new_text)
    file.close()


if __name__ == "__main__":
    main()
