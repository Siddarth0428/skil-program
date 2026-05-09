name = input("Enter student name: ")

m1 = int(input("Enter marks 1: "))
m2 = int(input("Enter marks 2: "))
m3 = int(input("Enter marks 3: "))

total = m1 + m2 + m3
avg = total / 3

print("Total Marks =", total)
print("Average =", avg)

if avg >= 90:
    print("Grade: A")
elif avg >= 75:
    print("Grade: B")
elif avg >= 50:
    print("Grade: C")
else:
    print("Grade: Fail")