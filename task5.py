def prime_factors(n):
    def is_prime(num):
        if num <= 1:
            return False
        if num == 2 or num == 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True
    
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
        while not is_prime(divisor):
            divisor += 1
    
    cumulative_product = 1
    for factor in factors:
        cumulative_product *= factor
    
    return factors, cumulative_product

# Example usage:
number = 56
factors, product = prime_factors(number)
print(f"Prime factors of {number}: {factors}")
print(f"Cumulative product of prime factors: {product}")
