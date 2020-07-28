
def get_char_counts(word):
    char_counts = {}
    for letter in word:
        index = ord(letter) - ord('a')
        char_counts[index] = char_counts.get(index, 0) + 1
    return char_counts

def get_delta(char_counts_1, char_counts_2):
    diff = {}
    for k1,v1 in char_counts_1.items():
        v2 = char_counts_2.get(k1, 0)
        diff[k1] = abs(v1 - v2)
        if (v2 > 0):
            char_counts_2[k1] = 0
        char_counts_1[k1] = 0
    return sum(char_counts_2.values()) + sum(diff.values())

def make_anagram(word_1, word_2):
    char_counts_1 = get_char_counts(word_1)
    char_counts_2 = get_char_counts(word_2)
    return get_delta(char_counts_1, char_counts_2)

print(make_anagram("hello", "billion"))
