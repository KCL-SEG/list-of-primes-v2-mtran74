"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes < 1:
        raise ValueError("Incorrect value entered try again")
        return
    list = [2]
    counter = 3
    while len(list) != number_of_primes:
        prime = True
        for i in range(3, counter + 1):
            if counter % i == 0:
                prime = False

        if prime == True:
            list.append(i)
        counter += 2
    return list
