import math

def calc_distance(num):
    # Fastest route is always equal to first moving
    # to the closest midpoint, then going straight in:
    #  . . .      . . .     . . .
    #  . . .  ->  . . x  -> . x .
    #  . . x      . . .     . . .
    
    # calculate the layer the number is on, starting at
    # layer 1 which only has the number 1.
    layer = math.floor((math.sqrt(num - 1) + 3) / 2)
    # layer_min is the lowest value in the layer
    layer_min = (2 * layer - 3) ** 2 + 1

    east = layer_min + (layer - 2)
    north = east + 2 * (layer - 1)
    west = north + 2 * (layer - 1)
    south = west + 2 * (layer - 1)
    distance = min([
        abs(num - east),
        abs(num - north),
        abs(num - west),
        abs(num - south)
    ])
    return distance + (layer - 1)


def main():
    assert calc_distance(12) == 3
    assert calc_distance(23) == 2
    assert calc_distance(1024) == 31
    assert calc_distance(46) == 3
    assert calc_distance(49) == 6

    print(calc_distance(347991))


if __name__ == "__main__":
    main()