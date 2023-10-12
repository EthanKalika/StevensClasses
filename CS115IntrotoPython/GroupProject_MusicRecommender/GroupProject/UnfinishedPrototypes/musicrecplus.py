# Music recommender system group project
# Group members: Ethan Kalika, Jack Piccirillo, and Michelle Wang
# Pledge: "I pledge my honor that I have abided by the Stevens Honor System." # Put quotes around the pledge

# TO DO:
# If file has stuff in it, make all artists in standard format

filename = "musicrecplus.txt"
Dictionary = {}

#Helper functions

def write_file(string, filename):
    """
    Input: A string and a filename
    Action: Writes the string as a new line in a new file called filename
    """
    myfile = open(filename, "w")
    myfile.write(string)
    myfile.close()
    
def append_file(string, filename):
    """
    Input: A string and a filename
    Action: Apends the string as a new line in the old file if it exists
    """
    myfile = open(filename, "a")
    myfile.write(string)
    myfile.close()

def read_preferences(filename):
    """
    Input: A filename
    Output: A dictionary with the contents of filename loaded into it ina given format
    """
    memo = {}
    with open(filename, "r") as f:
        for line in f:
            [username, singers] = line.strip().split(":")
            singersList = singers.split(",")
            memo[username] = singersList
    return memo

def standard_sort_list(L):
    """ Sort an input list of artists in alphabetical order with the first letter capitalized."""
    """
    Input: A list
    Output: A new list which is sorted
    Notes: The sorting command can be moved outside of the loop
           Is it part of the task description to create a new list
    """
    sortedL=[]
    for item in L:
        sortedL.append(item.strip().title())
        sortedL.sort()
    return sortedL

def user_input_sort_and_add_to_file(user_artist_pref):
    """ Follows input("Enter an artist that you like ( Enter to finish ): ").
        Will keep taking inputs until the user returns Enter.
        Save the user inputs into our text file named filename.
    """
    """
    Input: An artists name
    Action: Append a new line to filename with all the users preferences in alphabetical order
    Notes: Remove the spaces in the string after "input("
           I think this function can be made a lot more elegant if we remove the parameter and put a copy of the "input()" line before the while loop
    """
    prefs = []
    while user_artist_pref != "":
        prefs.append(user_artist_pref) # prefs is a list of artists the user has entered
        user_artist_pref = input("Enter an artist that you like ( Enter to finish ): ") # Get rid of spaces
    sortedPrefs = standard_sort_list(prefs)
    append_file(",".join(sortedPrefs), filename)

def create_total_artists_list(publicDictionary):
    """
    Input: A dictionary
    Output: A sorted list of all the artists in the dictionary without any repeats
    Notes: I think we should remove the enter after the for loop, this makes code style more consistent
    """
    publicDictionary_keys = list(publicDictionary.keys())
    total_artists_list = []
    for key in publicDictionary_keys:
        values = publicDictionary[key]
        for val in values:
            if val not in total_artists_list:
                total_artists_list += [val]

    total_artists_list = standard_sort_list(total_artists_list)
    return total_artists_list

def create_counter_list(publicDictionary):
    """ Make a list of the number of times users selected each artist in standard order."""
    """
    Input: A dictionary
    Output: A list of counts of the number of times that each artist appeared in teh dictionary
    Notes: How will these numbers be tied back to their artists? Or do they not have to be?
           If they have to be related back to the artists, then the list of artists must be soirted in some way
    """
    counter_list = []
    total_artists_list = create_total_artists_list(publicDictionary)
    publicDictionary_keys = list(publicDictionary.keys())
    for artist in total_artists_list:
        count = 0
        for key in publicDictionary_keys:
            artist_list = publicDictionary[key]
            if artist in artist_list:
                count += 1
        counter_list += [count]
    return counter_list
    
######################################################################################################################

# Is this a part of the program that runs indepenently of any particular user, kind of like a setup for everything else
    
UserName = input("Enter your name (put a $ symbol after your name if you wish your preferences to remain private): \n")

import os.path
file_exists = os.path.exists(filename)

import os

