import random
#Number Guessing Game

#Variables
random_value=random.randint(1,100)
user_difficulty=None
user_life=0

#Greeting User
user_greet="Welcome to Guess It Right! "
print(user_greet)

#User-info
name_value=True
while name_value:
    user_name=input("Enter your name: ")
    user_name_len=len(user_name)
    if user_name_len==0:
        print("User name should be at least one Word ")
    else:
        name_value=False

#User-Difficulty
difficulty = True
while difficulty:
        user_difficulty=input("Select your difficulty 'easy' or 'hard': ").casefold()
        if not user_difficulty in ["easy" , "hard"]:
            print("Answer in 'easy' or 'hard' only,Try again")
        else:
            difficulty=False

if user_difficulty=="easy":
    print("You have 10 Maximum attempts to guess the number")
    user_life=10
else:
    print("You have 5 Maximum attempts to guess the number")
    user_life=5

print("\n////////////////////////////////////////////////////////////////  Let's Begin  ////////////////////////////////////////////////////////////////////////////\n")

game_=True
reduce_life = user_life
while game_:
    user_guess = int(input("Guess the number between 1-100 : "))
    def guessing_game(a, r ,l):
        global reduce_life
        if a==r :
            print(f"🎉Congratulations!,You Guessed It Right🎯 , it was {random_value}")
            global game_
            game_=False
        elif (r-5)<a<(r+5):
            print("Almost There")
            l -= 1
            reduce_life=l
            print(f"You have {l} chances left ")
        elif a<r:
            print("Too Low!")
            l -= 1
            reduce_life=l
            print(f"You have {l} chances left ")

        elif a>r:
            print("Too High!")
            l -= 1
            reduce_life=l
            print(f"You have {l} chances left ")

        if reduce_life<1:
             print(f"Oops! You lost this time! 😢,Try Again It was {random_value}")
             game_=False
    guessing_game(a=user_guess, r=random_value,l=reduce_life)




