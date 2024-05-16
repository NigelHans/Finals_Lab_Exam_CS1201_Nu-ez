class Score:
    def __init__(self, points_file):
        self.points_file = points_file

    def load_scores(self):
        try:
            with open(self.points_file, 'r') as file:
                return [int(score.strip()) for score in file.readlines()]
        except FileNotFoundError:
            print("Score file not found. Using an empty list.")
            return []
        except ValueError:
            print('Invalid data in score file.')
            return []

    def save_scores(self, scores):
        try:
            with open(self.points_file, 'w') as file:
                for score in scores:
                    file.write(f"{score}\n")
        except IOError:
            print('Scores not saved!')

    def add_score(self, score):
        scores = self.load_scores()
        scores.append(score)
        scores.sort(reverse=True)
        scores = scores[:10]
        self.save_scores(scores)