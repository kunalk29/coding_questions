import bisect

def test_bisect() -> bisect:
    a = [1,4,6,12,59,291,505]
    # Bisect allows us to run a bisect algorithm on a sorted array. It continually evaluates if the
    # new addition is within the right or left half of the array by finding the midpoint, comparing to the new value,
    # then rerunning on the half of the array that the new value was in. O(N) = Log(N)
    new_value = 11
    b0 = bisect.bisect_left(a, new_value)
    print(f"The index the value of {new_value} would be added is {b0}")

    # Bisect left and right are used when we want to add a new value but want to be specific about the index returned
    # If the new value already exists, we would either return the index to the left or right of the matching values
    new_value = 59
    b1 = bisect.bisect_right(a, new_value)
    print(f"If we want the right most index to add this {new_value} we would used bisect_right and get: {b1}")


    b2 = bisect.bisect_left(a, new_value)
    print(f"If we want the left most index to add this new value: {new_value} we would used bisect_left and get: {b2}")


if __name__ == '__main__':
    d0 = test_bisect()