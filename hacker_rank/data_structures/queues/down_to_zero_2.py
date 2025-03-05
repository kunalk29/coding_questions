import math
from typing import List
def biggest_factor(n: int) -> int:
    square_root = int(math.sqrt(n))
    result = n
    for i in range(2, square_root + 1):
        if n % i == 0:
            result = int(n / i)
    return result


def down_to_zero_v0(n: int) -> int:
    # We know that we should probably start with some sort of modulo, GCF type equation - the max number of steps is 'n'
    steps = 0
    while n > 0:
        print(f"step: {steps}, n={n}")
        new_n = biggest_factor(n=n)
        if new_n == n:
            n -= 1
        else:
            n = new_n
        steps += 1
    # This greedy algorithm doesn't work because the path of least resistance is not always the largest reduction of n
    # Sometimes we need a larger number that may have more composite factors on the next go around

    return steps

def down_to_zero_v1_helper() -> List[int]:
    limit = 1_000_000
    all_nums = [-1] * limit
    for i in range(0,4):
        all_nums[i] = i

    for j in range(limit):
        if all_nums[j] == -1:
            all_nums[j] = all_nums[j - 1] + 1
        elif all_nums[j] > all_nums[j - 1] + 1:
            all_nums[j] = all_nums[j - 1] + 1
        k = 1
        while k <= j and k * j < limit:
            # multiply the two numbers - if the steps of that number are greater than what is already there or -1, change the steps
            k_j = k * j
            if all_nums[k_j] == -1:
                all_nums[k_j] = all_nums[j] + 1
            if all_nums[k_j] > all_nums[j] + 1:
                all_nums[k_j] = all_nums[j] + 1
            k += 1
    return all_nums

def downToZero(n):
    # This solution only works if you modify the __main__ function within Hacker Rank to use the helper function
    # before the 'for' loop of 'q' numbers, so you don't have to recreate it every time
    result_array = down_to_zero_v1_helper()
    return result_array[n]

if __name__ == '__main__':

    input_args = (27, )
    output = downToZero(*input_args)
    print(f"Input: {input_args}")
    print(f"Output: {output}")