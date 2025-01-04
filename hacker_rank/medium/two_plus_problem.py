from typing import List

def find_plus_size(new_arr: List[List[str]], i: int, j: int, height: int, width: int) -> int:
    depth = 0
    check = True
    while check:
        depth += 1
        if i - depth < 0:
            break
        if j - depth < 0:
            break
        if i + depth >= height:
            break
        if j + depth >= width:
            break
        if new_arr[i - depth][j] != 'G':
            break
        if new_arr[i + depth][j] != 'G':
            break
        if new_arr[i][j - depth] != 'G':
            break
        if new_arr[i][j + depth] != 'G':
            break
    if depth == 1:
        return 1
    else:
        return depth

def find_size_by_depth(depth: int) -> int:
    return 1 + 4 * (depth - 1)

def mark_grid(new_arr: List[List[str]], i: int, j: int, depth: int, ch: str) -> List[List[str]]:
    new_arr[i][j] = ch
    for k in range(1, depth):
        new_arr[i + k][j] = ch
        new_arr[i - k][j] = ch
        new_arr[i][j + k] = ch
        new_arr[i][j - k] = ch
    return new_arr

def still_valid(new_arr: List[List[str]], i: int, j: int, depth: int) -> bool:
    valid = True
    for k in range(1, depth):
        if new_arr[i + k][j] == 'B':
            valid = False
            break
        if new_arr[i - k][j] == 'B':
            valid = False
            break
        if new_arr[i][j + k] == 'B':
            valid = False
            break
        if new_arr[i][j - k] == 'B':
            valid = False
            break
    return valid

def twoPluses(grid: List[str]) -> int:
    size_array = []
    height = len(grid)
    width = len(grid[0])
    new_arr = [list(x) for x in grid]
    for i in range(height):
        for j in range(width):
            if new_arr[i][j] == 'G':
                plus_size = find_plus_size(new_arr=new_arr, i=i, j=j, height=height, width=width)
                for x in range(1, plus_size + 1):
                    size_array.append([i , j, x])
    size_array.sort(key=lambda e: e[2])
    if len(size_array) < 1:
        return 0
    elif len(size_array) == 1:
        return size_array[0][2]
    max_product = 0
    m = -1
    while m * -1 <= len(size_array):
        v1 = find_size_by_depth(depth=size_array[m][2])
        new_arr = mark_grid(
            new_arr=new_arr,
            i=size_array[m][0],
            j=size_array[m][1],
            depth=size_array[m][2],
            ch='B'
        )
        n = m - 1
        while n * -1 <= len(size_array):
            if still_valid(new_arr=new_arr, i=size_array[n][0], j=size_array[n][1], depth=size_array[n][2]):
                v2 = find_size_by_depth(depth=size_array[n][2])
                if v1 * v2 > max_product:
                    max_product = v1 * v2
                    break
            n -= 1
        new_arr = mark_grid(
            new_arr=new_arr,
            i=size_array[m][0],
            j=size_array[m][1],
            depth=size_array[m][2],
            ch='G'
        )
        m -= 1
    return max_product


if __name__ == '__main__':
    input_args = [
        'GGGGGGGGGGGG',
'GBGGBBBBBBBG',
'GBGGBBBBBBBG',
'GGGGGGGGGGGG',
'GGGGGGGGGGGG',
'GGGGGGGGGGGG',
'GGGGGGGGGGGG',
'GBGGBBBBBBBG',
'GBGGBBBBBBBG',
'GBGGBBBBBBBG',
'GGGGGGGGGGGG',
'GBGGBBBBBBBG'
    ]
    output = twoPluses(input_args)

    print(f"Output: {output}")
