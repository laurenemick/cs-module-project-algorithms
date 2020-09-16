'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
# what if k is longer than array 'nums'? -- iterate through arr and return 1 element in the arr (max)
# pattern: output length is (nums - k) + 1

def sliding_window_max(nums, k):
    if len(nums) == 0:
        return None
    elif k > len(nums):
        return max(nums)
    else:
        arr_len = [0 for _ in range((len(nums)-k) + 1)]
        new_arr = []
        start = 0 
        end = k

        for i in range(len(arr_len)):
            for num in range(start, end):
                new_arr.append(nums[num])
            arr_len[i] = max(new_arr)
            new_arr = []
            start += 1
            end += 1

    return arr_len



            






if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
