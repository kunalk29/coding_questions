from typing import List, Tuple

def load_data(file_path: str) -> Tuple[List[List[int]], List[List[int]]]:
    with open(file_path, 'r') as fptr:
        print("HERE")
        first_line = fptr.readline()
        print(first_line)
        n, m = first_line.split(" ")
        n, m = int(n), int(m)
        shots = []
        for _ in range(n):
            shots.append([int(x) for x in fptr.readline().split(" ")])

        players = []

        for _ in range(m):
            players.append([int(x) for x in fptr.readline().split(" ")])

    return shots, players