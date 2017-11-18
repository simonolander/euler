import operator as op
from functools import reduce

def ncr(n, r):
	r = min(r, n-r)
	if r == 0: return 1
	numer = reduce(op.mul, range(n, n-r, -1))
	denom = reduce(op.mul, range(1, r+1))
	return numer//denom


def p(n, r):
	return ncr(n, r) / 2**n


f8 = 0
# f7 = 1 + p(1, 1)*f8 + p(1, 0)*f7 -> (1 - p(1, 0) * f7 = 
f7 = (1 + p(1, 1)*f8) / (1 - p(1, 0))
f6 = (1 + p(2, 1)*f7 + p(2, 2)*f8) / (1 - p(2, 0))
f5 = (1 + p(3, 1)*f6 + p(3, 2)*f7 + p(3, 3)*f8) / (1 - p(3, 0))
f4 = (1 + p(4, 1)*f5 + p(4, 2)*f6 + p(4, 3)*f7 + p(4, 4)*f8) / (1 - p(4, 0))
f3 = (1 + p(5, 1)*f4 + p(5, 2)*f5 + p(5, 3)*f6 + p(5, 4)*f7 + p(5, 5)*f8) / (1 - p(5, 0))
f2 = (1 + p(6, 1)*f3 + p(6, 2)*f4 + p(6, 3)*f5 + p(6, 4)*f6 + p(6, 5)*f7 + p(6, 6)*f8) / (1 - p(6, 0))
f1 = (1 + p(7, 1)*f2 + p(7, 2)*f3 + p(7, 3)*f4 + p(7, 4)*f5 + p(7, 5)*f6 + p(7, 6)*f7 + p(7, 7)*f8) / (1 - p(7, 0))
f0 = (1 + p(8, 1)*f1 + p(8, 2)*f2 + p(8, 3)*f3 + p(8, 4)*f4 + p(8, 5)*f5 + p(8, 6)*f6 + p(8, 7)*f7 + p(8, 8)*f8) / (1 - p(8, 0))

print(f8)
print(f7)
print(f6)
print(f5)
print(f4)
print(f3)
print(f2)
print(f1)
print(round(f0, 10))

f = {32: 0}
for n in reversed(range(32)):
	remaining = 32 - n
	fn = (1 + sum(p(remaining, i)*f[n + i] for i in range(1, remaining + 1))) / (1 - p(remaining, 0))
	f[n] = fn
print(f)
print(round(f[0], 10)) 
