COUNT_EVENT = int(input())

queue = []

for i in range(COUNT_EVENT):
    event = input()
    match event[0]:
        case "К":
            queue.append(event.split(" - ")[-1][:-1])
        case "Я":
            queue.insert(0, event.split()[-1][:-1])
        case "С":
            try:
                print(f"Заходит {queue.pop(0)}!")
            except IndexError:
                print("В очереди никого нет.")
