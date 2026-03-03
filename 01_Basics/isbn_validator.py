"""
Project: ISBN-10 Validator
Description: Validates a 10-digit ISBN number
"""

def is_valid_isbn(isbn):
    # Check length
    if len(isbn) != 10:
        print("Invalid ISBN length ")
        return

    sum_total = 0

    for i in range(10):
        ch = isbn[i]

        if not ch.isdigit():
            print("Invalid ISBN ")
            return

        sum_total += int(ch) * (10 - i)

    if sum_total % 11 == 0:
        print("Valid ISBN ")
    else:
        print("Invalid ISBN ")


def main():
    isbn = input("Enter 10-digit ISBN: ")
    is_valid_isbn(isbn)


if __name__ == "__main__":
    main()