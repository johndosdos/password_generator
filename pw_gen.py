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
    password = generate_password(5)
    print(password)


main()
