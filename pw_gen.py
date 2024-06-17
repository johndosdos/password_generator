def generate_password(len_password):
    sequence_map = {
        "lower_case": "abcdefghijklmnopqrstuvwxyz",
        "upper_case": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "numbers": "0123456789",
    }

    password_output = ""


def main():
    password = generate_password(5)
    print(password)


main()
