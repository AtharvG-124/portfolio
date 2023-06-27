import random
# ---------------------Variables-----------------------
word_bank = ["consider"]#, "minute", "accord", "evident", "practice", "intend", "concern", "commit", "issue", "approach", "establish", "utter", "conduct", "obtain", "scarce", "policy", "straight", "stock", "furnish"]
attempts = 15
word = random.choice(word_bank)
length_of_word = len(word)
ans = []
secret_word = []
guessed_letters = []

# ---------------------Functions------------------------
def split(s):
    return [char for char in s]


def list_to_string(s):
    str1 = " "
    return str1.join(s)

# ---------------------Main Program---------------------------------
ans = split(word)

for j in range(length_of_word):
    ans[j] = '*'
print(list_to_string(ans))
secret_word = split(word)
answer = list_to_string(secret_word)

print('attempts: ', attempts)

while answer != word:
    guess = input("Guess a letter in the word: ")

    if guess in guessed_letters:
        print("The letter '", guess, "' has already been guessed. Try again.")

    guessed_letters.append(guess)

    if guess in secret_word:
        for i in range(length_of_word):
            if secret_word[i] == guess:
                ans.pop(i)
                ans.insert(i, guess)
    else:
        print("The letter '", guess, "' is not in the word. Try again.")
        print('attempts: ', attempts - 1)
        attempts = attempts - 1

    answer = ''.join(ans)
    print(list_to_string(ans))
    if attempts == 0:
        print("Sorry, you failed. Better luck next time!")
        print("the answer was: ", answer)
        break
else:
    print("Congratulations, you have finished!!!")

# ----------------------------------comments-------------------------------------
# secret word
    #print secret word without the letters. Ex: word = hello. Display: *****
# number of attempts
    # Subtracting number of attempts if letter is guessed wrong
    # if (input) not in secret word
# reveal letter if guessed