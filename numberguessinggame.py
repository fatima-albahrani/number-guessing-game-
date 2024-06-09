import random 
min = 1 
max = 100
attempt = 5
win = False 

number = random.randint(min , max)
last_hint = f"{ 'EVEN ' if number%2 == 0 else 'ODD'}"

def game_start():
    print(f"if you can guess the number that is between {min}  and {max} correctly within 5 attempts then you win")
    input("press enter to start the game ")

def game_play():
    global number , attempt , last_hint , win 


    while attempt > 0:
        print()
        print(f"you have {attempt} {'attempts ' if attempt > 1 else "attempt"} left ")

        if attempt == 1 :
            print(f"last chance , i'll give you a hint its an {last_hint} number ")

        while True :
             try:
                 guess = int(input("pick a number !"))
                 
                 if guess in range(min , max+1):
                  break
                 else :
                     print(f" enter a number between {min} and {max}")
             except ValueError:
                 print("enter numbers only !")

       
        if guess == number :
            win = True 
            break
        if attempt == 1:
         break

        if guess > number:
            if guess - number > 5:
                print("try smaller ")
            else :
                print( " very close ! , try smaller ")

        else:
            if number-guess > 5 :
                print("try bigger")
            else:
                print(" very close ! , try bigger")

        attempt -= 1



def game_over(win ):
    if win:
        print (f"yay you got it, you guessed  {number} correctly!")
    else:
        print(f"you lost. the number was {number} , try again later ")

if __name__ =='__main__':
    game_start()
    game_play()
    game_over(win )