if file_exists == False:
    while UserName == "":   # Are there any other possible invalid names?
        UserName = input("Enter your name (put a $ symbol after your name if you wish your preferences to remain private): \n")
    append_file(UserName + ':', filename)
    user_artist_pref = input("Enter an artist that you like ( Enter to finish ): \n")   # The spaces in the parenthesis should be removed
    user_input_sort_and_add_to_file(user_artist_pref)
    Dictionary = read_preferences(filename)
        # This next line can be removed and put at the bottom of the entire if else statement
    user_letter = input("Enter a letter to choose an option : \ne - Enter preferences \nr - Get recommendations \np - Show most popular artists \nh - How popular is the most popular \nm - Which user has the most likes \nq - Save and quit\n")
    while user_letter == '':    # Should't this say while user_letter is not equal to any of the desired letters
        print("Enter a letter to choose an option : \ne - Enter preferences \nr - Get recommendations \np - Show most popular artists \nh - How popular is the most popular \nm - Which user has the most likes \nq - Save and quit\n")
        user_letter = input()
    # To make code more consistent I think there should not be an enter here
else:
    Dictionary = read_preferences(filename)
    Existing_users = list(Dictionary.keys())
    if UserName in Existing_users:
            # This next line can be removed and put at the bottom of the entire if else statement
        user_letter = input("Enter a letter to choose an option : \ne - Enter preferences \nr - Get recommendations \np - Show most popular artists \nh - How popular is the most popular \nm - Which user has the most likes \nq - Save and quit\n")
        while user_letter == '':    # Should't this say while user_letter is not equal to any of the desired letters
            print("Enter a letter to choose an option : \ne - Enter preferences \nr - Get recommendations \np - Show most popular artists \nh - How popular is the most popular \nm - Which user has the most likes \nq - Save and quit\n")
            user_letter = input()
    elif os.stat(filename).st_size == 0: # If file exists but is empty
        append_file(UserName + ':', filename)
        user_artist_pref = input("Enter an artist that you like ( Enter to finish ): ") # Get rid of spaces?
        user_input_sort_and_add_to_file(user_artist_pref)
        Dictionary = read_preferences(filename)
            # This next line can be removed and put at the bottom of the entire if else statement
        user_letter = input("Enter a letter to choose an option : \ne - Enter preferences \nr - Get recommendations \np - Show most popular artists \nh - How popular is the most popular \nm - Which user has the most likes \nq - Save and quit\n")
        while user_letter == '':    # Should't this say while user_letter is not equal to any of the desired letters
            print("Enter a letter to choose an option : \ne - Enter preferences \nr - Get recommendations \np - Show most popular artists \nh - How popular is the most popular \nm - Which user has the most likes \nq - Save and quit\n")
            user_letter = input()
    else: # If file exists and is not empty
        append_file('\n' + UserName + ':', filename)
        user_artist_pref = input("Enter an artist that you like ( Enter to finish ): ") # Get rid of spaces?
        user_input_sort_and_add_to_file(user_artist_pref)
        Dictionary = read_preferences(filename)
            # This next line can be removed and put at the bottom of the entire if else statement
        user_letter = input("Enter a letter to choose an option : \ne - Enter preferences \nr - Get recommendations \np - Show most popular artists \nh - How popular is the most popular \nm - Which user has the most likes \nq - Save and quit\n")
        while user_letter == '':    # Should't this say while user_letter is not equal to any of the desired letters
            user_letter = input("Enter a letter to choose an option : \ne - Enter preferences \nr - Get recommendations \np - Show most popular artists \nh - How popular is the most popular \nm - Which user has the most likes \nq - Save and quit\n")

publicDictionary = {} # Dictionary with user inputs that do not end with $
Dictionary_keys = list(Dictionary.keys())
for key in Dictionary_keys:
     if key[len(key)-1] != "$":
        publicDictionary[key] = Dictionary[key]
        
