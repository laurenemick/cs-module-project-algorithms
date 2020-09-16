'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    new_arr = sorted(arr)

    for i in range(len(new_arr)):
        if new_arr[i] < 0:
            new_arr.insert(len(new_arr), new_arr.pop(i))
        else:
            break

    return new_arr[::-1]


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")

# moving_zeroes([0, 3, 1, 0, -2])