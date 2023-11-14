# Conditionals: if, else if, elif, 

age = int(input("Enter the age: "))

if age >= 18:
    print("You are adult, You can vote")
elif age >=3 and age < 18:
    print("You cannot vote, You are in School")
else:
    print("You are a kid now!")

