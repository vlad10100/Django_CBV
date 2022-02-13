
#  DECORATORS
#  function inside a function

def count(num):
	def inside(inside):
		output = inside
		print('step**')
		return(output)
	print('step*')
	return inside

@count
def decorator():
	print(inside)

print(decorator(10), 'step***')

