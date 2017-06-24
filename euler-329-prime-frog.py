from sympy import isprime, Rational

from Primer import average

"""
    1  2  3  4  5  6  7  8  9 10 11 12 13 14 15
    P  P  P  P  N  N  P  P  P  N  P  P  N  P  N
"""

length = 500
correct_croaks = ['P', 'P', 'P', 'P', 'N', 'N', 'P', 'P', 'P', 'N', 'P', 'P', 'N', 'P', 'N']


def neighbor_positions(position):
    if position == 0:
        return [1]
    elif position == length - 1:
        return [length - 2]
    else:
        return [position - 1, position + 1]


def correct_croak_prob(position, step):
    return croak_probs(position)[correct_croaks[step]]


def croak_probs(position):
    if isprime(position + 1):
        return {
            'P': Rational(2, 3),
            'N': Rational(1, 3)
        }
    else:
        return {
            'P': Rational(1, 3),
            'N': Rational(2, 3)
        }

probs = [
    [0] * length for step in range(15)
]

probs[14] = [correct_croak_prob(pos, 14) for pos in range(length)]

for step in reversed(range(14)):
    for pos in range(length):
        probs[step][pos] = average(probs[step + 1][next_pos] for next_pos in neighbor_positions(pos)) * correct_croak_prob(pos, step)

print(average(probs[0]))
