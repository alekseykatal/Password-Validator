def askPassword(initials):
    specialchar = "!@#$%^"

    while True:
        sPassword = input("Enter new password: ")
        issues = []

        iUpperCount = iLowerCount = iNumericCount = iSpecialCount = 0
        charcount = {}

        # Check the password length first
        if not (8 <= len(sPassword) <= 12):
            issues.append("Password must be between 8 and 12 characters.")

        # checks conditions
        for sLetter in sPassword:
            if sLetter.isupper():
                iUpperCount += 1
            elif sLetter.islower():
                iLowerCount += 1
            elif sLetter.isdigit():
                iNumericCount += 1
            elif sLetter in specialchar:
                iSpecialCount += 1

            # Count each ocur of char
            lowerchar = sLetter.lower()
            charcount[lowerchar] = charcount.get(lowerchar, 0) + 1

        # Validate all the password requirements after the loop
        if iUpperCount == 0:
            issues.append("Password must contain at least 1 uppercase letter.")
        if iLowerCount == 0:
            issues.append("Password must contain at least 1 lowercase letter.")
        if iNumericCount == 0:
            issues.append("Password must contain at least 1 number.")
        if iSpecialCount == 0:
            issues.append("Password must contain at least 1 of these special characters: !@#$%^.")

        # checks for pass
        if sPassword[:4].lower() == "pass":
            issues.append("Password can't start with Pass.")

        # checks for initials
        if initials.lower() in sPassword.lower():
            issues.append("Password must not contain user initials.")

        # Check for repeated characters
        repeatedchar = {char: count for char, count in charcount.items() if count > 1}
        if repeatedchar:
            issues.append("These characters appear more than once:")
            for char, count in repeatedchar.items():
                issues.append(f"{char}: {count} times")

        # Return the password if no issues were found
        if not issues:
            return sPassword
        else:
            # Print any issues found
            for issue in issues:
                print(issue)


def askName():
    # Ask for full name and ensure it contains exactly one space
    while True:
        sName = input("Enter full name (e.g., John Smith): ").strip()
        if sName.count(' ') == 1:
            first, last = sName.split(' ', 1)
            initials = first[0].upper() + last[0].upper()  # Get initials
            return sName, initials
        print("Please enter a valid full name.")


def main():
    # Get the user's name and initials
    name, initials = askName()
    print(f"Name: {name}")
    print(f"Initials: {initials}")

    # Ask for password and validate it
    askPassword(initials)
    print("Password is valid and OK to use.")


main()
