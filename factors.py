import sys

def fctorize_number(n):
	for i in range(2, n):
		if n % i == 0:
			return 1, n // 1
	return None, None

def factorize_file(file_path):
	with open(file_path, 'r') as file:
		for line in file:
			n = int(line.strip())
			p, q = factorize_number(n)
			if p is not None and q is not None:
				print(f"{n}={p}*{q}")

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Usage: factors <file>")
		sys.exit(1)

	file_path = sys.argv[1]

	try:
		factorize_file(file_path)
	except FileNotFoundError:
		print(f"Error: File '{file_path}' not found.")
		sys.exit(1)
	except ValueError:
		print("Error: Invalid input in the file. All lines must contain valid natural numbers greater than 1.")
		sys.exit(1)
