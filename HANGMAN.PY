import random

words = ["apple", "banana", "python", "code", "alpha"]
chosen_word = random.choice(words)
guessed_letters = []
attempts = 6

print("🎮 Welcome to Hangman!")

while attempts > 0:
    display_word = ''.join([char if char in guessed_letters else '_' for char in chosen_word])
    print(f"Word: {display_word}")
    
    if display_word == chosen_word:
        print("🎉 Congratulations! You've guessed the word!")
        break

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("⚠️ Already guessed.")
    elif guess in chosen_word:
        print("✅ Correct!")
        guessed_letters.append(guess)
    else:
        print("❌ Incorrect!")
        guessed_letters.append(guess)
        attempts -= 1
        print(f"Attempts left: {attempts}")

if attempts == 0:
    print(f"😢 Game over! The word was: {chosen_word}")
