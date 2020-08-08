# Write your code here
import random

class rock_paper_scissors:
    def __init__(self):
        self.human_play = None
        self.greet_player()
        rating = int(self.set_rating(self.greet_player))
        moves = self.set_plays()
        options = moves + ['!exit', '!rating']
        print("\nOkay, let's start")

        while self.human_play != '!exit':
            self.human_play = self.u_move()
            if self.human_play not in options:
                print("Invalid input")
                continue
            if self.human_play == '!rating':
                print("Your rating: " + str(rating))
                continue
            if self.human_play == '!exit':
                continue
            self.comp_play = self.c_move(moves)
            self.winner = self.outcome(self.human_play, self.comp_play, moves)
            if self.winner == "loss":
                rating += 0
            elif self.winner == "win":
                rating += 100
            elif self.winner == "draw":
                rating += 50

            self.announce(self.winner)
        print("Bye!")

    def greet_player(self):
        player = input("Enter your name: ")
        print("Hello, ", player, "\n")
        return player

    def set_rating(self, name):
        rating = "0"
        try:
            file = open('rating.txt', 'r')
            for line in file:
                if name in line:
                    rating = line.split()[1]
        finally:
            return rating


    def set_plays(self):
        options = input().split(",")
        if len(options) < 2:
            options = ["scissors", "rock", "paper"]
        return options


    def u_move(self):
        move = input()
        return move


    def c_move(self, moves):
        move = random.choice(moves)
        return move

    def outcome(self, h_move, c_move, moves):
        num_against = len(moves) // 2
        beats = []
        bows = []
        ind = moves.index(h_move)
        other_options = moves[ind + 1:] + moves[:ind]
        beats = other_options[num_against:]
        bows = other_options[:(num_against)]
        #print(other_options)
        #print(h_move + " beats " + ", ".join(beats))
        #print(h_move + " loses to " + ", ".join(bows))
        #print(c_move)
        if c_move in beats:
            return "win"
        elif c_move in bows:
            return "loss"
        else: return "draw"


    def announce(self, result):
        if result == "loss":
             print(f"Sorry, but computer chose {self.comp_play}")
        if result == "win":
            print(f"Well done. Computer chose {self.comp_play} and failed")
        if result == "draw":
            print(f"There is a draw {self.human_play}")


game = rock_paper_scissors()
