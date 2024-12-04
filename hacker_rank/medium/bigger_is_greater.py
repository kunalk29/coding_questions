import itertools


def generate_possibilities(w):
    possibilities = itertools.permutations(list(w))
    possibilities = set(possibilities)
    return possibilities


def biggerIsGreater_v1(w):
    # This is a brute force method - create all possibilities, sort them, and choose the one that
    # is at the next index compared to the original string
    possibilities = generate_possibilities(w)
    possibilities = [''.join(x) for x in possibilities]
    possibilities.sort()
    print(possibilities)
    if len(possibilities) == 1:
        return 'no answer'
    w_index = possibilities.index(w)
    if w_index + 1 == len(possibilities):
        return 'no answer'
    return possibilities[w_index + 1]


def make_smallest_string(s: str) -> str:
    if s == '':
        return ''
    x = list(s)
    x.sort()
    return ''.join(x)


def bigger_is_greater_v2(w: str) -> str:
    if len(w) == 1:
        return 'no answer'
    counter = len(w) - 2
    new_string = None
    switched = False
    # First, moving backwards, find the first letter you can change to make the string bigger
    while counter >= 0 and not switched:
        inner_count = counter + 1
        possible_switches = {}
        while inner_count < len(w):
            if w[counter] < w[inner_count]:
                possible_switches[inner_count] = ord(w[inner_count]) - ord(w[counter])
            inner_count += 1
        if len(list(possible_switches.keys())):
            current_min_key = None
            min_dist = 27  # distance between two letter can't exceed 26
            for k, v in possible_switches.items():
                if v < min_dist:
                    current_min_key = k

            new_string = list(w)
            new_string[counter] = w[current_min_key]
            new_string[current_min_key] = w[counter]
            new_string = ''.join(new_string)
            switched = True
        if not switched:
            counter -= 1

    if new_string is None:
        return 'no answer'

    # Then, rearrange the subsequent sub-string to be the smallest it can be
    remaining_string = new_string[counter + 1:]
    remaining_string = make_smallest_string(s=remaining_string)
    final_string = new_string[:counter + 1] + remaining_string
    return final_string


def biggerIsGreater(w: str) -> str:
    return bigger_is_greater_v2(w=w)