def print_numbers_descending(num):

    for i in range(num, 0, -1):
        if i == 1:
            print(i)
        else:
            print(i, end=",")

def print_numbers_ascending(num):

    for i in range(1, num+1):
        if i == num:
            print(i)
        else:
            print(i, end=",")


print_numbers_descending(10)
print_numbers_ascending(10)
print("\n")