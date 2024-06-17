import secrets


def generate_password(len_password):
    sequence_map = {
        "lower_case": "abcdefghijklmnopqrstuvwxyz",
        "upper_case": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "numbers": "0123456789",
    }

    password_output = ""

    for i in range(len_password):
        sequence = secrets.choice(list(sequence_map.keys()))
        password_output += secrets.choice(sequence_map[sequence])

    return password_output


def main():
    try:
        user_input = input("Enter password length: ")
        password = generate_password(int(user_input))

        if password:
            print(f'Passowrd: "{password}"')

    except ValueError:
        print("PLEASE ENTER A VALID NUMBER.")


main()
