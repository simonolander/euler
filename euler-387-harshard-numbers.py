from sympy import isprime

maximum = 10**14

harshad = set()
queue = list((n, n) for n in range(1, 10))

while len(queue):
	n, digit_sum = queue.pop()
	if isprime(n // digit_sum):
		for digit in [1, 3, 7, 9]:
			maybe_harshad = n * 10 + digit
			if maybe_harshad < maximum and isprime(maybe_harshad):
				harshad.add(maybe_harshad)
	for digit in range(0, 10):
		m = n * 10 + digit
		m_sum = digit_sum + digit
		if m < maximum and m % m_sum == 0:
			queue.append((m, m_sum))

print(sum(harshad))