####################################################################################################################
def menu(user_letter):  # This function should include a while loop that only runs while the user_letter is not q   # This can be considered a helper function and moved higher in the code
    if user_letter == "e": # Enter preferences
        new_preferences = input("Enter an artist that you like ( Enter to finish ): \n")    # Get rid of spaces? and new line
        new_prefs=[]    # Here we must put in the users current preferences
        while new_preferences != "":
            new_prefs.append(new_preferences) # prefs is a list of artists the user has entered
            new_preferences = input("Enter an artist that you like ( Enter to finish ): \n")    # Get rid of spaces? and new line
        sorted_new_prefs = standard_sort_list(new_prefs)
        Dictionary[UserName] = sorted_new_prefs
        if UserName[len(UserName)-1] != "$":
            publicDictionary[UserName] = sorted_new_prefs
        # I think that this next part can be turned into a function of its own
        user_letter = input("Enter a letter to choose an option : \ne - Enter preferences \nr - Get recommendations \np - Show most popular artists \nh - How popular is the most popular \nm - Which user has the most likes \nq - Save and quit\n")
        while user_letter == '':
            user_letter = input("Enter a letter to choose an option : \ne - Enter preferences \nr - Get recommendations \np - Show most popular artists \nh - How popular is the most popular \nm - Which user has the most likes \nq - Save and quit\n")
        menu(user_letter)   # We don't need thus here


    if user_letter == "r": # Get recommendations    # This can become and elif
        user_letter = input("Enter a letter to choose an option : \ne - Enter preferences \nr - Get recommendations \np - Show most popular artists \nh - How popular is the most popular \nm - Which user has the most likes \nq - Save and quit\n")
        menu(user_letter)   # We don't need thus here
        pass

    if user_letter == "p": # Show most popular artist   # This can become and elif

        total_artists_list = create_total_artists_list(publicDictionary)
        counter_list = create_counter_list(publicDictionary)

        if len(total_artists_list) <= 3:
            for artist in total_artists_list:
                print(artist)
        elif total_artists_list == ['']:
            print("Sorry, no artists found")
        else:
            first_index = counter_list.index(max(counter_list))
            counter_list[first_index] = 0
        
            second_index = counter_list.index(max(counter_list))
            counter_list[second_index] = 0
        
            third_index = counter_list.index(max(counter_list))
            counter_list[third_index] = 0

            print(total_artists_list[first_index])
            print(total_artists_list[second_index]) 
            print(total_artists_list[third_index])

        user_letter = input("Enter a letter to choose an option : \ne - Enter preferences \nr - Get recommendations \np - Show most popular artists \nh - How popular is the most popular \nm - Which user has the most likes \nq - Save and quit\n")
        menu(user_letter)   # We don't need thus here

    if user_letter == "h": # How popular is the most popular    # This can become and elif
        """ Print the number of likes the most popular artist received."""
        total_artists_list = create_total_artists_list(publicDictionary)
        counter_list = counter_list = create_counter_list(publicDictionary)
        if total_artists_list == ['']:
            print("Sorry, no artists found.")
        else:
            print(max(counter_list))    
        user_letter = input("Enter a letter to choose an option : \ne - Enter preferences \nr - Get recommendations \np - Show most popular artists \nh - How popular is the most popular \nm - Which user has the most likes \nq - Save and quit\n")
        menu(user_letter)   # We don't need thus here 

    if user_letter == "m": # Which user has the most likes  # This can become and elif
        """ Print the full name(s) of the user(s) who like(s) the most artists."""
        publicDictionary_keys = list(publicDictionary.keys())
        if len(publicDictionary_keys)==1 and publicDictionary[publicDictionary_keys[0]]==['']: 
            print("Sorry, no user found.")
        else:
            number_user_inputs = []
            for key in publicDictionary_keys:
                number_user_inputs += [len(publicDictionary[key])]
            max_number_user_inputs = max(number_user_inputs)
            n=-1
            max_number_indices = []
            for number in number_user_inputs:
                n += 1
                if number == max_number_user_inputs:
                    max_number_indices += [n]
            for index in max_number_indices:
                print(publicDictionary_keys[index])
        user_letter = input("Enter a letter to choose an option : \ne - Enter preferences \nr - Get recommendations \np - Show most popular artists \nh - How popular is the most popular \nm - Which user has the most likes \nq - Save and quit\n")
        menu(user_letter)   # We don't need thus here

    if user_letter == "q": # Save and quit, clear text file and resave the contents of Dictionary   # This should not be in the loop, it should be its own function
        with open(filename, 'w') as f:
            for key, value in Dictionary.items():
                f.write('%s:%s\n' % (key, ",".join(value)))
    
    if user_letter == "" or user_letter != "e" or user_letter != "r" or user_letter != "p" or user_letter != "h" or user_letter != "m" or user_letter != "q":
        user_letter = input("Enter a letter to choose an option : \ne - Enter preferences \nr - Get recommendations \np - Show most popular artists \nh - How popular is the most popular \nm - Which user has the most likes \nq - Save and quit\n")
        menu(user_letter)   # With the getNextUserLetter function there is no point in this code    # We don't need this here
    
menu(user_letter)   # This should be moved up to the setup portion of the code
