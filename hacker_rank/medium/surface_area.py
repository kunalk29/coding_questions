from typing import List

def surfaceArea_v0(A: List[List[int]]) -> int:
    height = len(A)
    width = len(A[0])
    surface_area = 6 * sum([sum(x) for x in A])
    print(f"New Surface Area BASE: {surface_area}")
    for i in range(height):
        for j in range(width):
            surface_area -= 2 * (A[i][j] - 1)
            print(f"New Surface Area BASE: {surface_area}")
            print(f"Working on index: {i}, {j}, value: {A[i][j]}")
            if i - 1 >= 0:
                print(f"Comparing {A[i - 1][j], A[i][j]}")
                surface_area -= min(A[i - 1][j], A[i][j])
                print(f"New Surface Area: {surface_area}")
            if i + 1 < height:
                print(f"Comparing {A[i + 1][j], A[i][j]}")
                surface_area -= min(A[i + 1][j], A[i][j])
                print(f"New Surface Area: {surface_area}")
            if j - 1 >= 0:
                print(f"Comparing {A[i][j - 1], A[i][j]}")
                surface_area -= min(A[i][j - 1], A[i][j])
                print(f"New Surface Area: {surface_area}")
            if j + 1 < width:
                print(f"Comparing {A[i][j + 1], A[i][j]}")
                surface_area -= min(A[i][j + 1], A[i][j])
                print(f"New Surface Area: {surface_area}")
    return surface_area


def surfaceArea(A: List[List[int]]) -> int:
    return surfaceArea_v0(A=A)

if __name__ == '__main__':
    input_args = [
        [1, 3, 4],
        [2, 2, 3],
        [1, 2, 4]
    ]
    input_args = [
        [
            51,
            32,
            28,
            49,
            28,
            21,
            98,
            56,
            99,
            77
        ]
    ]
    print(input_args)
    output = surfaceArea(A=input_args)
    print(output)