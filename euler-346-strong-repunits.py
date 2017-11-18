
maximum = 10**12

units = set([1])
for b in range(2, 10**6):
	n = b**2 + b**1 + 1
	p = 3
	while n < maximum:
		units.add(n)
		n += b**p
		p += 1
print(sum(units))
