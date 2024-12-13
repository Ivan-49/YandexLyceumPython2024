heap1 = int(input())
heap2 = int(input())

motion = True  # True - "AI", False - "User"

while heap1 != 0 or heap2 != 0:
    if motion:
        if min(heap1, heap2) == heap2 and heap2 != 0:
            print("""AI selected second pile""")
            count = heap2 % 4
            if count == 0:
                count = 2
            heap2 -= count
            print(
                f"""AI took it away {count} stones from second pile,
                  {heap2} remained in it, {heap1} remained in first pile"""
            )
            motion = False
        else:
            print("""AI selected first pile""")
            count = heap1 % 4
            if count == 0:
                count = 2
            heap1 -= count
            print(
                f"""AI took it away {count} stones from first pile,
                  {heap1} remained in it, {heap2} remained in second pile"""
            )
            motion = False
        if heap1 == 0 and heap2 == 0:
            print("""AI win, User lose""")
    else:
        while True:
            choosing_pile = int(input("""select pile: """))
            if choosing_pile == 1 and heap1 == 0:
                print("""There are no stones in first pile""")
            elif choosing_pile == 2 and heap2 == 0:
                print("""There are no stones in second pile""")
            else:
                break
        if choosing_pile == 1:
            print("""User selected first pile""")
            count = int(input())
            while not (1 <= count <= 3 and count <= heap1):
                print("""You entered incorrect number, try again""")
                count = int(input())
            heap1 -= count
            print(
                f"""User took it away {count} stones from first pile,
                  {heap1} remained in it, {heap2} remained in second pile"""
            )
            motion = True
        else:
            print("""User selected second pile""")
            count = int(input())
            while not (1 <= count <= 3 and count <= heap2):
                print("""You entered incorrect number, try again""")
                count = int(input())
            heap2 -= count
            print(
                f"""User took it away {count} stones from second pile,
                  {heap2} remained in it, {heap1} remained in first pile"""
            )
            motion = True
        if heap1 == 0 and heap2 == 0:
            print("""User win, AI lose""")
