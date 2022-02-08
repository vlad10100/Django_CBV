# a = [1,2,3]

# try:
# 	print("Second Element = %s" %a[1])
# 	print("Fourth Element = %s" %a[4])

# except:
# 	print('An error occured')


""" 
	Result :
Second Element = 2
An error occured

"""

"""
/////////////Catching Specific Excetion


				try:
				    # statement(s)
				except IndexError:
				    # statement(s)
				except ValueError:
				    # statement(s)


"""


# def fun(x):
# 	if x < 4:
# 		b = (x/(x-3))

# 	print('The value of b: ', b)


# try:
# 	fun(3)
# 	fun(4)			# will not enter if statement, b will not be declared.
# 	fun(5)			# will not enter if statement, b will not be declared.

# except ZeroDivisionError:
# 	print("ZeroDivisionError has occured.")
# except NameError:
#     print("NameError Occurred and Handled, b is not declared")   



# def division(x, y):
# 	try:
# 		answer = (x+y) / (x-y)
# 	except ZeroDivisionError:
# 		print('Undefined')
# 	else:
# 		print(answer)


# division(3,3)			# 1/0 = undefined
# division(4,3)
# division(100, 101)


# 1/0 = undefined
# 0/0 = indeterminate
# inf/inf = indeterminate
# 1/inf = 0
# inf - inf = indetereminate
# -inf - inf = indeterminate


"""
/////////////////FINALLY

							try:
							    # Some Code.... 

							except:
							    # optional block
							    # Handling of exception (if required)

							else:
							    # execute if no exception

							finally:
							    # Some code .....(always executed)

"""

# try:
# 	f = 5 // 0
# except ZeroDivisionError:
# 	print('Undefined, cant divide by zero')
# finally:
# 	print('>>>  This is always executed')



try:
	amount = 40000
	if amount < 4000:
		raise ValueError('Please add money in your account.')
	else:
		print('You can use your account')
except ValueError as e:
	# e = ValueError
	print(e)


# " as " >>>>	CREATE an ALIAS