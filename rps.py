#!/usr/bin/env python3
import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def __init__(self):
        self.self_moves = []
        self.opponent_moves = []
        self.roundNum = 0

    def move(self):
        return "rock"
        

    def learn(self, my_move, their_move):
        self.self_moves.append(my_move)
        self.opponent_moves.append(their_move) 
        self.roundNum += 1
        #print(self.self_moves, self.opponent_moves, self.roundNum)
        return


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))

#Selects a random move from RPS
class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)

#Reads input from the user for RPS
class HumanPlayer(Player):
    def move(self):
        choice = input("Type rock, paper or scissors ").lower()
        while choice != "rock" and choice != "paper" and choice != "scissors":
            choice = input("Invalid input, please type rock, paper or scissors: ").lower()
        return choice

#Picks the last move from the oponent to use in current round
class ReflectPlayer(Player):
    def move(self):
        if len(self.opponent_moves):
            return self.opponent_moves[-1]
        else:
            return "rock"

#cycles through rock paper and scissors
class CyclePlayer(Player):
    def move(self):
        global moves
        return moves[self.roundNum % len(moves)]
      
        # code under will produce an error when game is played over 3 times, that is why % is used instead. (reminder code above is of more effecent and not error/bug prone )
        # remainder = self.roundNum % len(moves)
        
        # if self.roundNum == 0:
        #     return 'rock'
        # elif self.roundNum == 1:
        #     return 'paper'
        # elif self.roundNum == 2:
        #     return 'scissors'



class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_tally = 0
        self.p2_tally = 0
      

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        #print(move1,move2)
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if beats(move1,move2):
            self.p1_tally += 1
            # print("Player 1:" "{move1}")

        elif beats(move2,move1):
            self.p2_tally +=1
            # print("Player 2:" "{move2}")
        
        else:
            "Tie round"

        print()
        print("You have",self.p1_tally,"wins")
        print("The computer has",self.p2_tally,"wins")
        print()

    def play_game(self):
        print("Game start!")
        for round in range(5):
            print(f"Round {round}:")
            self.play_round()

        # print(self.p1_tally)
        # print(self.p2_tally)
        print()
        print("Game over!")



game = Game(HumanPlayer(), RandomPlayer())
game.play_game()

play_game = True
while play_game:
  repeat = input("Play again? (Y/N) ").lower()
while repeat != "n" and repeat != "y":
  repeat = input("Invalid input, please try again: ").lower()
        
  while repeat == "n":
    play_game = False
    break