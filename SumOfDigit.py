# To calculate the sum of the digits of a number
def digit_sum (n):
    #initialize a empty list a
	a = []
    #while the number is greater than 0, slice the number and keep the remainder digit of the resultant number into a list a
	while n > 0:
        a.append(n%10)
        n = n/10
    #in the end take the sum of all the digits collected in the list-a    
    return sum(a)