import secrets
import string


def intro():
    print(
        """
 ========================================= 
|    _ ____      __     __ _  ___ _ __    |
|   | '_ \ \ /\ / /    / _` |/ _ \ '_ \   |
|   | |_) \ V  V /    | (_| |  __/ | | |  |
|   | .__/ \_/\_/      \__, |\___|_| |_|  |
|   | |                 __/ |             |
|   |_|                |___/              |
 =========================================
"""
    )


def generate_password(len_password):
    sequence_map = {"0": string.ascii_letters, "1": string.digits}

    password_output = ""

    dash_counter = 0

    for i in range(len_password):
        sequence = secrets.choice(list(sequence_map.keys()))
        password_output += secrets.choice(sequence_map[sequence])

        dash_counter += 1

        # for every 4 characters, we append a dash
        if dash_counter % 4 == 0 and i < len_password - 1:
            password_output += "-"
            dash_counter = 0

    return password_output


def main():
    intro()

    min_pw_length = 8

    while True:
        try:
            user_input = input("Please enter desired password length: ")
            if int(user_input) >= min_pw_length:
                password = generate_password(int(user_input))

                if password:
                    print(f" Password: {password}")
                    break
                else:
                    print(" Password generation failed.")
            elif int(user_input) < 1:
                print(" Error: Password could not be less than 0")
            else:
                print(f" Try Again. Required minimum characters: {min_pw_length}")

        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    main()
