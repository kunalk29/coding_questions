from typing import List

def dynamic_array(n: int, queries: List[int]) -> List[int]:
    arr = [[] for _ in range(n)]
    last_answer = 0
    answers = []
    for query_type, x, y in queries:
        if query_type == 1:
            idx = x ^ last_answer % n
            arr[idx].append(y)
        if query_type == 2:
            idx = x ^ last_answer % n
            last_answer = arr[idx][y % len(arr[idx])]
            answers.append(last_answer)
    return answers

if __name__ == '__main__':
    inputs = (2, [[1,0,5], [1, 1, 7], [1, 0, 3], [2, 1, 0], [2, 1, 1]])
    output = dynamic_array(*inputs)
    print(f"input: {inputs}, output: {output}")