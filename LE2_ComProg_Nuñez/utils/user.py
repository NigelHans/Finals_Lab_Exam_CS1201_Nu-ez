from utils.user_manager import UserManager
from utils.dice_game import DiceGame

class User:
    def __init__(self, username, password, match_file, score_file):
        self.username = username
        self.password = password
        self.match_file = match_file
        self.score_file = score_file

    def register(self):
        username = input("Enter Your Username: ")
        password = input("Enter Your Password: ")
        cpassword = input("Confirm Your Password: ")

        user_accounts = UserManager.load_users()

        while True:
            if password != cpassword:
                print("Passwords do not match. Please try again.")
                self.register()
                return

            if not UserManager.validate_username(username, user_accounts):
                username = input("Enter Your Username: ")
                continue
            if not UserManager.validate_password(password):
                password = input("Enter Your Password: ")
                continue

            user_accounts[username] = (password, 0)
            UserManager.save_users(user_accounts)
            print("Registered Successfully!")
            self.menu()
            return

    def login(self):
        user_accounts = UserManager.load_users()

        if not user_accounts:
            print("No user accounts found. Please register first.")
            self.register()
            return

        while True:
            username = input("Enter Your Username: ")
            password = input("Enter Your Password: ")

            if username in user_accounts and user_accounts[username][0] == password:
                print("Successfully Logged In!")
                game_instance = DiceGame(self.match_file, self.score_file)
                game_instance.play_game()
                break
            else:
                print("Invalid username or password. Please try again.")

    def logout(self):
        print("Press 1 if you want to Stay")
        print("Press 2 if you want to Exit")
        choice = input("Enter Your Choice: ")

        if choice == "1":
            self.menu()
        elif choice == "2":
            print("Exiting program.")
            return

    def menu(self):
        print("Welcome to the Dice Game Menu!")
        print("1. Register")
        print("2. Login")
        print("3. Logout")
        choice = input("Enter your choice: ")
        if choice == "1":
            self.register()
        elif choice == "2":
            self.login()
        elif choice == "3":
            self.logout()
        else:
            print("Invalid choice. Please try again.")
            self.menu()