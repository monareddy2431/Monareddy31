# Simple Job Portal in Python

jobs = [
    "Python Developer",
    "Software Engineer",
    "Data Analyst"
]

print("===== JOB PORTAL =====")

for i in range(len(jobs)):
    print(i + 1, ".", jobs[i])

choice = int(input("\nEnter Job Number to Apply: "))

if 1 <= choice <= len(jobs):
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    mobile = input("Enter Mobile Number: ")

    print("\n===== APPLICATION SUCCESSFUL =====")
    print("Name     :", name)
    print("Email    :", email)
    print("Mobile   :", mobile)
    print("Applied  :", jobs[choice - 1])
else:
    print("Invalid Job Number")
