class Receipt:
    def __init__(self):
        self.number = 0
        self.items = []
        self.total = 0
        self.count = 0


receipt = Receipt()


def add_item(item_name, item_cost):
    global receipt

    if receipt.number == 0:
        receipt.number = 1

    receipt.items.append((item_name, item_cost))
    receipt.total += item_cost
    receipt.count += 1


def print_receipt():
    global receipt

    if len(receipt.items) == 0:
        return

    print(f"Чек {receipt.number}. Всего предметов: {receipt.count}")

    for item in receipt.items:
        print(f"{item[0]} - {item[1]}")

    print(f"Итого: {receipt.total}")
    print("-----")
    number = receipt.number
    del receipt
    receipt = Receipt()
    receipt.number = number + 1


add_item("Блокнот", 100)
print_receipt()

add_item("Ручка", 70)
print_receipt()
print_receipt()

add_item("Булочка", 15)
add_item("Булочка", 15)
add_item("Чай", 5)
print_receipt()

add_item("Булочка", 15)
add_item("Булочка", 15)
