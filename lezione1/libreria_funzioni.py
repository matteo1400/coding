def is_n_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True



def factorial(x):
    result = 1
    for i in range(1, x + 1):
        result = i * result 
    return result 