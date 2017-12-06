EXAMPLE_INPUT = "0	2	7	0"

def count_cycles(memBankStr):
    history = []
    mem_banks = [int(x) for x in memBankStr.strip().split()]
    num_banks = len(mem_banks)
    while True:
        # Find largest
        idx = mem_banks.index(max(mem_banks))
        val = mem_banks[idx]
        # Redistribute
        mem_banks[idx] = 0
        for _ in range(val):
            idx += 1
            if idx >= num_banks:
                idx = 0
            mem_banks[idx] += 1
        # Test if we encountered this config before
        if mem_banks in history:
            return len(history) + 1
        history.append(mem_banks[:])

def main():
    assert count_cycles(EXAMPLE_INPUT) == 5
    with open('input.txt', 'r') as input_file:
        print(count_cycles(input_file.read()))

if __name__ == "__main__":
    main()
