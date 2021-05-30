# **Exercise (optional)**: Write a function that takes a string as argument, 
# and creates a new string that is a copy of the argument, except that every 
# non-letter is replaced by a space (e.g., "`ph@t l00t`" is changed to "`ph t l  t`"). 
# To write such a function, you will start with an empty string, and traverse the 
# characters of the argument one by one. When you encounter a character that is 
# acceptable, you add it to the new string. When it is not acceptable, you add a space 
# to the new string. Note that you can check whether a character is acceptable by simple 
# comparisons, e.g., any lower case letter can be found using the test `if ch >= 'a' and ch <= 'z':`. 

# String cleaning function
def clean_string(string):
    
clean_string("Aph@t 100t")





























# **Exercise 6.3:** In the text below, count how often the word "wood" occurs 
# (using program code, of course). Capitals and lower case letters may both be 
# used, and you have to consider that the word "wood" should be a separate word, 
# and not part of another word. Hint: If you did the exercises from this chapter, 
# you already developed a function that "cleans" a text. Combining that function 
# with the `split()` function more or less solves the problem for you.

text = """How much wood would a woodchuck chuck
If a woodchuck could chuck wood?
He would chuck, he would, as much as he could,
And chuck as much as a woodchuck would
If a Mr. Smith could chuck wood\n\r\t."""

































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