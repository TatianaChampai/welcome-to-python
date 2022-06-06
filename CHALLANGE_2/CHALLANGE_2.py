a: int = 12
b: int = 45
c: int = 75

def shift_a_b_c():
	global a
	global b
	global c
	a , b , c = c , a , b
	pass

def main():
	print("=== BEFORE shift_a_b_c() ===")
	print("A: {0}".format(a))
	print("B: {0}".format(b))
	print("C: {0}".format(c))

	shift_a_b_c()

	print("=== AFTER shift_a_b_c() ===")
	print("A: {0}".format(a))
	print("B: {0}".format(b))
	print("C: {0}".format(c))
	pass

if __name__ == "__main__":
	main()