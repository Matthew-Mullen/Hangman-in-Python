#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Wordpuzzle_v2 starts with no letters guessed in the puzzle. The player will only be given one guess. The number of guesses remaining is not displayed when the user is prompted for a guess. After the user's guess, the updated puzzle should be displayed with letter(s) filled in if the player guessed a letter which appears in the word. If the player correctly guesses any letter in the word, the program displays a congratulatory message with the correct word. Otherwise, the program displays a failure message with the same correct word. 

import random
def main():
    # read and display instructions
    #file=open('instructions.txt','r')
    #instructions=file.read()
    #print(instructions)
    
    # randomize a word out of a given list of words
    list_of_words = ['apple', 'banana', 'watermelon', 'kiwi', 'pineapple', 'mango']
    word=random.choice(list_of_words)
    
    # turn the randomized word into a puzzle
    new_word=[]
    str_to_append='_'*len(word)
    for i in str_to_append:
        new_word.append(i)
    #new_word=' _ '*len(word)  
    print(' '.join(new_word))
    # win condition set to false
    
    # prompt user for one guess. loop will end no matter if the guess is right or wrong because user only has one guess
    num_guesses=3
    guess_list=[]
    win=False
    while num_guesses!=0 and win==False:
        print('You have this many guesses remaining %d' % num_guesses)
        decrement_guess=False
        guess=input('Guess a letter: ')
        guess_list.append(guess)
        #print('You have this many guesses remaining %d' % num_guesses)
        for i in range(len(word)):
            if guess == word[i]:
                new_word[i]=word[i]
        if guess not in word:
            print('word')
            num_guesses-=1
        print(' '.join(new_word))
        if ''.join(new_word)==word:
            win=True
    
        
    #print(' '.join(new_word))
            
    if win==True:
        print('Good job! You found the word ' + word + '!')
        input('Press enter to end the game.')
    if win==False:
        print('Not quite. The correct word was ' + word +'. Better luck next time.')
        input('Press enter to end the game.')
main()

