a: int = 12
b: int = 45

def swap_a_b():
	global a
	global b
	temp = a
	a = b
	b = temp
	pass

def main():
	print("=== BEFORE swap() ===")
	print("A: {0}".format(a))
	print("B: {0}".format(b))

	swap_a_b()

	print("=== AFTER swap() ===")
	print("A: {0}".format(a))
	print("B: {0}".format(b))
	pass

if __name__ == "__main__":
	main()