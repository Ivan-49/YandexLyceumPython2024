from __future__ import annotations


class Stones:
    def __init__(self, count: int) -> None:
        self.count: int = count

    def minus(self, count_user_minus: int) -> None:
        self.count -= count_user_minus
        return f"Количество комней уменьшено на {count_user_minus}, сейчас {self.count}"

    def win(self, why: Player) -> str:
        if why.name == "AI":
            return f"ИИ выиграл!"
        elif why.name == "User":
            return f"Вы выиграли!"
        else:
            return None


class Player:
    def __init__(
        self,
        name: str,
        active: bool = False,
    ) -> None:
        self.active = active
        self.name = name

    def move(self, stones: Stones, coun: int) -> None:
        stones.minus(coun)

    def win(self, stones: Stones) -> None:
        if stones.count <= 0:

            return stones.win(self)


class User(Player):
    def movement(self, stones: Stones) -> None:
        while True:
            try:
                count_user = int(input())
            except ValueError:
                print(f"Некорректный ход: {count_user}")
            if count_user <= 3 and count_user >= 1 and count_user <= stones.count:
                self.move(stones, count_user)
                print(f"{count_user} {stones.count}")
                self.active = False
                return self.win(stones)
            else:
                print(f"Некорректный ход: {count_user}")


class AI(Player):
    def movement(self, stones: Stones) -> None:
        res: int
        count_stones = stones.count

        res = count_stones % 4
        if res == 0:
            res = 2

        self.move(stones, res)
        print(f"{res} {stones.count}")
        self.active = False
        return self.win(stones)


def main() -> None:
    stones = Stones(int(input()))
    user = User("User")
    ai = AI("AI")
    aaaaa = "a"
    while aaaaa != "":
        aaaaa = ai.movement(stones)
        if stones.count <= 0:
            break
        aaaaa = user.movement(stones)
        if stones.count <= 0:
            break
    print(aaaaa)


if __name__ == "__main__":
    main()
