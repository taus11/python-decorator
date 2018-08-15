# python-decorator
Simple code to show what a @decorator is for



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


# Output
top bread
vegetables
bottom bread

top bread
meat
bottom bread
