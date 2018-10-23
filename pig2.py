#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS211 Assignment8 - A simple game called Pig - Tested in Python 2.7.15
   The objective of the game is to reach 100 points or more before the other player.
   If  you are playing a timed game.  Time is set to 60 seconds.
   If 60 seconds is reach and no one has reached 100 points, the player
   with higher score wins the game.  
   ***************************************************************************
   To start a timed game with player 1 as human and player 2 as computer,
   please type: pig2.py --player1 human --player2 computer --timed yes
   ***************************************************************************
   To start a timed game with player 1 as computer and player 2 as computer,
   please type: pig2.py --player1 computer --player2 computer --timed yes
   ***************************************************************************
   To start a timed game with player 1 as human and player 2 as human,
   please type: pig2.py --player1 human --player2 human --timed yes
   ***************************************************************************
   If you don't want to play a time game, type:  --timed no
   ***************************************************************************
   Every time a player rolled from 2 to 6, the terminal color will stay green.
   If the player rolled a 1, the terminal text will display red.
"""

import argparse
import random
import time

class Player:

    def __init__(self, identity):

        self.identityvar = identity
        self.scorevar = 0     
        self.tempscorevar = 0    
        self.tempscorevarPrev = 0   
        self.iswinvar = False

    def identity(self):

        return self.identityvar

    def score(self):

        return self.scorevar

    def subtract_from_score(self, sub):

        self.scorevar -= sub

    def previous_hold_score(self):

        return self.tempscorevarPrev

    def is_winner(self):

        return self.iswinvar

    def make_winner(self):

        self.iswinvar = True

    def roll_die(self):
        random.seed(time.time())
        current_roll = int(random.random() * 6) + 1
        self.tempscorevar += current_roll

        if current_roll == 1:
            print ("\x1b[31m\"You have rolled a 1.  Sorry, no points will be added and you lose your turn.\n\x1b[0m")

        elif current_roll == 2:
            
            print ("\x1b[32m\"Player %i, you have rolled a 2. \n\n" \
                  "Current turn rolled up score is: %i\n \n\x1b[0m") % (self.identity(), self.tempscorevar)

        elif current_roll == 3:
            print ("\x1b[32m\"Player %i, you have rolled a 3 \n\n" \
                  "Current turn rolled up score is: %i\n \n\x1b[0m") % (self.identity(), self.tempscorevar)

        elif current_roll == 4:
            print ("\x1b[32m\"Player %i, you have rolled a 4 \n\n" \
                  "Current turn rolled up score is: %i\n \n\x1b[0m") % (self.identity(), self.tempscorevar)

        elif current_roll == 5:
            print ("\x1b[32m\"Player %i, you have rolled a 5 \n\n" \
                  "Current turn rolled up score is: %i\n \n\x1b[0m") % (self.identity(), self.tempscorevar)

        elif current_roll == 6:
            print ("\x1b[32m\"Player %i, you have rolled a 6 \n\n" \
                  "Current turn rolled up score is: %i\n \n\x1b[0m") % (self.identity(), self.tempscorevar)

        return current_roll


    def decide(self, rolled_value):

        if rolled_value == 1:
            self.tempscorevar = 0
            print "The Player %i has a score of %i\n\n" % \
                  (self.identity(), self.scorevar)
            return 1

        if self.tempscorevar + self.scorevar >= 100:
            print "Total points      : %i" % \
                  (self.tempscorevar+self.scorevar)
            print "********************\nPlayer %i has won the game" \
                  "********************" % (self.identity(),
                                            self.tempscorevar+self.scorevar)
            self.iswinvar = True
            return 0

        decision = raw_input("Type 'r' for roll and 'h' for hold. ")

        while decision != "r" and decision != "h":
            decision = raw_input("Error. Please only type 'r' for roll "
                                 "and 'h' for hold.  ")

        if decision == "h":
            self.scorevar += self.tempscorevar
            self.tempscorevarPrev = self.tempscorevar
            self.tempscorevar = 0
            print "Player %i's score is %i\n\n" \
                  "*************************\n" \
                  "  PLEASE SWITCH PLAYER.  \n" \
                  "*************************\n\n" \
                  % (self.identity(), self.scorevar)
            return 2

        if decision == "r":
            return 3

class ComputerPlayer(Player):

    def decide(self, rolled_value):

        if rolled_value == 1:
            self.tempscorevar = 0
            print "Player %i current score is %i\n" % \
                  (self.identity(), self.scorevar)
            return 1

        if self.tempscorevar+self.scorevar >= 100:
            print ("\x1b[93;32m\n************************************************************\n" \
                         "Player %i has reached a score of %i points and won the game!  \n" \
                         "************************************************************\n" \
                         "\x1b[0m ") % (self.identity(), self.tempscorevar+self.scorevar)
            self.iswinvar = True
            return 0

        decision = "h"

        if (100 - self.scorevar) >= 25:
            if self.tempscorevar < 25:
                decision = "r"
        else:
            if self.tempscorevar < (100 - self.scorevar):
                decision = "r"

        if decision == "h":
            print "Computer player selected H to Hold. \n\n" 
            self.scorevar += self.tempscorevar
            self.tempscorevarPrev = self.tempscorevar
            self.tempscorevar = 0
            print "The player %i score is %i\n" \
                  "*************************\n" \
                  "  PLEASE SWITCH PLAYER.  \n" \
                  "*************************\n" \
                  % (self.identity(), self.scorevar)
            return 2

        if decision == "r":
            print "Computer player selected r to Roll. \n"
            return 3

        print ""


class PlayerFactory:

    def get_player(self, identity, type_of_player):

        if type_of_player == "computer":
            return ComputerPlayer(identity)

        if type_of_player == "human":
            return Player(identity)


class Game:
 
    def __init__(self, player1, player2):

        self.listOfPlayers = []
        self.listOfPlayers.append(player1)
        self.listOfPlayers.append(player2)

    def number_of_players(self):

        return len(self.listOfPlayers)

    def player_list(self):

        return self.listOfPlayers

    def roll_game_die(self, player):

        return player.roll_die()

    def decide(self, roll_die_value, player):

        return player.decide(roll_die_value)

    def reset_game(self):

        for x in range(0,len(self.listOfPlayers)):
            self.listOfPlayers.pop()


class TimedGameProxy(Game):

    def __init__(self, playerA, playerB):

        self.listOfPlayers = []
        self.startTime = time.time()
        self.listOfPlayers.append(playerA)
        self.listOfPlayers.append(playerB)


    def start_game(self):

        winner = 0
        result = 3
        exists_no_winner = True

        while exists_no_winner and (60 - (time.time()-self.startTime)) > 0:

            for player in self.listOfPlayers:

                print "*********************************\nPLAYER %i currently has %i points\n" \
                "*********************************\n" % (player.identity(), player.score())

                while result == 3:
                    print "\nThere are %f seconds left on the timer. \n" % (60 - (time.time()
                                                      -self.startTime))
                    if (60 - (time.time()-self.startTime)) < 0:
                        result = 4
                        print "Sorry, time is up!\n"
                        break
                    else:
                        resulting_face = self.roll_game_die(player)

                    print "There are %f seconds left on the timer. \n" % (60 - (time.time()
                                                      -self.startTime))
                    if (60 - (time.time()-self.startTime)) < 0:
                        result = 4
                        print "The game has ended"
                        break
                    else:
                        result = self.decide(resulting_face, player)

                        if (60 - (time.time()-self.startTime)) < 0:
                            print "Time limit has reached.  Game is now finished!\n"


                            if result == 2:
                                prev_score = player.previous_hold_score()
                                overtime = (time.time()-self.startTime) - 60
                                print "%i points cannot be add because time limit has been reached. \n\n" \
                                      "The game is already over by %f seconds\n" % (prev_score, overtime)
                                player.subtract_from_score(
                                    player.previous_hold_score())

                            result = 4
                            break

                if result == 4:
                    if self.listOfPlayers[0].score() > \
                            self.listOfPlayers[1].score():
                        self.listOfPlayers[0].make_winner()
                        winner = "1"
                    elif self.listOfPlayers[0].score() < \
                            self.listOfPlayers[1].score():
                        self.listOfPlayers[1].make_winner()
                        winner = "2"
                    else:
                        self.listOfPlayers[0].make_winner()
                        self.listOfPlayers[1].make_winner()
                        winner = "1 & 2"
                    exists_no_winner = False
                    print ("\x1b[93;32m\n************************************\n  Player %s has won the game!  \n" \
                          "************************************\x1b[0m" \
                          "\nPlayer 1 final score is: %i\nPlayer 2 final score is: %i") % \
                          (winner, self.listOfPlayers[0].score(), self.listOfPlayers[1].score())
                    break

                if result == 0:
                    exists_no_winner = False
                    break

                result = 3


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--player1", help="Indicate if player 1 is 'human'"
                                          " or 'computer'.")
    parser.add_argument("--player2", help="Indicate if player 2 is 'human'"
                                          " or 'computer'.")
    parser.add_argument("--timed", help="Indicate if game is timed to 60"
                                        " seconds. Type 'yes' or 'no'.")

    args = parser.parse_args()

    try:
        player1_choice = args.player1.lower()
        player2_choice = args.player2.lower()
        timed_game = args.timed.lower()

    except AttributeError:
        print "Please type 'human' or 'computer' for players and 'yes' or 'no' if you want a 60 seconds timed game."
        exit(1)

    if player1_choice != "human" and player1_choice != "computer":
        print "Please type 'human' or 'computer' for --player1."
        exit(1)
    if player2_choice != "human" and player2_choice != "computer":
        print "Please type type 'human' or 'computer' for --player2."
        exit(1)
    if timed_game != "yes" and timed_game != "no":
        print "Please type 'yes' or 'no' for --timed. "
        exit(1)

    factory = PlayerFactory()
    player1 = factory.get_player(1, player1_choice)
    player2 = factory.get_player(2, player2_choice)

    print ("\x1b[93;47mWELCOME TO THE PIG GAME\x1b[0m")

    if timed_game == "yes":
        print "Timed game has been selected. \n" \
        "The game will end in 60 seconds \n" \
        "The player with the higher score is the winner if no one reaches 100 points or more before time runs out.\n" 
        
        timed_game = TimedGameProxy(player1, player2)
        timed_game.start_game()
        timed_game.reset_game()

    elif timed_game == "no":
        game1 = Game(player1, player2)

        exists_no_winner = True
        result = 3

        while exists_no_winner:

            for player in game1.player_list():
                print "**********************\nPLAYER %i has %i points" \
                      "\n**********************" % \
                      (player.identity(), player.score())

                while result == 3:
                    resulting_face = game1.roll_game_die(player)
                    result = game1.decide(resulting_face, player)

                if result == 0:
                    exists_no_winner = False
                    break

                result = 3

        game1.reset_game()

    print "\nThank you for playing. \n \n" \
          "The game will now exit. \n \n" \
          "GODD BYE!\n"

if __name__ == "__main__":
    main()
