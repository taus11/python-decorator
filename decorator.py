def decorator(func):
	def wrapper():
		print('top bread')
		func()
		print('bottom bread\n')
	return wrapper

@decorator
def vegSandwich():
	print 'vegetables'

@decorator
def NonvegSandwich():
	print("meat")

vegSandwich()
NonvegSandwich()
