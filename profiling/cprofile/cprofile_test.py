import cProfile

def slow_function():
	total = 0
	for i in range(1_000_000):
		total += 1
	return total

def fast_function():
	return sum(range(1_000_000))


def fibo(n: int) -> int:
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)

def main():
	print(fibo(30))

if __name__ == '__main__':
	main()
	
cProfile.run('main()', 'output.prof')