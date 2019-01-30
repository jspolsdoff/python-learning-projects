#when running script rememeber to type 'python3' before filename
# import library
import json

# load json data as python dictionary
data = json.load(open("dictionary.json"))

# function in order to get definition
def retrieve_definition(word):
    return data[word]
    
# get user input
word_user = input("Enter a word: ")

# get definition and print the result
print(retrieve_definition(word_user))