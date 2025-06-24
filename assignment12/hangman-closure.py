def make_hangman(secret_word):
    guesses = [] 

    def hangman_closure(letter):
        guesses.append(letter)

        display_word = ''.join([letter if letter in guesses else '_' for letter in secret_word])
        print(display_word)

        all_guessed = all(letter in guesses for letter in secret_word)
        return all_guessed
    return hangman_closure

secret = input("Enter the secret word: ").lower() 
hangman = make_hangman(secret) 

while True:
    guess = input("Guess a letter: ").lower() 
    if hangman(guess):
        print("You guessed the word!")
        break