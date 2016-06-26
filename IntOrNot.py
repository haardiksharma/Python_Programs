# to check whether a number is an integer or not,without using a simple integer check
def is_int(x):
	#check if the number's decimal values are there, if difference is zero, then the number is a integer  
    if x - round(x) == 0:
        return True
    #if the difference is present then the number is non-integer
	else:
        return False