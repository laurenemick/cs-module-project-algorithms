'''
Input: an integer
Returns: an integer

 1. He can eat 1 cookie at a time 3 times
 2. He can eat 1 cookie, then 2 cookies 
 3. He can eat 2 cookies, then 1 cookie
 4. He can eat 3 cookies all at once. 
'''
# # runtime is O(3^n)
# def eating_cookies(n):
#     if n < 0:
#         return 0
#     elif n == 0:
#         return 1
#     # if n < 2:
#     #     return 1
#     # elif n == 2:
#     #     return 2
#     else:
#         return eating_cookies(n - 3) + eating_cookies(n - 2) + eating_cookies(n - 1) 
 
# Improved - 0(n)
def eating_cookies(n, cache=None): 
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif cache and cache[n] > 0: 
        return cache[n]
    else:
        if not cache:
            # init an empty cache
            cache = {i: 0 for i in range(n+1)} 
        # store answers in our cache
        cache[n] = eating_cookies(n - 3, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 1, cache) 
    return cache[n]

eating_cookies(5)
# # Another way
#     arr = [0,0,1]
#     i = 0
#     while i < n:
#         arr.append(arr[0] + arr[1] + arr[2])
#         arr.pop(0)
#         i += 1
#     return arr[2]

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
