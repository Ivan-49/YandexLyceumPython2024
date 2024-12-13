hash_value = 0
is_valid = True
count = int(input())

for index in range(count):

    input_number = int(input())
    major = input_number // (256**2)
    minor = (input_number // 256) % 256
    hash_value = (37 * (major + minor + hash_value)) % 256
    reconstructed_number = hash_value + (minor * 256) + (major * (256**2))

    if hash_value >= 100 or input_number != reconstructed_number:
        print(index)
        is_valid = False
        break

if is_valid:
    print(-1)
