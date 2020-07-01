import sys

def palindrome():
    word = input("Enter a word or number to check if it is a palindrome: ")
    if word == word[::-1]:
        print("Yes, It is a Palindrome")
    else:
        print("No, it is not a Palindrome")

palindrome()
    
while True:
    def playagain():
        play_again = str.lower(input("If you'd like to play again, please type 'yes':  "))
        if play_again == "yes":
            palindrome()
        elif play_again == "no":
            print("Thanks for playing")
            sys.exit()
        else:
            print("Please answer 'yes' or 'no'")
            playagain()   
              
    playagain()
  
    