from sympy import isprime


def is_center_of_prime_triplet(n, start, size):
    if not isprime(n):
        return False

    count = 0
    if n > start and isprime(n - size):
        count += 1
    if n > start and isprime(n + size - 1):
        count += 1
        if count == 2:
            return True
    if n > start and isprime(n - 1):
        count += 1
        if count == 2:
            return True
    if n < start + size - 2 and isprime(n - size + 2):
        count += 1
        if count == 2:
            return True
    if n < start + size - 1 and isprime(n - size + 1):
        count += 1
        if count == 2:
            return True
    if n < start + size - 1 and isprime(n + 1):
        count += 1
        if count == 2:
            return True
    if isprime(n + size):
        count += 1
        if count == 2:
            return True
    if isprime(n + size + 1):
        count += 1
        if count == 2:
            return True

    return False


def sum_prime_triplets_for_row(row):
    if row <= 1:
        return 0

    start = row*(row+1)//2 + 1 - row
    prime_sum = 0
    for n in range(start, start + row):
        if not isprime(n):
            continue
        if (
            is_center_of_prime_triplet(n, start, row)
            or (n - start > 0 and is_center_of_prime_triplet(n - row, start - row + 1, row - 1))
            or (n - start < row - 1 and is_center_of_prime_triplet(n - row + 1, start - row + 1, row - 1))
            or (n - start < row - 2 and is_center_of_prime_triplet(n - row + 2, start - row + 1, row - 1))
            or (n - start > 0 and is_center_of_prime_triplet(n + row - 1, start + row, row + 1))
            or is_center_of_prime_triplet(n + row, start + row, row + 1)
            or is_center_of_prime_triplet(n + row + 1, start + row, row + 1)
            or is_center_of_prime_triplet(n - 1, start, row)
            or is_center_of_prime_triplet(n + 1, start, row)
        ): prime_sum += n

    return prime_sum


print(sum_prime_triplets_for_row(5678027) + sum_prime_triplets_for_row(7208785))
