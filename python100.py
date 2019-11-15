# Task 1

user_dict = {
    "name": input("User name: "),
    "product": input("Product name: "),
    "product_count": int(input("Product count: "))
}

print(user_dict)


# Task 2

size = int(input("Triangle size: "))

spaces_count = size - 1
middle = int(len(range(size)) / 2) + 1
for r in range(size):
    line = '*' * (r + 1)

    if r + 1 == middle:
        stars = '*' * size
        spaces = ''
    elif r + 1 < middle:
        spaces_count = int((size - (r + 1)) / 2)
        spaces = ' ' * spaces_count
        stars_count = (size - spaces_count)
        stars = '*' * stars_count
    elif r + 1 > middle:
        stars_count = size - (r + 1)
        stars = '*' * spaces_count
        spaces_count = int((size - spaces_count) / 2)
        spaces = ' ' * stars_count

    print(spaces + stars + spaces)


# Task 3

a = int(input("Enter var a: "))
b = int(input("Enter var b: "))

if a < b:
    r = range(a, b + 1)
else:
    r = range(b, a + 1)

even_count = 0
for val in r:
    if val % 2 == 0:
        even_count += 1

print(even_count)


# Task 4

def uppercase_last_letter(sting):
    words = sting.split()
    new_string = ""
    for w in words:
        new_string += w[:-1] + w[-1].upper() + ' '

    return new_string


s = uppercase_last_letter("Some test string")
print(s)


# Task 5

numbers = input("Enter numbers: ")
numbers = [int(n) for n in numbers.split()]


def numbers_sum(piece):
    if len(piece) == 0:
        return 0
    else:
        return piece[0] + numbers_sum(piece[1:])


sum = numbers_sum(numbers)
print(sum)


# Task 6

words1 = input("Enter words 1 set (divided by spaces): ")
words2 = input("Enter words 2 set (divided by spaces): ")

words1 = set([w for w in words1 if w != ' '])
words2 = set([w for w in words2 if w != ' '])


common_words = words1.intersection(words2)
count_common_words = len(common_words)

print(common_words, count_common_words)


# Task 7

a = float(input("Enter side a len: "))
b = float(input("Enter side b len: "))
c = float(input("Enter side c len: "))

different_val_set = {a, b, c}


if len(different_val_set) < 3:
    l = [a, b, c]
    l.sort()
