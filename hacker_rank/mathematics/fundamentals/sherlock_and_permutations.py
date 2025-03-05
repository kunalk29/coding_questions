import math


def solve_v0(n, m):
    p = n + m - 1
    r = m - 1
    numerator = math.factorial(p)
    denominator = math.factorial(r) * math.factorial(p - r)
    return int(numerator // denominator % (1e9 + 7))


def inner_factorial(i, j):
    result = 1
    for k in range(j, i):
        result = result * (k + 1)
    return result


def solve_v1(n, m):
    p = n + m - 1
    r = m - 1
    # This is done to avoid overflow errors - break down the combination formula
    numerator = inner_factorial(i=p, j=r)
    denominator = math.factorial(p - r)
    answer = int(numerator // denominator)
    # When using modulo, both sides should be an int - using the '1e9' by default is a float
    answer = answer % int(1e9 + 7)

    return answer


def solve(n, m):
    return solve_v1(n=n, m=m)

if __name__ == '__main__':
    input_args = (19, 10)
    output = solve(*input_args)
    print(f"Inputs: {input_args}, Output: {output}")