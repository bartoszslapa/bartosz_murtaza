# String cleaning function
def clean_string(string):
    new_string = ""
    for character in string:        
        # check if it's alphabetical if so
        # if (character >= 'a' and character <= 'z') or (character >= 'A' and character <= 'Z'):
        if character.lower() >= 'a' and character.lower() <= 'z':
            # add it to the temp_string
            # left_side = right_side
            # assign the value of left side to the right side calculate right side
            new_string = new_string + character
            # shorter version: temp_string += character
        else:
            # else you add a space to your temp_string
            new_string += " "
    return new_string

def wood_counter(text):
    # first we create a counter = 0
    counter = 0

    # we clean the string
    cleaned_string = clean_string(text)

    # split the text and store words in a LIST
    # it's a list of STRINGS !! it's not a string
    text_splitted = cleaned_string.split()

    # check word by word if we see "wood"
    for word in text_splitted:  # here we check every STRING in the list
        if word.lower() == "wood":
            counter += 1

    return counter

text = """How much wood would a woodchuck chuck
If a woodchuck could chuck wood?
He would chuck, he would, as much as he could,
And chuck as much as a woodchuck would
If a Mr. Smith could chuck wood\n\r\t."""

how_much_wood = wood_counter(text)
print(how_much_wood)





































# read whole text
# create a counter
# get rid \n
# get rid of ?. special grammar
# lowercase my sentence
"if a woodchuck could chuck wood"
# split the string by some character
["if", "a", "woodchuck"]
#check if wood is in the list
    # if yes
       # counter = counter +1 <--> counter += 1 
    # else
        #pass
#return