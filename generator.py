#VsemPrivet Vsemmoezdorovo
def generator_():
	number = 0
	while number<1000000:
		yield number
		number += 3
for i in generator_():
	print(i, end=" ")
