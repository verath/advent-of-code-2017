import sys


def solve_captcha(captcha):
    shift = len(captcha) / 2
    captcha = [int(c) for c in captcha]
    captcha_shifted = captcha[shift:] + captcha[:shift]
    captcha_pairs = zip(captcha, captcha_shifted)
    matching_values = [pair[0] for pair in captcha_pairs if  pair[0] == pair[1]]
    return sum(matching_values)

def main():
    assert solve_captcha("1212") == 6
    assert solve_captcha("1221") == 0
    assert solve_captcha("123425") == 4
    assert solve_captcha("123123") == 12
    assert solve_captcha("12131415") == 4

    if len(sys.argv) < 2:
        print "Usage: {} input.txt".format(sys.argv[0])
        return

    input_filename = sys.argv[1]
    captcha = ""
    with open(input_filename, "r") as input_file:
        captcha = input_file.read().strip()

    print solve_captcha(captcha)

if __name__ == "__main__":
    main()
