from src.utils.calculate.calculate import calculate

assert calculate("1+2") == 3
assert calculate("(12-10)*(9+6)") == 30
assert calculate("12-10*9+6") == -72
assert calculate("12/6") == 2
assert calculate("2^3") == 8
assert calculate("2^3%2") == 0