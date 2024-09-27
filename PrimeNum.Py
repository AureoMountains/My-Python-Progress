nums=range(1,1000)

def is_prime(num):
    for x in range(10,num):
        if (num%x) == 0:
            return False
        return True
    primes=list(filter(is_prime, nums))
