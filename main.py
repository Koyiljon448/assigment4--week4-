def num_divide3(num):
    count = 0
    for i in range(1, num + 1):
        if i % 3 == 0:
            count += 1
    return count


while True:
    user_input = input("Enter a positive integer: ")

    if user_input.lower() == 'done':
        print("bye!!!")
        break

    try:
        num = int(user_input)
        if num <= 0:
            print("Error. Enter a positive integer.")
        else:
            result = num_divide3(num)
            print(f"Numbers divisible by 3 among numbers 1 to {num}: {result}")
    except ValueError:
        print("Enter a positive integer:")
