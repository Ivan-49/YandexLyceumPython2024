home_book = int(input())
summer_book = int(input())

home_book_set = [input() for i in range(home_book)]
summer_book_set = [input() for i in range(summer_book)]
for i in summer_book_set:
    if i in home_book_set:
        print("YES")
    else:
        print("NO")