print("Q1")
i = 0
while True:
    i += 1
    if i > 5: break
    print("*" * i)
print()

print("Q2")

A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
for num in A:
    total += num
average = total / len(A)
print(average)