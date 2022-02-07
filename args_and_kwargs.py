
# 					///////////		ARGS	/////////	


# 													/////////// example 1
def add_numbers():
	l = [(1,2),2,3, 'hello', 1, 3]
	return l 






# 													/////////// example 2
l = add_numbers()
print(*l)

def add_numbers(a,b,c):
	print(a,b,c)

# l=[1,2,3]				# l 	=  list
# add_numbers(*l)		# *l 	=	values separated by spaces







#													/////////// example 3
def add_numbers(*args):
	print(args)			# print args ---->> 1, 2, 3 become a tuple

add_numbers(1,2,3)		# 1, 2, 3  -->>  numbers separated by comma




#													/////////// example 4
def add_numbers(a, *args):
	print(a, args)
	print((sum(args), sum(a)))

add_numbers({1,2,3},1,2,3,4,5,6,7)

# RESULT!!!!
# a = {1, 2, 3}
# args = (1, 2, 3, 4, 5, 6, 7)





# 					///////////		KWARGS	/////////	

def add_numbers(**kwargs):		# **kwargs --->> **l
	print(kwargs['c'])

l = {'a':1, 'b':2, 'c':4}
# l >>>>>  a=1, b=2, c=4
add_numbers(**l)				# **l --->>  {'a':1, 'b':2, 'c':4} 