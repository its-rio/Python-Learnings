# for loop on list 

marks = [54, 76, 98, 34, 89, 67, 98, 64]

for score in marks:
    print(score)

# while Loop
print("----------------------------------------")
# i = 0
# while i < len(marks):
#     print(marks[i])
#     i = i + 1

# List Operations

print(marks[0])
print(marks[1])

# Add element at last:
marks.append(23)
print(marks)

# Add element anywhre between:
marks.insert(1, 45)
print(marks)

# Check if element is exist or not gives us TRUE or FALSE
print(45 in marks)

# Length of list
print(len(marks))

# To empty whole list clear() is used
marks.clear()
print(marks)