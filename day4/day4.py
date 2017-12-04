
def is_valid(passphrase):
    passphrase = passphrase.strip().split()
    return len(passphrase) == len(set(passphrase))

def main():
    assert is_valid("aa bb cc dd ee")
    assert not is_valid("aa bb cc dd aa")
    assert is_valid("aa bb cc dd aaa")
    
    num_valid = 0
    with open('input.txt', 'r') as input_file:
        for line in input_file:
            if is_valid(line):
                num_valid += 1
    print num_valid

if __name__ == "__main__":
    main()
