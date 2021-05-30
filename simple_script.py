# greeting Murtaza
for a in range (1, 2):
    print ("Czesc Murtaza, for the", a, "time!")

print("---------------------")      # a nice separator

# finding the largest number
list_of_numbers = [1, 2, 6, 20, 70]     # i've changed the name of the variable to be more adequate

print (max(list_of_numbers))        # max is a FUNCTION u have to use on your list
                                    # should work now
# greeting a user
def greet_user (first_name, last_name):
    print (f'HI {first_name}, {last_name}!')
    print ('welcome abroad')

print ('start')                                   
greet_user ('mary', 'martha')
print ('finish')