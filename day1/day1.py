import sys


def solve_captcha(captcha):
    captcha = [int(c) for c in captcha]
    captcha_shifted = captcha[:-1] + [captcha[0]]
    captcha_pairs = zip(captcha, captcha_shifted)
    matching_values = [pair[0] for pair in captcha_pairs if  pair[0] == pair[1]]
    return sum(matching_values)

def main():
    assert solve_captcha("1122") == 3
    assert solve_captcha("1111") == 4
    assert solve_captcha("1234") == 0
    assert solve_captcha("91212129") == 9

    if len(sys.argv) < 2:
        print "Usage: day1.py input.txt"
        return

    input_filename = sys.argv[1]
    captcha = ""
    with open(input_filename, "r") as input_file:
        captcha = input_file.read().strip()

    print solve_captcha(captcha)


if __name__ == "__main__":
    main()
