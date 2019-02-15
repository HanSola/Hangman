import getpass
import os
import re
#n = 6 #number of guesses
regex = r'([A-Za-z])'

def ascii_art(num):
    if num == 6:
        print(' \  O  / ')
        print('  \ | /  ')
        print('    |    ')
        print('   /\    ')
        print('  /  \   ')
    if num == 5:
        print(' \  O  / ')
        print('  \ | /  ')
        print('    |    ')
        print('   /     ')
        print('  /      ')
    if num == 4:
        print(' \  O  / ')
        print('  \ | /  ')
        print('    |    ')
        print('         ')
        print('         ')
    if num == 3:
        print(' \  O    ')
        print('  \ |    ')
        print('    |    ')
        print('         ')
        print('         ')  
    if num == 2:
        print('    O    ')
        print('    |    ')
        print('    |    ')
        print('         ')
        print('         ')   
    if num == 1:
        print('    O    ')
        print('         ')
        print('         ')
        print('         ')
        print('         ') 
    if num == 1:
        print('         ')
        print('         ')
        print('         ')
        print('         ')
        print('         ')    
          
def display_code(encode_in,letter_list, rem):
    string_out = encode_in.replace(" ", "    ")
    string_out = string_out.replace("_", " _ ")
    print('    ')
    print('    ')
    print('    ')
    print('Phrase:    '+string_out)
    print('Letter Box: '+ letter_list)
    if n>0:
        print('{} out of {} incorrect guesses remaining'.format(rem,n))
        if n==6:
            ascii_art(n-rem)
    print('    ')
    print('    ')
    return
def player2_start():
    guess = input('Player 2 input:').lower()
    if len(guess) > 1:
        print('Enter only 1 character at a time')
        return('0')
    else:
        reg_check = re.compile(regex)
        if not reg_check.search(guess):
            print('Enter a valid character')
            return('0')
        else:
            if letters.find(guess) > -1 or encoded.find(guess) > -1:
                print('This character already been guessed')
                return('0')
            else:
                return(guess.lower())

print('Welcome to Hang-man')
print('Player 1 will enter a word/phrase and Player 2 will attempt to guess the string 1 character at a time')
#print('Player 2 will only have {} guesses to figure out the word or phrase'.format(n))
print('Input how many guesses Player will 2 have? A normal game is 6. To play with unlimited guesses, enter 0.')
raw_in = input( 'Number of turns:')

try:
    n = int(raw_in) 
except:
    print("This is not a number. The game will continue with 6 guesses")
    n = 6
 
#print('Player 1, press <Enter> to begin')
print('Player 1:Enter your word or phrase below.') 
#print('It cannot be more than {} characters long'.format(g))
print('Special characters and whitespace will be shown. Only A-z characters will need to be found ')
print('Note that the letters will not appear as you type. Press <Enter> to continue')
raw_data = getpass.getpass('Pass-phrase:')
alt_data = raw_data.lower()
encoded = re.sub(regex,"_",alt_data)
letters = ""
c = 0
r=1
if n>0:
    r = n - c
game_over = False
while not game_over:
    
    display_code(encoded,letters,r)
    check = player2_start() 
    if check is not '0':
        if check not in raw_data.lower():    
            c = c+1
            letters = letters + "    " + check
        else:
            while alt_data.find(check) > -1: #warning, could be result in infinite loop
                ind = alt_data.find(check)
                alt_data = alt_data[:ind]+'_'+alt_data[ind+1:]
                encoded = encoded[:ind]+check+encoded[ind+1:]
            
    r = n - c #remaining = number - count
    if encoded == raw_data.lower():
        game_over = True
        msg = "Congratulations Player 2"
        if n==6:
            ascii_art(c)
    if r < 1 and n > 0:
        game_over = True
        msg = "You lose!"
        if n==6:
            ascii_art(c)
#game over 
print(msg)
print('Answer: '+ raw_data)
print('Game Over')
os.system('pause')
