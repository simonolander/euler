from sympy.ntheory import factorint

print('Calculating r(10**9)...')
n = (10 ** 1000000000 - 1) // 9
print('Factoring...')
print(factorint(n, limit=170000, verbose=True))
