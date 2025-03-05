def generate_time_in_string(h: int) -> str:
    time_map = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
        20: 'twenty',
        21: 'twenty one',
        22: 'twenty two',
        23: 'twenty three',
        24: 'twenty four',
        25: 'twenty five',
        26: 'twenty six',
        27: 'twenty seven',
        28: 'twenty eight',
        29: 'twenty nine',
    }
    return time_map[h]


def timeInWords(h, m):
    hour_in_string = generate_time_in_string(h=h)
    if h == 12:
        next_hour_in_string = generate_time_in_string(h=1)
    else:
        next_hour_in_string = generate_time_in_string(h=h + 1)

    if not m:
        return f"{hour_in_string} o' clock"
    elif not m % 15:
        if m == 15:
            return f"quarter past {hour_in_string}"
        elif m == 30:
            return f"half past {hour_in_string}"
        elif m == 45:
            return f"quarter to {next_hour_in_string}"
    if m < 30:
        minute_in_string = generate_time_in_string(h=m)
        return f"{minute_in_string} minutes past {hour_in_string}"
    else:
        remaining_minutes_in_string = generate_time_in_string(h=60 - m)
        return f"{remaining_minutes_in_string} minutes to {next_hour_in_string}"


if __name__ == '__main__':
    input_args = 1, 1

    answer = timeInWords(*input_args)
    print(f"Input: {input_args}")
    print(f"Output: {answer}")