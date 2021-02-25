import random
print("Do you want to toss by rock,paper,scissor or by odd&even\n")
print("For rock,paper,scissor type --Y-- & For Odd&even type --O--\n")
Q=input()
if Q == "Y":
    J=input("Enter what you choose\nType=Rock , paper , Scissor\n")
    print("\n")
    K=random.randint(0,2)
    if K == 0 :
        print("Rock")
        if J == "Rock":
            print("Its a tie")
        elif J == "paper":
            print("You win the game")
        elif J == "Scissor":
            print("Computer won the game")
    elif K == 1:
        print("paper")
        if J == "Rock":
            print("Computer won the game")
        elif J == "paper":
            print("Its a tie")
        elif J == "Scissor":
            print("You won the game")
    elif K == 2:
        print("Scissor")
        if J == "Rock":
            print("You won the game")
        elif J == "paper":
            print("Computer won the game")
        elif J == "Scissor":
            print("Its a Tie")
    else:
        print("Not Valid")
elif Q == "O":
    L=input("Which one do you wanna choose ODD or EVEN\n")
    J=int(input("Enter Any number from 1--10\n"))
    K=random.randint(1,10)
    print("Computer Chooses-->\n")
    print(K)
    R=K+J
    if R%2== 0:
        print("Its an EVEN")
        if L== "EVEN":
            print("You Won")
        else:
            print("You lost")
    else:
        print("Its an ODD")
        if L== "ODD":
            print("You Won")
        else:
            print("You lost")
