#Function to calculate if the number is a prime number or not
def is_prime(x):
    #all the numbers less than 2 are essentially non-prime.
	if (x < 2):
        return False
    #As per the definition of prime numbers, there are obly divisors for them. 1 being the number one and the other one the number itself.
	#...if there is presence of a third divisor, then the particular number is bound to be a non-prime.	
    for n in range(x):
        if (n > 1) and (x%n == 0):
            return False
            break
    #if previous loop fails then the number is prime number.
	return True