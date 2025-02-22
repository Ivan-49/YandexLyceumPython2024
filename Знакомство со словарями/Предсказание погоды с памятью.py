current_weather = input()

if current_weather == "ясно":
    clear = 1
    cloudy = 0

else:
    clear = 0
    cloudy = 1

prob_clear_to_clear = float(input())
prob_cloudy_to_cloudy = float(input())
iterations = int(input())

for _ in range(iterations):
    clear, cloudy = (
        max(clear * prob_clear_to_clear, cloudy * (1 - prob_cloudy_to_cloudy)),
        max(cloudy * prob_cloudy_to_cloudy, clear * (1 - prob_clear_to_clear)),
    )

if clear > cloudy:
    print("ясно")
    print(clear)

elif cloudy > clear:
    print("пасмурно")
    print(cloudy)

else:
    print("равновероятно")
    print(clear)
