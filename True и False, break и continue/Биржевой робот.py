buyCost = sellCost = 0
prevDay = int(input())
while sellCost == 0:
    currDay = int(input())
    if buyCost == 0 and currDay > prevDay:
        buyCost = currDay
    if buyCost != 0 and currDay < prevDay:
        sellCost = currDay
    prevDay = currDay
print(buyCost, sellCost, sellCost - buyCost)
