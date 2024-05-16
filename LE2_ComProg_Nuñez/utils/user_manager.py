import os

class UserManager:
    @staticmethod
    def load_users():
        user_accounts = {}
        try:
            with open("Users_Data.txt", 'r') as file:
                for line in file:
                    username, password, points = line.strip().split(',')
                    user_accounts[username] = (password, int(points))
            print("Users Information loaded successfully.")
            return user_accounts
        except FileNotFoundError:
            print("Data not Found")
            return user_accounts

    @staticmethod
    def save_users(user_accounts):
            with open("Users_Data.txt", 'w') as file:
                for username, (password, points) in user_accounts.items():
                    file.write(f"{username},{password},{points}\n")
            print("Users saved successfully.")

    @staticmethod
    def validate_username(username, user_accounts):
        while True:
            if len(username) < 4:
                print("Username must be 4 characters and above")
                return False
            if username in user_accounts:
                print("Username not Found. Please Try Again!")
                return False
            return True

    @staticmethod
    def validate_password(password):
         while True:
            if len(password) < 4:
                print("Password must be 4 characters and above")
                password = input("Enter Your Password: ")
                continue
            return password

	