# Strings
# The methods we are using on strings is not do any change on original strings give new strings

name = "Tony Stark"

print(name.upper())
print(name.lower())

# find the character and give its index number
print(name.find('S'))

print(name.find('Stark'))

#Replace the strings, substrings, chracters
print(name.replace('Stark', 'Ironman'))

# if we want to check any string present in variable
print('S' in name)

#but not do chahge in original its static
print(name)