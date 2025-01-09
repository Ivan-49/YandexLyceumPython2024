start_weather = input()
sunny_to_cloudy = float(input())
cloudy_to_sunny = float(input())
num_days = int(input())

cloudy_to_cloudy = 1 - cloudy_to_sunny
sunny_to_sunny = 1 - sunny_to_cloudy
weather_probs = {"пасмурно": [], "ясно": []}
current_probs = [cloudy_to_sunny, sunny_to_cloudy]
is_cloudy = True

for _ in range(num_days - 1):
    next_probs = []

    for prob in current_probs:
        if is_cloudy:
            next_probs.append(round(cloudy_to_sunny * prob, 4))
            weather_probs["пасмурно"].append(round(cloudy_to_sunny * prob, 4))
            next_probs.append(prob * sunny_to_sunny)
            weather_probs["пасмурно"].append(round(prob * sunny_to_sunny, 4))
            is_cloudy = False

        else:
            next_probs.append(prob * sunny_to_cloudy)
            next_probs.append(round(cloudy_to_cloudy * prob, 4))
            weather_probs["ясно"].append(round(cloudy_to_cloudy * prob, 4))
            weather_probs["ясно"].append(round(prob * sunny_to_cloudy, 4))
            is_cloudy = True

    current_probs = next_probs

max_prob = max(current_probs)

if max_prob in weather_probs["пасмурно"] and max_prob in weather_probs["ясно"]:
    print("равновероятно")
    print(max_prob)

elif max_prob in weather_probs["ясно"]:
    print("ясно")
    print(max_prob)

else:
    print("пасмурно")
    print(max_prob)
