from typing import List

from hacker_rank.utils.functions import load_data


def solve_v0(shots: List[List[int]], players: List[List[int]]) -> int:
    player_strengths = {}
    for i, p in enumerate(players):
        player_strengths[i] = 0
        for s in shots:
            if not (p[0] > s[1] or p[1] < s[0]):
                player_strengths[i] += 1
    return sum(player_strengths.values())

def solve_v1(shots: List[List[int]], players: List[List[int]]) -> int:
    starts = [0 for _ in range(100_000)]
    ends = [0 for _ in range(100_000)]
    print(max([x[1] for x in shots]))
    for shot in shots:
        shot_start, shot_end = tuple(shot)
        starts[shot_start] += 1
        ends[shot_end + 1] += 1
    for i in range(len(starts) - 1):
        starts[i + 1] += starts[i]
        ends[i + 1] += ends[i]
    player_strength_sum = 0
    for player in players:
        player_start, player_end =  tuple(player)
        player_strength_sum += starts[player_end] - ends[player_start]
    return player_strength_sum


def solve(shots: List[List[int]], players: List[List[int]]) -> int:
    return solve_v1(shots=shots, players=players)


if __name__ == '__main__':
    input_args = (
        [
            [1, 2],
            [2, 3],
            [4, 5],
            [6, 7]
        ],
        [
            [1, 5],
            [2, 3],
            [4, 7],
            [5, 7]
        ]
    )
    # print(input_args)
    input_args = load_data('/Users/kunalkoppula/opt/repos/coding_questions/hacker_rank/medium/datasets/mr_x_and_his_shots_test_5.txt')
    output = solve(*input_args)
    print(output)