url = input()
requrst = {}

get_requrst = url[url.index("?") + 1 :]

for i in get_requrst.split("&"):
    key, value = i.split("=")
    requrst[key] = value

print(requrst[input()])
