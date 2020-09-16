'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
# set() method is used to convert any of the iterable to sequence of iterable elements with dintinct elements

def single_number(arr):
    return 2 * sum(set(arr)) - sum(arr) 

    # # Don't understand this...
    # # ^ == Binary XOR Bitwise Operator
    # # https://www.geeksforgeeks.org/find-element-appears-array-every-element-appears-twice/
    # res = arr[0]
    # for i in range(1, len(arr)):
    #     res = res ^ arr[i]

    # Why didn't this work?
    # count = 0
    # if arr[-1] != arr[-2] and arr[-1] != arr[-3]:
    #     return arr[-1] 
    # elif arr[0 + count] == arr[1 + count]:
    #     count += 2
    # elif arr[0 + count] != arr[1 + count]:
    #     if arr[0 + count] != arr[2 + count]:
    #         return arr[0 + count]
    #     else:
    #         return arr[1 + count]
    
if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")