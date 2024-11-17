user = int(input())
mnoj = int(str(user)[0])
while (mnoj != 1) and (user <= 1_000_000_000):
    mnoj = int(str(user)[0])
    user *= mnoj
print(user)

