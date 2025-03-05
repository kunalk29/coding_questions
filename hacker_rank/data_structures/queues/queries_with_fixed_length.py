from typing import List


def solve_helper_v0(arr: List[int], q: int) -> int:
    results = []
    for i in range(len(arr) - (q - 1)):
        results.append(max(arr[i:i+q]))
    return min(results)

def solve_v0(arr: List[int], queries: List[int]) -> List[int]:
    results = []
    for q in queries:
        results.append(solve_helper_v0(arr=arr, q=q))
    return results

def solve_helper_v1(arr: List[int], q: int) -> int:
    results = []
    for i in range(len(arr) - (q - 1)):
        results.append(max(arr[i:i+q]))
    return min(results)

def solve_v1(arr: List[int], queries: List[int]) -> List[int]:
    results = []
    for q in queries:
        results.append(solve_helper_v0(arr=arr, q=q))
    return results

def solve(arr, queries):
    return solve_v0(arr=arr, queries=queries)

if __name__ == '__main__':
    fp = 'datasets/queries_with_fixed_length_dataset_0'
    queries = []
    with open(fp, 'r') as f:
        first_line = f.readline().split(" ")
        len_arr, len_queries = int(first_line[0]), int(first_line[1])
        arr = [int(x) for x in f.readline().split()]
        for j in range(len_queries):
            queries.append(int(f.readline()))

    # input_args = ([33,11, 44, 11, 55], [1,2,3,4,5])
    output = solve(arr=arr, queries=queries)
    print(output)