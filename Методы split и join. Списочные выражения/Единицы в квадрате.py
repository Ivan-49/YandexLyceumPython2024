user = int(input())
print(', '.join([str(i**2) for i in range(user) if i**2 < user**2 and int(str(i).count('1')) == len(str(i))]))

print(', '.join(str(i**2) for i in range(int(input())) if str(i).count('1') == len(str(i)) and i**2 < int(input())**2))