import random
import string

print("=" * 50)
print("      RANDOM PASSWORD GENERATOR")
print("=" * 50)

passwords = []

# Load saved passwords
try:
    with open("passwords.txt", "r") as file:
        passwords = file.read().splitlines()
except FileNotFoundError:
    pass


def save_passwords():
    with open("passwords.txt", "w") as file:
        for password in passwords:
            file.write(password + "\n")


def generate_password():

    try:
        length = int(input("Enter Password Length: "))

        if length < 4:
            print("Password length should be at least 4.")
            return

        characters = (
            string.ascii_letters +
            string.digits +
            string.punctuation
        )

        password = ""

        for i in range(length):
            password += random.choice(characters)

        passwords.append(password)
        save_passwords()

        print("\n✅ Generated Password:")
        print(password)

    except ValueError:
     print("Invalid Length.")


def view_passwords():
    if len(passwords) == 0:
        print("\nNo Saved Passwords.")
    else:
        print("\n========== SAVED PASSWORDS ==========")
        for i, password in enumerate(passwords, start=1):
            print(f"{i}. {password}")


def delete_password():
    if len(passwords) == 0:
        print("No passwords available.")
        return

    view_passwords()

    try:
        num = int(input("\nEnter password number to delete: "))

        if 1 <= num <= len(passwords):
            removed = passwords.pop(num - 1)
            save_passwords()
            print(f"✅ '{removed}' deleted successfully!")

        else:
            print("❌ Invalid password number.")

    except ValueError:
        print("❌ Invalid input.")


def password_strength(password):

    score = 0

    if len(password) >= 8:
        score += 1

    if any(c.islower() for c in password):
        score += 1

    if any(c.isupper() for c in password):
        score += 1

    if any(c.isdigit() for c in password):
        score += 1

    if any(c in string.punctuation for c in password):
        score += 1

    if score <= 2:
        return "Weak 🔴"

    elif score == 3 or score == 4:
        return "Medium 🟡"

    else:
        return "Strong 🟢"


def check_strength():

    password = input("Enter Password: ")

    print("Password Strength:", password_strength(password))


def generate_multiple():

    try:
        count = int(input("How many passwords? "))
        length = int(input("Password Length: "))

        if length < 4:
            print("Password length should be at least 4.")
            return

        characters = (
            string.ascii_letters +
            string.digits +
            string.punctuation
        )

        print("\nGenerated Passwords:\n")

        for i in range(count):

            password = ""

            for j in range(length):
                password += random.choice(characters)

            passwords.append(password)
            print(password)

        save_passwords()

    except ValueError:
        print("Invalid Input.")
while True:

    print("\n" + "=" * 40)
    print("     RANDOM PASSWORD GENERATOR")
    print("=" * 40)
    print("1. Generate Password")
    print("2. View Saved Passwords")
    print("3. Delete Password")
    print("4. Check Password Strength")
    print("5. Generate Multiple Passwords")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        generate_password()

    elif choice == "2":
        view_passwords()

    elif choice == "3":
        delete_password()

    elif choice == "4":
        check_strength()

    elif choice == "5":
        generate_multiple()

    elif choice == "6":
        print("\n👋 Thank you for using Random Password Generator!")
        break

    else:
        print("❌ Invalid choice! Please enter a number between 1 and 6.")