def count():
    yield 1
    yield "two"
    yield 3

print("Printing nexts on count")
c = count()
print(next(c))
print(next(c))
print(next(c))
print(next(c, "não há mais"))
print(next(c, "não há mais"))
print(next(c, "não há mais"))
print(next(c, "não há mais"))

# print("Printing nexts on count without object")
# print(next(count()))
# print(next(count()))
# print(next(count()))
# print(next(count()))

# with open("file.txt") as file:
#     print(file.read())