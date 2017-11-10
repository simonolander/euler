from Primer import primer_10_000_000

max_n = 10**7
primer = primer_10_000_000()

ans = 0
for i in range(2, max_n + 1):
    factors = list(primer.factor_int(i, distinct=True))
    if len(factors) == 1:
        ans += 1
        print(i, 1, ans)
    else:
        largest_factor = factors[-1]
        ii = i - largest_factor
        while ii > 0:
            if pow(ii + 1, 2, i) == ii + 1:
                ans += ii + 1
                print(i, ii + 1, ans)
                break
            elif pow(ii, 2, i) == ii:
                ans += ii
                print(i, ii, ans)
                break
            ii -= largest_factor

print(ans)
