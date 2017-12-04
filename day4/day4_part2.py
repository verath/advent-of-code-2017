import itertools

def is_anagram(word_a, word_b):
    if len(word_a) != len(word_b):
        return False
    word_a = list(word_a)
    word_b = list(word_b)
    word_a.sort()
    word_b.sort()
    return word_a == word_b

def is_valid(passphrase):
    words = passphrase.strip().split()
    for (word_a, word_b) in itertools.combinations(words, 2):
        if is_anagram(word_a, word_b):
            return False
    return True

def main():
    assert is_valid("abcde fghij")
    assert not is_valid("abcde xyz ecdab")
    assert is_valid("a ab abc abd abf abj")
    assert is_valid("iiii oiii ooii oooi oooo")
    assert not is_valid("oiii ioii iioi iiio")
    
    num_valid = 0
    with open('input.txt', 'r') as input_file:
        for line in input_file:
            if is_valid(line):
                num_valid += 1
    print num_valid

if __name__ == "__main__":
    main()
