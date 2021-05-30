# greeting Murtaza
for a in range (1, 4):
    print ("Czesc Murtaza, for the", a, "time!")

print("---------------------")      # a nice separator

# -------------------------------------------------------

# finding the largest number
list_of_numbers = [1, 2, 6, 20, 70]     # i've changed the name of the variable to be more adequate

print (max(list_of_numbers))        # max is a FUNCTION u have to use on your list
                                    # should work now

# -------------------------------------------------------
  
# greeting a user - Murtaza's feature
def greet_user (first_name, last_name):
    print (f'HI {first_name}, {last_name}!')
    print ('welcome abroad')

print ('start')                                   
greet_user ('mary', 'martha')
print ('finish')

# -------------------------------------------------------

# sorting some list - Bartosz's feature:
# I'm gonna get some random list and then sort it and print it out sorted! :)
from random import randint as random_integer    # we're going to import a function from module random
                                                # that generates random integers, it's called randint()
                                                # but we're gonna rename is as random_integer()

random_list = []    # empty list
    
for index in range(0, 20):  # for loop that's gonna execute 20 times

    random_list.append(random_integer(1, 10))   # u use random_integer saying the range
                                                # from which the random numbers are supposed to come

print(random_list)                  # testing the randomness ;)

sorted_list = sorted(random_list)   # we use sorted() to get a sorted version of random_list
                                    # then we store it in the sorted_list

print(sorted_list)                  # testint the sortedness :D
