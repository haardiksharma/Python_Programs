#to calculate the factorial of the number
def factorial(x):
    #initialize this variable to 1
	prod = 1
    # as long as number is not zero, keep multiplying it with the previous prodcut, to calculate the final factorial.
	for n in range(x):
        if n != 0:
            prod = prod*n
	#since the range will only be able to reach a number less than x, so we need to compensate that by multiplying the last prod with 'n+1'		
    return prod*(n+1)  