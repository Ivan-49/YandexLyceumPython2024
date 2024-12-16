import math


teams = sorted(
    [(input(), int(input())) for _ in range(int(input()))],
    key=lambda t: t[1],
    reverse=True,
)

cutoff = math.ceil(len(teams) / 2)
print(*sorted(t[0] for t in teams[:cutoff]), sep='\n')
print(*sorted(t[0] for t in teams[cutoff:]), sep='\n')

