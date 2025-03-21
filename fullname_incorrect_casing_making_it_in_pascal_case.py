fullname = str(input("Enter your name: "))

pascal_case = fullname.replace("_", " ").title().replace(" ", "")

print(pascal_case)