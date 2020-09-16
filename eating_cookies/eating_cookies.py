'''
Input: an integer
Returns: an integer

 1. He can eat 1 cookie at a time 3 times
 2. He can eat 1 cookie, then 2 cookies 
 3. He can eat 2 cookies, then 1 cookie
 4. He can eat 3 cookies all at once. 
'''
def eating_cookies(n):
    if n < 2:
        return 1
    elif n == 2:
        return 2
    else:
        return eating_cookies(n - 3) + eating_cookies(n - 2) + eating_cookies(n - 1) 
 

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
