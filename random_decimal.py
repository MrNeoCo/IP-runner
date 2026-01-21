from decimal import Decimal, getcontext
import random

getcontext().prec = 20  # enough precision

low = Decimal('6.20')
high = Decimal('7.10')

def random_decimal():
    r = Decimal(random.random())  # 0 ≤ r < 1
    value = low + (high - low) * r
    return value.quantize(Decimal('0.000000000'))  # 9 decimal places

# examples
for _ in range(26):
    print(random_decimal())
