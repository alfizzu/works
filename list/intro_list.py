expenses = [120,130,140,150,160]


print(expenses[0])
print(expenses[1])
print(expenses[4])
print(expenses[-1])
print("  ")

print("one approach")
for amount in expenses:
    print(amount)

print("  ")

print("another approach")
for i in range(0,5):
    print(expenses[i])