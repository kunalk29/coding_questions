from typing import List

def solve_v0(t: List[int]) -> int:
    current_finished = 0
    current_finished_index = None
    t_len = len(t)
    for j in range(t_len):
        added_minutes = [t_len - j + x for x in range(0, j)]  + [x for x in range(0, t_len - j)]
        print(added_minutes)
        total_time_list = [a_i - b_i for a_i, b_i in zip(t, added_minutes)]
        print(total_time_list)
        finished = sum([x <= 0 for x in total_time_list])
        print(j, finished)
        if finished > current_finished:
            print(f"New index: {j}, value: {finished}")
            current_finished_index = j
            current_finished = finished
    return current_finished_index + 1

def solve_v1(t: List[int]) -> int:
    t_len = len(t)
    finish_map = {x: 0 for x in range(t_len)}
    for i in range(t_len):
        val = t[i]
        print(f"Index: {i}, value: {val}")
        # valid_values = list(range(i + 1
    #     for j in :
    #         print(f"Adding to index: {j} moving value from {finish_map[i]} to {finish_map[i] + 1}")
    #         finish_map[j] += 1
    # current_max = None
    # max_index = -1
    # print(finish_map)
    # for m in finish_map.keys():
    #     if current_max is None or finish_map[m] > current_max:
    #         current_max = finish_map[m]
    #         max_index = m
    # return max_index

def solve_v2(t: List[int]) -> int:
    n = len(t)
    A = [0] * (n + 1)
    for i, x in enumerate(t):
        r1 = max(-1, i - x) + 1
        r2 = min(max(i, i - x + n) + 1, n)
        print(r1, r2)
        A[0] += 1
        A[r1] -= 1
        A[i + 1] += 1
        A[r2] -= 1
        print(A)
    for i in range(n):
        A[i + 1] += A[i]
        print(i + 1, A[i + 1])
    print(A)
    return A.index(max(A)) + 1

def solve(t: List[int]) -> int:
    return solve_v2(t=t)

if __name__ == '__main__':

    input_args = [4,9,11,3,6,8,4,10,2,3,9,7]
    output = solve(t=input_args)
    print(f"Input: {input_args}")
    print(f"Output: {output}")