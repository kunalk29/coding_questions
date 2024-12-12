from typing import List

def absolutePermutation(n: int, k: int) -> List[int]:
    return absolute_permutation_v3(n=n, k=k)



def absolute_permutation_v3(n: int, k: int) -> List[int]:
    if k == 0:
        return [x + 1 for x in range(n)]
    if n % 2*k != 0:
        return [-1]
    flip = 1
    x = [0 for _ in range(n)]
    for i in range(len(x)):
        j = i + 1
        x[i] = j + k * flip

        if j % k == 0:
            flip = flip * - 1
    return x

def absolute_permutation_v2(n: int, k: int) -> List[int]:
    if not k:
        return [x + 1 for x in range(n)]
    if n % 2 == 1:
        return [-1]
    mapping = {x: None for x in range(1, n + 1)}
    for i in range(k):
        j = i + 1
        mapping[j] = j + k
        mapping[n - i] = n - i - k
    used_numbers = {x for x in mapping.values() if x is not None}
    for x in range(n + k + 1, n - k + 1):
        choices = [x + k, x - k]
        for x in choices:
            if x < 0:
                choices.remove(x)
            if x in used_numbers:
                choices.remove(x)
        if len(choices) == 1:
            mapping[x] = choices[0]
        else:
            return [-1]

    # Unfinished - there are two choices for many possible inputs, instead of only being wittled down to 1


def absolute_permutation_v1(n: int, k: int) -> List[int]:
    if not k:
        return [x + 1 for x in range(n)]
    if n % 2 == 1:
        return [-1]
    if k == n / 2:
        return [x + k  + 1 for x in range(n -k)] + [x + 1 for x in range(k)]
    if k == 1:
        return [x + 2 if x % 2 == 0 else x for x in range(n)]
    return [-1]

def check_abs_diff(arr: List[int], k: int) -> bool:
    remainders = [abs(arr[i] - (i + 1))  == k for i in range(len(arr))]
    return all(remainders)


def absolute_permutation_v0(n: int, k: int) -> List[int]:
    from itertools import permutations
    base = [x + 1 for x in range(n)]
    possiblities = list(permutations(base))
    possiblities = [x for x in possiblities if check_abs_diff(arr=x, k=k)]
    possiblities.sort()
    if not len(possiblities):
        return [-1]
    return possiblities[0]


if __name__ == '__main__':

    input_args = (24, 1)
    output = absolute_permutation_v3(*input_args)
    print(f"Input: {input_args}")
    print(f"Output: {output}")

