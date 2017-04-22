from numpy import ndindex


def count_numbers(remaining_digits, digits=[], memo={}):
    current_sum = sum(digits)
    assert current_sum < 10

    if (remaining_digits, current_sum) in memo:
        return memo[remaining_digits, current_sum]

    ans = 0
    if remaining_digits is 0:
        ans = 1
    else:
        for n in range(10 - current_sum):
            if not digits and n is 0:
                continue
            ans += count_numbers(remaining_digits - 1, digits[-1::] + [n], memo)

    memo[remaining_digits, current_sum] = ans
    return ans


def count_numbers_debug(remaining_digits, digits=[], memo={}):
    current_sum = sum(digits[-2::])
    d0, d1, *_ = digits[-2::] + [None, None]
    assert sum(digits[-3::]) < 10, digits

    if (remaining_digits, d0, d1) in memo:
        return memo[remaining_digits, d0, d1]

    if remaining_digits is 0:
        # print(''.join(map(str, digits)) + ', ', end='')
        return 1

    ans = 0
    for n in range(10 - current_sum):
        if not digits and n is 0:
            continue
        ans += count_numbers_debug(remaining_digits - 1, digits + [n], memo)

    memo[remaining_digits, d0, d1] = ans
    # print(memo)

    return ans


def acc(numbers):
    ans = 0
    for digit in numbers:
        ans = ans * 10 + digit
    return ans


def get_numbers(digits):
    for numbers in ndindex(* digits * [10]):
        if numbers[0] == 0:
            continue
        alright = True
        for a, b, c in zip(numbers, numbers[1::], numbers[2::]):
            if a + b + c > 9:
                alright = False
                break
        if alright:
            yield acc(numbers)

digits = 500
# print(', '.join((map(str, list(get_numbers(digits))))))
# print(len(list(get_numbers(digits))))
# print(count_numbers(digits))
print(count_numbers_debug(digits))
