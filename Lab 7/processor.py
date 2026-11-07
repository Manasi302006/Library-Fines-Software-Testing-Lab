
def parse_member_id(member_id):
    if not isinstance(member_id, str) or not member_id.strip():
        raise ValueError("Member ID must be a non-empty string")

    parts = member_id.split('-')

    if len(parts) != 2 or not parts[0].strip() or not parts[1].strip():
        raise ValueError("Invalid member ID format")

    try:
        number = int(parts[1])
    except ValueError:
        raise ValueError("Member ID number must be an integer")

    return parts[0].strip().upper(), number


def total_fine(days_csv):
    if not isinstance(days_csv, str) or not days_csv.strip():
        raise ValueError("Days must be provided as CSV text")

    try:
        days = [int(d.strip()) for d in days_csv.split(',')]
    except ValueError:
        raise ValueError("Days must contain valid integers")

    if any(d < 0 for d in days):
        raise ValueError("Days cannot be negative")

    fine = 0

    for d in days:
        if d > 14:
            fine += (d - 14) * 2

    return fine


def shelf_code(title):
    if not isinstance(title, str):
        raise ValueError("Title must be a string")

    words = title.split()

    if len(words) < 2:
        raise ValueError("Title must contain at least two words")

    return (words[0][0] + words[1][0]).upper()


def main():
    print("==== Running parse_member_id ====")
    user_input = input("Enter a member ID (e.g. STU-1023): ")
    result = parse_member_id(user_input)
    print("Member Type and Number:", result)

    print("\n==== Running total_fine ====")
    user_input = input("Enter days kept for each book as CSV (e.g. 10,20,30): ")
    result = total_fine(user_input)
    print("Total Fine:", result)

    print("\n==== Running shelf_code ====")
    user_input = input("Enter a book title with at least two words: ")
    result = shelf_code(user_input)
    print("Shelf Code:", result)


if __name__ == "__main__":
    main()
