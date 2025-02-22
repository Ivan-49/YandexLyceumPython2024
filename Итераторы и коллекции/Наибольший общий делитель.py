from math import gcd
from functools import reduce
from sys import stdin

bash_input = [int(i.strip()) for i in stdin.readlines()]

print(reduce(gcd, bash_input))
