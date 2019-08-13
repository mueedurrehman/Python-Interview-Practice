def is_prime_v2(number):
    if number <= 1 or number % 2 == 0:
        return False
    if number == 2:
        return True
    iter = 3
    test_limit = round(number**0.5)
    while iter <= test_limit:
        if number % iter == 0:
            return False
        iter += 2
    return True
number = 10000007