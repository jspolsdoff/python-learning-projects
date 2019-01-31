# when running script rememeber to type 'python3' before filename
# import library
import json
from difflib import get_close_matches

# load json data as python dictionary
data = json.load(open('dictionary.json'))

# function in order to get definition
def retrieve_definition(word):
    # make all words lowercase to match JSON format
    word = word.lower()
    
    # check if the word is in the dictionary
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        action = input('Did you mean %s instead? [y or n]' % get_close_matches(word, data.keys())[0])
        action = action.lower()
        if (action == 'y'):
            return data[get_close_matches(word, data.keys())[0]]
        elif (action == 'n'):
            return ("The word doesn't exist")
        else:
            return("Sorry. We don't understand your entry")
    
# get user input
word_user = input('Enter a word: ')

# get definition 
output = retrieve_definition(word_user)

# conditional to handle more than one definition
if type(output) == list:
    for item in output:
        print('-', item)
else:
    print('-', output)