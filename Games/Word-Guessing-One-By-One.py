#Game #3

print("Word ia a land animal") #მნიშვნელობა სიტყვის
def guess_the_word():
    word = "Giraffe" #sityva
    guessed_letters = set()

    print("guess the number") #ჩვენი დავალება რა უნდა გავაკეთოთ

    while True:
        guess = input('guess the letter').lower() 

        if len(guess) != 1 or not guess.isalpha(): #ასო-ასო ჩავსვათ ასოები
            print("invalid input. try again")
            continue

        guessed_letters.add(guess)

        display = ' '. join([letter if letter in guessed_letters else '_' for letter in word]) 
        print(display)

        if '_' not in display:
            print("congrats! you guessed the word correctly") #შენ გამოიცანი
            break
if __name__ == "__main__":
    guess_the_word()


