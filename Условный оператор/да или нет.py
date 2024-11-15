first_string = input().strip().lower()
second_string = input().strip().lower()
valid_words = ["да", "нет"]
if first_string in valid_words and second_string in valid_words:
    print("ВЕРНО")
else:
    print("НЕВЕРНО")

