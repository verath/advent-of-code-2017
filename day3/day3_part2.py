
def gen_positions():
    x, y = 0, 0    
    yield (0, 0)
    layer = 1
    while True:
        x += 1
        layer += 1
        direction_steps = 2 * (layer - 1)
        yield (x, y)
        for _ in range(direction_steps - 1):
            y += 1
            yield (x, y)
        for _ in range(direction_steps):
            x -= 1
            yield (x, y)
        for _ in range(direction_steps):
            y -= 1
            yield (x, y)
        for _ in range(direction_steps):
            x += 1
            yield (x, y)


def get_pos_value(spiral, pos):
    (pos_x, pos_y) = pos
    adjacent_squares = [(x, y)
                        for x in range(pos_x-1, pos_x+2)
                        for y in range(pos_y-1, pos_y+2)
                        if (x, y) != (pos_x, pos_y)]
    adjacent_sum = sum([
        spiral[square] if square in spiral else 0
        for square in adjacent_squares
    ])
    return adjacent_sum


def main():
    spiral = {
        (0, 0): 1
    }
    positions = gen_positions()
    next(positions) # Skip (0, 0)
    for pos in positions:
        val = get_pos_value(spiral, pos)
        if val > 347991:
            print(val)
            break
        spiral[pos] = val


if __name__ == "__main__":
    main()
