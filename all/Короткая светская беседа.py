user_mood = input("Какое у вас настроение? ").strip().lower()

positive_keywords = {"хорошее", "прекрасно", "отлично", "замечательно"}
negative_keywords = {"плохое", "ужасно", "отвратительно", "скверно"}

has_positive = any(word in user_mood for word in positive_keywords)
has_negative = any(word in user_mood for word in negative_keywords)

if has_positive and has_negative:
    ...
elif "не" in user_mood or "?" in user_mood or (not has_positive and not has_negative):
    print("Извините, я вас не понимаю.")
elif has_positive:
    print("Отлично, у меня тоже всё хорошо :)")
elif has_negative:
    print("Ничего, скоро всё наладится.")
else:
    print("Спасибо за ваш ответ!")
