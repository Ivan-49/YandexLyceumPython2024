user = int(input())
spaces_count = user - 1
fg_count = 1
for i in range(user):
    print(' ' * spaces_count + '*' * fg_count)
    fg_count += 2
    spaces_count -= 1