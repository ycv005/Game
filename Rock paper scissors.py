def compare(player,c):
    print(player, 'vs', c)
    if player==c:
        print("Draw")
        return
    elif player=='r' and c=='p':
        print("Computer Wins!")
        return
    elif player=="r" and c=="s":
        print("You Wins!")
        return
    elif player=="p" and c=="r":
        print("You Wins!")
        return
    elif player=="p" and c=="s":
        print("Computer Wins!")
        return
    elif player=="s" and c=="p":
        print("You Wins!")
        return
    elif player=="s" and c=="r":
        print("Computer Wins!")
        return

from random import randint
print("Welcome to fight of the Rock, Paper and Scissor")
rules="""
Here is the rules of game-
Rock vs Scissor- Rock Wins
Paper vs Scissor- Scissor Wins
Rock vs Paper- Paper Wins
Enter 'r' for rock, 's' for scissors, and 'p' for paper
"""
print (rules)
player=input("Enter your choice: ")
player=player.lower()
if player!='r' or player!='s' or player!='p':
    print("Wrong Input")
    player=input("Enter your choice once again: ")
    player=player.lower()
print("Now computer's role")
c=randint(1,3)
if c==1:
    c='r'
elif c==2:
    c='s'
else:
    c='p'

compare(player,c)

