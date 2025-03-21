number = int(input("Enter a number (0-1000): "))

if 0 <= number <= 1000:
    fomatted_number = f"{number:06}"

    print("Output:", fomatted_number)

else:
    print("Error: Put a number between 0-1000")
