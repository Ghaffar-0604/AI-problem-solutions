from hangman_art import stages,logo
from hangman_words import word_list
import random


wordChoosen=random.choice(word_list)
lives=6
print("Guess word is ",wordChoosen)


print(logo)
display=[]

for i in range(len(wordChoosen)):
    display.append("_")

while "_" in display:
    guess=input("Guess a letter: ").lower()
    for i in range(len(wordChoosen)):
        letter=wordChoosen[i]
        if guess==letter:
            display[i]=guess
    if guess not in wordChoosen:
        lives=lives-1
        if lives==0:
            print("Guess word is ",wordChoosen)
            print(stages[lives])
            print("You Have lost!")
            exit(1)
        
    print(f"{' '.join(display)}")
    print(stages[lives])
else:
    print("You Won!")
    print("Guess word is ",wordChoosen)















        
