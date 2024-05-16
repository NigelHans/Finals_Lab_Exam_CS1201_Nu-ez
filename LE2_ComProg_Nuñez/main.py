from utils.user import User
import os

def check_files():
    files = ['match_file.txt', 'top_scores.txt', 'Users_Data.txt']
    for file in files:
        if not os.path.isfile(file):
            print(f"File {file} does not exist. Creating a new one.")
            open(file, 'a').close()

check_files()

def main():
    match_file = 'match_file.txt'
    score_file = 'top_scores.txt'

    user = User(username="", password="", match_file=match_file, score_file=score_file)

    while True:
        print("Welcome to the Main Menu!")
        print("1. User Menu")
        print("2. Exit") 
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            user.menu()
        elif choice == "2":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()