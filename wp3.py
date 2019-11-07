# Version 3 of Wordpuzzle, Version 3 displays a randomly chosen word to the user that is missing all letters. The user is then prompted to guess each of the missing letters and is shown the word with blanks in place of letters, blanks are then replaced where appropriate by the letter he guessed if his guess was correct, he is given 4 guesses and he is then shown the correct answer and given feedback as to whether he was correct. The game ends if the user guesses all letters or runs out of guesses.

import random
# function that readds instructions from provided file and prints them to screen
def display_instructions(instruction_file):
        file_contents=instruction_file.read()
        instruction_file=instruction_file.close()
        print(file_contents)

# collects guess from user, displays the number of guesses remaining and returns guess
def get_guess(num_guesses):
        print('The number of guesses remaining is ' + str(num_guesses)+ '.') 
        guess = input("Guess a letter ")
        return guess

# updates puzzle where appropriate using the user's guess
def update_puzzle_string(guess,answer,puzzle):
        for i,x in enumerate(answer):
                if x is guess:
                        puzzle[i]=guess
        return True
                        
        
                

# puzzle_string is printed and shown to the user
def display_puzzle_string(puzzle):
        print('The current state of the puzzle is '+str(puzzle))

# checks if all letters that were added to the puzzle are equal to the answer, returns True if that condition is met
def is_word_found(puzzle):
        underscore_check='_'
        if '_' not in str(puzzle):
                return True
                

# calls the functions get_guess, update_puzzle_string, display_puzzle_string, and is_word_found. It evaluates these while tracking the number of guesses. The function then returns the value of True for is_win if the game was won.
def play_game(answer,puzzle):
        num_guesses=4
        is_win=False
        while num_guesses>0:
                guess=get_guess(num_guesses)
                update_puzzle = update_puzzle_string(guess,answer,puzzle)

                display_puzzle_string(puzzle)
                is_word_fd=is_word_found(puzzle)
                if guess not in answer:
                        num_guesses-=1                

                if is_word_fd==True:
                        return True
                
        else:
                print('You lose the correct word was ' + answer)
                input('')
# evaluates the return of the play_game function and provides the user with congratulations and prints the answer to the console                
def display_results(is_win, answer):
        
        
        while is_win ==True:
                print('You win the correct answer is ' + answer)
                input('')
                
# main function of game contains information not needed explicitly in each function and calls the functions responsible for the game
def main():
        
        instruction_file=open('instructions.txt', 'r')

        list_of_words = ['apple', 'banana', 'watermelon', 'kiwi', 'pineapple', 'mango']
        answer=random.choice(list_of_words)
        puzzle=['_'] * len(answer)
        
        display_instructions(instruction_file)
        print('The puzzle so far is ' + str(puzzle))
        is_win=play_game(answer,puzzle)
        
        
        is_word_found(puzzle)
        
        display_results(is_win,answer)

main()