#!/usr/bin/python

import sys


def rock_paper_scissors(n):
  # define a list with all of the possible plays.
    choices = ['rock', 'paper', 'scissors']
  # define empty list to return the possible combinations
    possible_plays = []
  # inner recursive function to handle passing of data

    def rps_helper(result, rounds):
        if rounds == 0:  # Base case to stop if the amount of rounds is 0
            # append the result of inner function to the outer empty array
            possible_plays.append(result)
            return

        for i in range(0, len(choices)):  # Looping over the length of the possible choices
            # recursing while passing in the results and rounds decrementing
            rps_helper(result + [choices[i]], rounds - 1)

    rps_helper([], n)
    return possible_plays


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
