a = int(input("Your age: "))
b = input("Your status: ")
status_1 = "married"
status_2 = "unmarried"
if ((a >= 30) and (b == status_1)):
    print("You are emplyed for this job with free medical! ")
if ((a >= 30) and (b == status_2)):
    print("You are employed for this job with no medical! ")
if (a < 30):
    print("You are not aligible for this job! ")