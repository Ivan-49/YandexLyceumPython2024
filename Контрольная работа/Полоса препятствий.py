num_words = int(input())
anti_vampire_words = {input().lower() for _ in range(num_words)}

num_lines = int(input())
best_line = ""
max_matches = -1

for _ in range(num_lines):
    line = input().lower()
    parts = line.split()

    if not parts or len(parts[0]) <= 1:
        continue

    matches = sum(1 for word in anti_vampire_words if word in line)

    if matches >= max_matches:
        max_matches = matches
        best_line = line

if best_line:
    result_words = [
        part for part in best_line.split() if part not in anti_vampire_words
    ]
    print("; ".join(result_words))
else:
    print("")
