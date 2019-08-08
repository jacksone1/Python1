import sys

Q1 = input("What, is your name")
Q2 = input("What, is your quest?")
Q3 = input("What, is the average air speed velocity of an unlaiden swallow?")

A1 = input( Q1 + ", do you choose rock, paper, or scissors")
A2 = input( Q2 + ", do you choose rock, paper, or scissors")

def compare(Q1, Q2, A1, A2):
    if A1 == A2:
        return("It's a tie!")

    elif A1 == "rock":
        if A2 == "scissors":
            return( Q1 + " wins!")
        else:
            return( Q2 + " wins!")

    elif A1 == "scissors":
        if A2 == "paper":
            return (Q1 + " wins!")
        else:
            return (Q2 + " wins!")

    elif A1 == "paper":
        if A2 == "rock":
            return (Q1 + " wins!")
        else:
            return (Q2 + " wins!")
    else:
        return("Invalid input! Please enter rock, paper, or scissors and try again!")

print( compare(Q1, Q2, A1, A2) )