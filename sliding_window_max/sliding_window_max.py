'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
# what if k is longer than array 'nums'? -- iterate through arr and return 1 element in the arr (max)
# pattern: output length is (nums - k) + 1

def sliding_window_max(nums, k):
    if k > len(nums):
        return max(nums)

    arr_len = (len(nums)-k) + 1

    for i in range(nums):

            






if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
