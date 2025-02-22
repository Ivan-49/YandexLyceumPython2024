def prepare(*args, magic=1):
    global ingredients
    insert_index = magic
    arg_index = 0

    while arg_index < len(args) and insert_index <= len(ingredients):
        ingredients.insert(insert_index, args[arg_index])
        insert_index += magic + 1
        arg_index += 1
