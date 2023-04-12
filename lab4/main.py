import distance as ds


def suggest_word(word):
    pass


def main():
    word1 = "car"
    word2 = "cat"
    print(f"levensthein:        {ds.levensthein(word1, word2)}")
    print(f"hamming:            {ds.hamming(word1, word2)}")
    print(f"indel:              {ds.indel(word1, word2)}")
    print(f"levensthein_mod:    {ds.levensthein_mod(word1, word2)}")
    print(f"hamming_mod:        {ds.hamming_mod(word1, word2)}")


if __name__ == "__main__":
    main()
