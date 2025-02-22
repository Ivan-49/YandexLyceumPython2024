old_message = ""


def print_without_duplicates(message):
    global old_message
    if message != old_message:
        print(message)
        old_message = message
