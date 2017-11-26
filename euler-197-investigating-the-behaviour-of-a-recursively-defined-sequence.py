from math import floor


def f(x):
	return floor(2**(30.403243784 - x**2)) * 10**-9


u0 = -1
u1 = f(u0)
for i in range(1000):
	u0, u1 = u1, f(u1)


print(u0 + u1)
