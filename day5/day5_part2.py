EXAMPLE_INPUT = "0\n3\n0\n1\n-3\n"

def count_steps(jump_list):
    jump_list = [int(n) for n in jump_list.splitlines()]
    steps = 0
    idx = 0
    while idx < len(jump_list):
        next_idx = idx + jump_list[idx]
        if jump_list[idx] >= 3:
            jump_list[idx] -= 1
        else:
            jump_list[idx] += 1
        idx = next_idx
        steps += 1
    return steps

def main():
    assert count_steps(EXAMPLE_INPUT) == 10
    with open('input.txt', 'r') as input_file:
        print(count_steps(input_file.read()))

if __name__ == "__main__":
    main()
