students = ["ram", "shyam", "Radha", "Radhika", "shamu"]

# Break the loop when condition is met
for i in students:
    if i == "Radhika":
        break
    print(i)

print("--------------------------")

# did not take the element which mention in condition
for j in students:
    if j == "Radha":
        continue
    print(j)

