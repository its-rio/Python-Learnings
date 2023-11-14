first = int(input("Enter the number: "))
operator = input("Enter operrator (+,-,*,/,%)")
sec = int(input("Enter the number: "))

if operator == '+':
    print(first + sec)
elif operator == '-':
    print(first - sec)
elif operator == '*':
    print(first * sec)
elif operator == '/':
    print(first / sec)
elif operator == '%':
    print(first % sec)
else:
    print("Invalid Input")

