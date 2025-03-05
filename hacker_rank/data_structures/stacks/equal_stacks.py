from typing import List

def equalStacks_v0(h1, h2, h3):
    h1.reverse()
    h2.reverse()
    h3.reverse()
    while h1 and h2 and h3:
        if sum(h1) == sum(h2) and sum(h1) == sum(h3):
            return sum(h1)
        if sum(h1) >= sum(h2) and sum(h1) >= sum(h3):
            h1.pop()
        elif sum(h2) >= sum(h1) and sum(h2) >= sum(h3):
            h2.pop()
        else:
            h3.pop()
    # this method  is slow because we are constantly taking the sums, instead of relying on sums and subtracting.
    return 0

def equalStacks_v1(h1: List[int], h2: List[int], h3: List[int]) -> int:
    h1.reverse()
    h2.reverse()
    h3.reverse()
    sums = [0, 0, 0]
    running_sums = {f'h{a + 1}': 0 for a, b in enumerate([h1, h2, h3])}
    for x, y in enumerate([h1, h2, h3]):
        for z in y:
            running_sums[f'h{x + 1}'] += z
            sums.append(running_sums[f'h{x + 1}'])
    sums = sorted(sums, reverse=True)
    current_num = sums[0]
    current_count = 1
    for i in range(1, len(sums)):
        if sums[i] == current_num:
            current_count += 1
            if current_count == 3:
                return current_num
        else:
            current_num = sums[i]
            current_count = 1
    # We know atleast this will end with 0's since we put three zeros in at the beginning

def equalStacks_v2(h1: List[int], h2: List[int], h3: List[int]) -> int:
    # The most efficient version would be to combine the two above - start with max sizes, take off the end of the
    # largest list and subtract from that sum. Therefore not running sum() all the time.
    h1.reverse()
    h2.reverse()
    h3.reverse()
    sum1 = sum(h1)
    sum2 = sum(h2)
    sum3 = sum(h3)
    while h1 and h2 and h3:
        if sum1 == sum1 == sum3:
            return sum1
        if sum1 >= sum2 and sum1 >= sum3:
            sum1 -= h1.pop()
        elif sum2 >= sum1 and sum2 >= sum3:
            sum2 -= h2.pop()
        else:
            sum3 -= h3.pop()
    # this method  is slow because we are constantly taking the sums, instead of relying on sums and subtracting.
    return 0



def equalStacks(h1, h2, h3):
    return equalStacks_v2(h1=h1, h2=h2, h3=h3)

if __name__ == '__main__':
    input_args = ([3, 2, 1, 1, 1],[4, 3, 2], [1, 1, 4, 1])
    print(f"Inputs: {input_args}")
    output = equalStacks_v1(*input_args)
    print(f"Output: {output}")