"""
URL: https://stepik.org/lesson/334150/step/8?unit=317559
boolean for a:b:c string (a: palindrome, b: prime, c: even)
example: 1221:101:22
"""

# my solution:
def is_valid_password(p):
    is_palindrome = False
    nums = [int(i) for i in p.split(':')]
    if str(nums[0]) == str(nums[0])[::-1] and len(nums) == 3:
        is_palindrome = True

    primes = 1
    for i in range(2, nums[1]+1):
        if nums[1] % i == 0:
            primes += 1
    is_prime = primes == 2

    is_even = nums[2] % 2 == 0

    return is_palindrome and is_prime and is_even

# alternative solution 1:
def is_valid_password(password):
    password = password.split(':')
    return (password[0] == password[0][::-1])
            and (len([i for i in range(1, int(password[1])+1) if int(password[1]) % i == 0]) == 2)
            and (int(password[2]) % 2 == 0)