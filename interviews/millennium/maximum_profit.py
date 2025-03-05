# Question #1: The objective is given an array of prices, find the maximum profit if you must buy before you sell
# and can only have one 'lot' on at a time

from typing import List

def maximum_profit_q1(arr: List[float]) -> float:
    # one can assume the array is in chronological order
    answer = 0.0
    ind = 1
    buy_price = arr[0]
    while ind < len(arr):
        current_value = arr[ind]
        if current_value >= arr[ind - 1]:
            ind += 1
            continue
        else:
            # if the new value is not greater, we must take our buy price and reset to newest value, and add the
            # difference from the buy_price and the previous_value. We know all prices in between have been growing
            # larger
            answer += (arr[ind - 1] - buy_price)
            buy_price = arr[ind]
            ind += 1
    if arr[ind - 1] > buy_price:
        answer += (arr[ind - 1] - buy_price)
    return answer

# Question #2: Let's take the above question a step further - let's say you can buy as many times as you want
# but must start with a buy (can't be short stock). At each point you can buy one lot, and sell as many as you want.

def maximum_profit_q2(arr: List[float]) -> float:
    answer = 0.0
    current_max = arr[-1]
    # assumes a list of more than one
    ind = len(arr) - 2
    while ind > 0:
        if arr[ind] > current_max:
            current_max = arr[ind]
        else:
            answer += current_max - arr[ind]

        ind -= 1
    return answer

# Question #3: Now you can execute a short or long position, and can hold a maximum of n-1 positions at a time
def maximum_profit_q3(arr: List[float]) -> float:
    # Step 1: start at the end, keep track of high and low, execute n - 1 times

    low = arr[0]
    high = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < low:
            low = arr[i]
        if arr[i] > high:
            high = arr[i]
    return round((len(arr) - 1) * (high - low), 1)


if __name__ == "__main__":
    # Testing Question #1

    input = ([2.9, 5.2, 3.1, 3.5, 4.9, 9.3, 13.1, 5.3, 8.3, 5.1, 5.1, 5.6, 9.3], )
    output_q1 = maximum_profit_q1(*input)
    print(f"Question #1 - Input: {input}, Output: {output_q1}")

    # Testing Question #2
    output_q2 = maximum_profit_q2(*input)
    print(f"Question #2 - Input: {input}, Output: {output_q2}")

    # Testing Question #3
    output_q2 = maximum_profit_q3(*input)
    print(f"Question #3 - Input: {input}, Output: {output_q2}")