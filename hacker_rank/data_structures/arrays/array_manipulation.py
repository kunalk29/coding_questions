from typing import List

def arrayManipulation_v0(n: int, queries: List[List[int]]) -> int:
    v = [0 for _ in range(n)]
    for start_index, end_index, value in queries:
        for i in range(start_index - 1, end_index):
            v[i] += value

    return max(v)

def find_start_index(q: List[int], current_array: List[List[int]]) -> int:
    ind = 0
    while ind < len(current_array):
        if q[0] <= current_array[ind][0]:
            return ind
        ind += 1
    return len(current_array)

def is_overlap(a: List[int], b: List[int]) -> bool:
    if a[2] >= b[1] or b[2] >= a[1]:
        return True
    return False

def arrayManipulation_v1(n: int, queries: List[List[int]]) -> int:
    v = [queries[0]]
    for ind in range(1, len(queries)):
        start_index = find_start_index(q=queries[ind], current_array=v)
        if start_index == len(v):
            v.append(queries[ind])
        else:
            v.insert(start_index, queries[ind])
        print(v)
        if is_overlap(queries[ind], queries[start_index]):
            #augment the sides, create new middle
            indices = [queries[ind][0], queries[ind][1], queries[start_index][0], queries[start_index][1]]
            indices.sort()
            print(indices)
            left_hand_side = [indices[0], indices[1], queries[ind][2]]
            overlap = [indices[1], indices[2], queries[ind][2] + queries[start_index][2]]
            right_hand_side = [indices[2], indices[3], queries[start_index][2]]
            print(start_index - 1)
            print(v)
            v.pop(start_index)
            print(v)
            v.pop(start_index - 1)
            print(v)
            v.insert(start_index, right_hand_side)
            print(v)
            v.insert(start_index, overlap)
            print(v)
            v.insert(start_index, left_hand_side)
            print(v)
        else:
            v.insert(start_index, queries[ind])
    return max([x[2] for x in v])

if __name__ == '__main__':
    inputs = (
        5,
        [
            [1, 2, 100],
            [2, 5, 100],
            [3, 4, 100]
        ]
    )
    output = arrayManipulation_v1(*inputs)
    print(f"input: {inputs}, output: {output}")