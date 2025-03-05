from typing import List

def two_stacks_v0(maxSum, a, b):
    current_sum = 0
    current_count = 0
    a_index = 0
    b_index = 0
    while current_sum <= maxSum:
        if a_index == len(a) and b_index == len(b):
            break
        elif a_index == len(a):
            current_sum += b[b_index]
            b_index += 1
        elif b_index == len(b):
            current_sum += a[a_index]
            a_index += 1
        elif a[a_index] < b[b_index]:
            current_sum += a[a_index]
            a_index += 1
        elif b[b_index] < a[a_index]:
            current_sum += b[b_index]
            b_index += 1
        current_count += 1
    return current_count - 1

def two_stacks_v1(maxSum: int, a: List[int], b: List[int]) -> int:
    cumsum_a = []
    current_sum_a = 0
    for x in a:
        current_sum_a += x
        if current_sum_a < maxSum:
            cumsum_a.append(current_sum_a)
        else:
            break

    cumsum_b = []
    current_sum_b = 0
    for y in b:
        current_sum_b += y
        if current_sum_b < maxSum:
            cumsum_b.append(current_sum_b)
        else:
            break
    print(cumsum_a, cumsum_b)
    while cumsum_a[-1] + cumsum_b[-1] > maxSum:
        print(cumsum_a, cumsum_b)
        if cumsum_a[-1] > cumsum_b[-1]:
            cumsum_a = cumsum_a[:-1]
        else:
            cumsum_b = cumsum_b[:-1]
    return len(cumsum_a) + len(cumsum_b) + 1

def two_stacks_v2(maxSum: int, a: List[int], b: List[int]) -> int:
    x = maxSum
    print(a, b)
    a = a[::-1]
    b = b[::-1]
    print(a, b)
    handy_stack = []
    el_count = 0
    total = 0

    while len(a) > 0:
        print(total, el_count, handy_stack)
        if total + a[-1] <= x:
            temp = a.pop()
            handy_stack.append(temp)
            total += temp
            el_count += 1
        else:
            break

    total_b = 0
    while len(b) > 0:
        print(total, total_b, el_count, handy_stack)
        if total_b + b[-1] <= x:
            if total + b[-1] <= x:
                temp = b.pop()
                total += temp
                total_b += temp
                el_count += 1
            else:
                temp = b.pop()
                total = total - handy_stack.pop() + temp
                total_b += temp
        else:
            break

    return el_count


def twoStacks(maxSum, a, b):
    return two_stacks_v2(maxSum=maxSum, a=a, b=b)

if __name__ == '__main__':

    input_args = (12, [1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1])
    output = twoStacks(*input_args)
    print(f"Input: {input_args}")
    print(f"Output: {output}")