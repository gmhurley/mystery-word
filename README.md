# mystery-word
Mystery word game vs the computer

The computer selects a word at random from the list of words in the file /usr/share/dict/words.

The game must be interactive:

Chose level of difficulty at the beginning of the program. Easy mode only has words of 4-6 characters; normal mode only has words of 6-8 characters; hard mode only has words of 8+ characters.

At the start of the game, you'll be told how many letters the computer's word contains.

You'll be asked to supply one guess (i.e. letter) per round. This letter can be upper or lower case and it should not matter. If enter more than one letter, you'll be notified the input is invalid and can try again.

Computer will let you know if your guess appears in the computer's word.

Diusplays the partially guessed word, as well as letters that have not been guessed. For example, if the word is BOMBARD and the letters guessed are a, b, and d, the screen should display:

B _ _ B A _ D

You're allowed 8 guesses. You'll be reminded how many guesses you have left after each round.

You lose a guess only when you guess incorrectly. If you guess a letter that is in the computer's word, you do not lose a guess.

If you guess the same letter twice, a guess is not taken away. Instead, a message letting you know you've already guessed that letter and you'll be asked to try again.

The game ends when you construct the full word or run out of guesses. If you runs out of guesses, the word is revealed.

When a game ends, you'll be asked if you want to play again.