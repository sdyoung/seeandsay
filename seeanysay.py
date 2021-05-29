#!/usr/bin/python3
# This will generate the seeandsay riddle.

START = "1121"

def generate(existing):
	current_value = existing[0]
	counter = 0
	return_value = ""
	
	for i in existing:
		print("i is %s, current value is %s, counter is %s" % (i, current_value, counter))
		if i == current_value:
			counter += 1
		else:
			print("adding to value")
			return_value += str(counter) + str(current_value)
			current_value = i
			counter = 1
	return(return_value)

r = START

for j in range(1,10):
	r += generate(r)
	print(r)
