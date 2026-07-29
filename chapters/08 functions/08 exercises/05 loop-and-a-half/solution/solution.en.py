def getInteger(prompt):

    """
    Ask for an integer using the given prompt, retrying for as long as the
    user does not enter a valid integer. (This is pcinput.getInteger().)
    """

    while True:
        try:
            number = int(input(prompt))
        except ValueError:
            print("That is not an integer -- please try again")
            continue
        return number


def get_valid_number(prompt):

    """
    Ask for an integer using the given prompt, and keep asking until the
    user enters a value between 0 and 1000 (inclusive).
    """

    while True:
        number = getInteger(prompt)
        if 0 <= number <= 1000:
            return number
        print("The numbers should be between 0 and 1000")


def main():

    while True:
        x = get_valid_number("Enter number 1: ")
        if x == 0:
            break
        y = get_valid_number("Enter number 2: ")
        if y == 0:
            break
        if x % y == 0 or y % x == 0:
            print("Error: the numbers cannot be dividers")
            return
        print("Multiplication of", x, "and", y, "gives", x * y)

    print("Goodbye!")


if __name__ == '__main__':
    main()
