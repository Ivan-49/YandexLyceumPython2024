events = [input() for i in range(int(input()))]

queue = []

for event in events:

    if "встал" in event:
        queue.append(" ".join(event.split()[:-3]))
    elif "будет за тобой" in event:
        first, second = " ".join(event.split()[1:-3]).split("! ")

        print

        queue.insert(queue.index(first) + 1, second)
    elif "хватит тут стоять" in event:
        queue.remove(" ".join(event.split()[:-5])[:-1])

print(*queue, sep="\n")
