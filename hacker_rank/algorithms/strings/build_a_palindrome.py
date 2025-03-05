from typing import Dict

def reverse_string(c: str) -> str:
    result = []
    for i in range(1, len(c) + 1):
        result.append(c[-1*i])
    return ''.join(result)

def is_palindrome(c: str) -> bool:
    len_c = len(c)
    if len_c % 2 == 1:
        half_length = int((len_c + 1)/ 2)
        return c[:half_length] == reverse_string(c[half_length - 1:])
    else:
        half_length = int(len_c / 2)
        return c[:half_length] == reverse_string(c[half_length:])

def generate_letter_count(value: str) -> Dict[str, int]:
    result = {}
    for i in range(len(value)):
        if value[i] in result.keys():
            result[value[i]] += 1
        else:
            result[value[i]] = 1

    return result

def buildPalindrome_v0(a: str, b: str) -> str:
    letter_count_a = generate_letter_count(value=a)
    letter_count_b = generate_letter_count(value=b)
    if len(set(letter_count_a.keys()).intersection(set(letter_count_b.keys()))) == 0:
        return '-1'


def buildPalindrome(a, b) -> str:
    # Unfinished - required learning about suffix trees
    return buildPalindrome_v0(a=a, b=b)

if __name__ == '__main__':
    input_args = 'abcd', 'efg'
    output = buildPalindrome(*input_args)
    print(output)