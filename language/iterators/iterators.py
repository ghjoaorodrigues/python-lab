nums = [1, 2, 3]

print("Printing nums directly")
print(nums)
print("")

# print("Printing iterator")
# it = iter(nums)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it, "list end"))
# print(next(it, "list end"))
# print(next(it, "list end"))
# print("")

print("Printing nums through for loop in iterator")
it = iter(nums)
next(it)
for n in it:
    print(n)


