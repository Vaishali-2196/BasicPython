def print_numbers_ascending(num):
    for i in range(1, num + 1):
        if i == num:
            print(i, end=" ")
        else:
            print(i, end=", "),

print_numbers_ascending(10)

s1 = "TheGoodTheBadTheUgly"

s1_list = list(s1)

print("\n" + "\n " + "To reverse a string")
for i in range(len(s1_list) -1, -1, -1):
    print(s1[i], end="")

print("\n")
print("To swap two variables")

a = 10
b = 20

print("a: " + str(a) + "  b: " + str(b))
a, b = b, a

print("a: " + str(a) + "  b: " + str(b))

print("\n")
print("Fibonacci numbers")
# 1 2 3 5 8 13 21
def fibonacci_numbers (num):
    start = 1
    mid = 2
    print (str(start) + ", " + str(mid), end=", ")

    for i in range(num - 2):
        end = start + mid
        print(end, end=", ")
        start = mid
        mid = end

fibonacci_numbers(7)

print("\n")
print("factorial of number")
def factorial(num):
    temp = num;
    while num > 1:
        temp = temp * (num - 1)
        print(str(temp) + "  num: " + str(num))
        num = num - 1

factorial(7)


print("\n")
for i in range (1, 5):
    for j in range (1, i + 1):
        print("*", end="")
    print("\n", end="")


print("\n")
for x in range (0, 5):
    for y in range (0, 5-x):
        print("*", end="")
    print("\n", end="")
