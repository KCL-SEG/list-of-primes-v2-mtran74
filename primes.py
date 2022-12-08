"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes < 1:
        raise ValueError("Incorrect value entered try again")
        return
    list = []
    nextPrime = 2
    while len(list) < number_of_primes:
        is_prime = True
        for i in range(2, nextPrime):
            if nextPrime % i == 0:
                is_prime = False
                break
        if is_prime:
            list.append(nextPrime)
        nextPrime += 1
    return list
