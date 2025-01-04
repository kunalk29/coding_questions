from typing import Tuple

def maxValue_v0(t: str) -> int:
    # TODO: Unfinished - as it doesn't complete in the time necessary
    t_len = len(t)
    max_result = t_len
    i = 0
    while i < t_len:

        char_len = 1
        farthest_end = 1
        while char_len < int(t_len / 3) + 1:
            if t[i:i + char_len] == t[i + char_len: i + 2 * char_len]:
                min_str, length = find_overlapping_string(new_str=t[i:], repeated=t[i:i+ char_len])
                end = len(min_str) * length
                if end > farthest_end:
                    farthest_end = end
                max_value = calculate_max_value(min_str=min_str, length=length)
                if max_value > max_result:
                    max_result = max_value
            char_len += 1
        i += farthest_end
    return int(max_result)

def find_overlapping_string(new_str: str, repeated: str) -> Tuple[str, int]:
    length = 1
    idx = 0
    min_str_len = len(repeated)
    check = True
    while check:
        if idx + min_str_len * 2 > len(new_str):
            break
        if new_str[idx:idx+min_str_len] == new_str[idx + min_str_len:idx + min_str_len * 2]:
            length += 1
            idx += min_str_len
        else:
            break
    return repeated, length

def calculate_max_value(min_str: str, length: int) -> int:
    v1 = len(min_str)
    if length % 2 == 1:
        max_value =  v1 * (length + 1) / 2 * (length + 1) / 2
    else:
        max_value = v1 * (length / 2 + 1) * (length / 2)
    return int(max_value)

import os
from itertools import zip_longest, islice


def suffix_array_best(s):
    """
    suffix array of s
    O(n * log(n)^2)
    """
    n = len(s)
    k = 1
    line = to_int_keys_best(s)
    while max(line) < n - 1:
        line = to_int_keys_best(
            [a * (n + 1) + b + 1
             for (a, b) in
             zip_longest(line, islice(line, k, None),
                         fillvalue=-1)])
        k <<= 1
    return line

def inverse_array(l):
    n = len(l)
    ans = [0] * n
    for i in range(n):
        ans[l[i]] = i
    return ans


def to_int_keys_best(l):
    """
    l: iterable of keys
    returns: a list with integer keys
    """
    seen = set()
    ls = []
    for e in l:
        if not e in seen:
            ls.append(e)
            seen.add(e)
    ls.sort()
    index = {v: i for i, v in enumerate(ls)}
    return [index[v] for v in l]


def suffix_matrix_best(s):
    """
    suffix matrix of s
    O(n * log(n)^2)
    """
    n = len(s)
    k = 1
    line = to_int_keys_best(s)
    ans = [line]
    print(n, k, line, ans)
    while max(line) < n - 1:
        line = to_int_keys_best(
            [a * (n + 1) + b + 1
             for (a, b) in
             zip_longest(line, islice(line, k, None), fillvalue=-1)])
        ans.append(line)
        k <<= 1
        print(n, k, line, ans)
    return ans

def suffix_array_alternative_naive(s):
    return [rank for suffix, rank in sorted((s[i:], i) for i in range(len(s)))]

def lcp(sm, i, j):
    """
    longest common prefix
    O(log(n))

    sm: suffix matrix
    """
    n = len(sm[-1])
    if i == j:
        return n - i
    k = 1 << (len(sm) - 2)
    ans = 0
    for line in sm[-2::-1]:
        if i >= n or j >= n:
            break
        if line[i] == line[j]:
            ans ^= k
            i += k
            j += k
        k >>= 1
    return ans


def maxValue(a):

    res = inverse_array(suffix_array_best(a))
    print(to_int_keys_best(a))
    print(suffix_array_best(a))

    mtx = suffix_matrix_best(a)

    lcp_res = []
    for n in range(len(res) - 1):
        lcp_res.append(lcp(mtx, res[n], res[n+1]))
    lcp_res.append(0)

    max_score = len(a)

    lcp_res_len = len(lcp_res)

    for i, num in enumerate(res):

        if lcp_res[i] <= 1:
            continue

        lcp_res_i = lcp_res[i]

        cnt = 2
        for ii in range(i+1, lcp_res_len):
            if lcp_res[ii] >= lcp_res_i:
                cnt += 1
            else:
                break
        for ii in range(i-1, -1, -1):
            if lcp_res[ii] >= lcp_res_i:
                cnt += 1
            else:
                break

        max_score = max(cnt * lcp_res_i, max_score)

    return max_score

if __name__ == '__main__':
    input_args = 'abcabcddd'
    output = maxValue(input_args)
    print(output)