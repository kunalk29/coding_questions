from typing import List

def flatten(s: List[List[int]]) -> List[int]:
    return [x for y in s for x in y]

def create_all_magic_squares() -> List:
    pass

def formingMagicSquares_v0(s: List[List[int]]) -> int:
    return formingMagicSquares(s=s)

def formingMagicSquares(s: List[List[int]]) -> int:
    return formingMagicSquares_v0(s=s)

if __name__ == '__main__':
    # input_args = 1, 1
    #
    # answer = formingMagicSquares(*input_args)
    # print(f"Input: {input_args}")
    # print(f"Output: {answer}")
    print(flatten([[1,2,3], [4,5,6]]))