def power(num,ind):

	#BASE CASE 
	if ind==1:
		return num
	elif ind==0:
		return 1

	#RECURSIVE CASE 	
	if ind%2 == 1:		#ODD INDEX
		return power(num,(ind/2))*power(num,(ind/2))*num
	else:				#EVEN INDEX
		return power(num,(ind/2))*power(num,(ind/2))


def basic_power_function_recursive(num,ind):
	if(ind==1):
		return 1
	return num*basic_power_function(num,ind-1)

def basic_power_function_loop(num,index):
	total = 1
	for i in range(index):
		total*=num
	return total

print power(2,100009)
# print basic_power_function_recursive(2,100000)
# print basic_power_function_loop(2,1000000)

