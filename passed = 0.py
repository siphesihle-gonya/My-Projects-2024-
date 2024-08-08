passed = 0
failed = 0
students = 0

while students<10:
    grade = int(input())
    if grade >=50:
        passed = passed + 1
    else:
        failed = failed + 1
    students = students+1
print("passed",passed)
print("Failed",failed)
if passed > 8:
    print("BONUS to lecturer")
