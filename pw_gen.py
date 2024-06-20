import secrets
import string


def generate_password(len_password):
    sequence_map = {"0": string.ascii_letters, "1": string.digits}

    password_output = ""

    for i in range(len_password):
        sequence = secrets.choice(list(sequence_map.keys()))
        password_output += secrets.choice(sequence_map[sequence])

    return password_output


def main():
    try:
        while True:
            user_input = input("Enter password length: ")
            if int(user_input) >= 8:
                password = generate_password(int(user_input))

                if password:
                    print(f'Passowrd: "{password}"')
                    break
            else:
                print("REQUIRED MINIMUM CHARACTERS: 8")

    except ValueError:
        print("PLEASE ENTER A VALID NUMBER.")


if __name__ == "__main__":
    main()
