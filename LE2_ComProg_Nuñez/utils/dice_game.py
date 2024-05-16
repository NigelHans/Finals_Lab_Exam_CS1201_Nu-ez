import random
from utils.score import Score
from datetime import datetime

class DiceGame:
    def __init__(self, match_file, score_file):
        self.match_file = match_file
        self.score = Score(score_file)

    def match_history(self, user_points, computer_points):
        try:
            with open(self.match_file, 'a') as file:
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file.write(f"{current_time} - User Score: {user_points}, Computer Score: {computer_points}\n")
        except IOError:
            print('Error in saving match history')

    def display_top_scores(self):
        scores = self.score.load_scores()
        print("Top Scores:")
        for idx, score in enumerate(scores, start=1):
            print(f"{idx}. {score}")

    def play_game(self):
        while True:
            print("Welcome to Dice Game")
            print("1. Start Game")
            print("2. Top Scores")
            print("3. Logout")

            choice = int(input("Enter your Choice: "))
            if choice == 1:
                self.user_points = 0
                self.computer_points = 0
                while True:
                    choice = input("Enter P to Play or Q to Quit: ")
                    if choice.upper() == "P":
                        self.user_choice = random.randint(1, 6)
                        self.cpu_choice = random.randint(1, 6)
                        print(f'User got: {self.user_choice} and Computer got: {self.cpu_choice}')

                        if self.cpu_choice < self.user_choice:
                            print("You Win")
                            self.user_points += 1
                        elif self.cpu_choice == self.user_choice:
                            print("It's a Tie")
                        else:
                            print("CPU Wins")
                            self.computer_points += 1

                        print(f'Total Points, User: {self.user_points}, Computer: {self.computer_points}')
                        self.match_history(self.user_points, self.computer_points)
                    elif choice.upper() == "Q":
                        self.score.add_score(self.user_points)
                        break
            elif choice == 2:
                self.display_top_scores()
            elif choice == 3:
                return