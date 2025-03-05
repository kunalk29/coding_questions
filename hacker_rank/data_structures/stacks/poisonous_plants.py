def poisonousPlants(arr):
    stack = [0]
    days = [0] * len(arr)
    pivot = arr[0]
    res = 0

    for ind in range(1, len(arr)):
        print(f"i: {ind}, arr[i]: {arr[ind]}")
        if arr[ind] > arr[ind - 1]:
            days[ind] = 1

        pivot = min(pivot, arr[ind])
        print(f"pivot: {pivot}")
        # print("stack = {}".format(stack))
        while stack and arr[stack[-1]] >= arr[ind]:
            print(f"in while loop, stack: {stack}")
            if arr[ind] > pivot:
                print(f"adjusting days[ind]: {days[ind]} to: {max(days[ind], days[stack[-1]] + 1)}")
                days[ind] = max(days[ind], days[stack[-1]] + 1)

            stack.pop()
            print(f"new_stack: {stack}")

        res = max(res, days[ind])
        print(f"new_res: {res}")
        stack.append(ind)
        print(f"always add to stack: {stack}")

    return res

if __name__ == '__main__':
    input_args = ([4, 3, 7, 5, 6, 4, 2],)
    output = poisonousPlants(*input_args)
    print(f"Inputs: {input_args}, Output: {output}")