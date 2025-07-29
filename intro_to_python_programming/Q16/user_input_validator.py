class UserInputValidator:
    def __init__(self) -> None:
        pass

    def user_input(self):
        try:
            age = int(input("Enter your age (1-120)? "))
            if 0 < age <= 120:
                return f"Valid age entered: {age}"
            else:
                return "Out of range. Please enter a number between 1 and 120."
        except:
            return "Invalid input. Please enter a valid number."

if __name__ == "__main__":
    userInputValidator1 = UserInputValidator()
    print(userInputValidator1.user_input())
