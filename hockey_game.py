import random

class HockeyGame:
    def __init__(self, rounds):
        self.rounds = rounds
        self.player1_name = input("Enter Player 1's name: ")
        self.player2_name = input("Enter Player 2's name: ")
        self.player1_score = 0
        self.player2_score = 0

    def shoot(self, player_name):
        input(f"{player_name}, press Enter to shoot...")
        shot_result = random.choice(['Goal!', 'Missed.'])
        print(shot_result)
        return shot_result == 'Goal!'

    def play_round(self, round_num):
        print(f"\nRound {round_num}:")

        # Player 1's turn
        player1_goal = self.shoot(self.player1_name)
        if player1_goal:
            self.player1_score += 1
            print(f"{self.player1_name} scores!")

        print(f"Score: {self.player1_name} - {self.player1_score}, {self.player2_name} - {self.player2_score}")

        # Player 2's turn
        player2_goal = self.shoot(self.player2_name)
        if player2_goal:
            self.player2_score += 1
            print(f"{self.player2_name} scores!")

        print(f"Score: {self.player1_name} - {self.player1_score}, {self.player2_name} - {self.player2_score}")

    def play_overtime(self):
        print("\nOvertime! Each player takes turns shooting until someone scores.")
        while True:
            # Player 1's turn
            player1_goal = self.shoot(self.player1_name)
            if player1_goal:
                self.player1_score += 1
                print(f"{self.player1_name} scores!")
                break

            # Player 2's turn
            player2_goal = self.shoot(self.player2_name)
            if player2_goal:
                self.player2_score += 1
                print(f"{self.player2_name} scores!")
                break

            print("No goals yet. Another round of overtime!")

    def play_game(self):
        print("\nWelcome to the Hockey Game!")
        print(f"Each player takes turns shooting. The player with the highest score after {self.rounds} rounds wins.")

        for round_num in range(1, self.rounds + 1):
            self.play_round(round_num)

            # Check for tie after regular rounds
            if self.player1_score == self.player2_score and round_num == self.rounds:
                print("It's a tie! Going into overtime.")
                self.play_overtime()
                print("\nOvertime Result:")
                print(f"Score: {self.player1_name} - {self.player1_score}, {self.player2_name} - {self.player2_score}")

        print("\nGame Over!")

        if self.player1_score > self.player2_score:
            print(f"{self.player1_name} wins!")
        elif self.player2_score > self.player1_score:
            print(f"{self.player2_name} wins!")
        else:
            print("It's still a tie! What an intense game.")


if __name__ == "__main__":
    while True:
        try:
            num_rounds = int(input("Enter the number of rounds: "))
            if num_rounds > 0:
                game = HockeyGame(num_rounds)
                game.play_game()
            else:
                print("Please enter a positive number of rounds.")
        except ValueError:
            print("Invalid input. Please enter a valid number of rounds.")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Good Game!")
            break
