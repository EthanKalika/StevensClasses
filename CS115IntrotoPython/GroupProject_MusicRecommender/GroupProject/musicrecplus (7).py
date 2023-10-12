# Music recommender system group project
# Group members: Ethan Kalika, Jack Piccirillo, and Michelle Wang
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.


filename = "musicrecplus.txt"
Dictionary = {}

#Helper functions

def write_file(string, filename): # From class
    """Write string in document titled filename. If it doesn't exist, create the file."""
    """
    Input: A string and a filename
    Action: Writes the string as a new line in a new file called filename
    From Class
    """
    myfile = open(filename, "w")
    myfile.write(string)
    myfile.close()
    
def append_file(string, filename): # From class
    """Add string to the end of the text for document titled filename."""
    """
    Input: A string and a filename
    Action: Apends the string as a new line in the old file if it exists
    From class
    """
    myfile = open(filename, "a")
    myfile.write(string)
    myfile.close()

def read_preferences(filename): # From class
    """ Create dictionary memo and write each key:value in a new line, values separated by commas."""
    """
    Input: A filename
    Output: A dictionary with the contents of filename loaded into it ina given format
    From class
    """
    memo = {}
    with open(filename, "r") as f:
        for line in f:
            [username, singers] = line.strip().split(":")
            singersList = singers.split(",")
            memo[username] = singersList
    return memo

def standard_sort_list(L): # Ethan Kalika
    """ Sort an input list of artists in alphabetical order with the first letter capitalized."""
    """
    Input: A list
    Output: A new list which is sorted
    Ethan Kalika
    """
    sortedL=[]
    for item in L:
        sortedL.append(item.strip().title())
        sortedL.sort()
    return sortedL

def user_input_sort_and_add_to_file(user_artist_pref): # Michelle Wang
    """ Follows input("Enter an artist that you like (Enter to finish): \n").
        Will keep taking inputs until the user returns Enter.
        Save the user inputs into our text file named filename.
    """
    """
    Input: An artists name
    Action: Append a new line to filename with all the users preferences in alphabetical order
    Michelle Wang
    """
    prefs = []
    while user_artist_pref != "":
        if user_artist_pref in prefs:
            user_artist_pref = input("Enter an artist that you like (Enter to finish): \n")
        else:
            prefs.append(user_artist_pref) # prefs is a list of artists the user has entered
            user_artist_pref = input("Enter an artist that you like (Enter to finish): \n")
    sortedPrefs = standard_sort_list(prefs)
    append_file(",".join(sortedPrefs), filename)

def create_total_artists_list(publicDictionary): # Jack Piccirillo
    """Create a list of all the artists from publicDictionary, no repeats."""
    """
    Input: A dictionary
    Output: A sorted list of all the artists in the dictionary without any repeats
    Jack Piccirillo
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

def create_counter_list(publicDictionary): # Michelle Wang
    """ Make a list of the number of times users selected each artist in standard order."""
    """
    Input: A dictionary
    Output: A list of counts of the number of times that each artist appeared in teh dictionary
    Michelle Wang
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

def getSimilarities(lst1, lst2): # Ethan Kalika
    """
    Input: Two lists lst1 and lst2 with no repeated elements
    Output: The number of common elements between the lists
    Ethan Kalika
    """
    count = 0
    element2Index = 0
    for element1 in lst1:
        if element1 in lst2:
            count += 1
    return count
    
######################################################################################################################
    
UserName = input("Enter your name (put a $ symbol after your name if you wish your preferences to remain private): \n")
UserName = UserName.title()

import os.path
file_exists = os.path.exists(filename)

import os
import sys

if file_exists == False: # If file does not exist -- Michelle Wang
    '''
    If the file does not exist yet then this statement creates it. Then it initializes the user and populates their preferences, creates the dictionary, and displays the menu.
    Michelle Wang
    '''
    while UserName == "":
        UserName = input("Enter your name (put a $ symbol after your name if you wish your preferences to remain private): \n")
    append_file(UserName + ':', filename)
    user_artist_pref = input("Enter an artist that you like (Enter to finish): \n")
    user_input_sort_and_add_to_file(user_artist_pref)
    Dictionary = read_preferences(filename)
    user_letter = input("Enter a letter to choose an option: \ne - Enter preferences \nr - Get recommendations \np - Show most popular artists \nh - How popular is the most popular \nm - Which user has the most likes \ns - Show Preferences \nq - Save and quit\n")
    while user_letter == '':
        print("Enter a letter to choose an option: \ne - Enter preferences \nr - Get recommendations \np - Show most popular artists \nh - How popular is the most popular \nm - Which user has the most likes \nq - Save and quit\n")
        user_letter = input()
    
else: # If file exists -- Michelle Wang
    '''
    If the file does exist then this statement initializes the user and populates their preferences, creates the dictionary, and displays the menu. This statement preforms this task accordingly to
    wether or not the file is empty
    Michelle Wang
    '''
    Dictionary = read_preferences(filename)
    Existing_users = list(Dictionary.keys())
    if UserName in Existing_users:
        user_letter = input("Enter a letter to choose an option: \ne - Enter preferences \nr - Get recommendations \np - Show most popular artists \nh - How popular is the most popular \nm - Which user has the most likes \ns - Show Preferences \nq - Save and quit\n")
        while user_letter == '':
            user_letter = input("Enter a letter to choose an option: \ne - Enter preferences \nr - Get recommendations \np - Show most popular artists \nh - How popular is the most popular \nm - Which user has the most likes \ns - Show Preferences \nq - Save and quit\n")
    elif os.stat(filename).st_size == 0: # If file exists but is empty
        append_file(UserName + ':', filename)
        user_artist_pref = input("Enter an artist that you like (Enter to finish):\n")
        user_input_sort_and_add_to_file(user_artist_pref)
        Dictionary = read_preferences(filename)
        user_letter = input("Enter a letter to choose an option: \ne - Enter preferences \nr - Get recommendations \np - Show most popular artists \nh - How popular is the most popular \nm - Which user has the most likes \ns - Show Preferences \nq - Save and quit\n")
        while user_letter == '':
            user_letter = input("Enter a letter to choose an option: \ne - Enter preferences \nr - Get recommendations \np - Show most popular artists \nh - How popular is the most popular \nm - Which user has the most likes \ns - Show Preferences \nq - Save and quit\n")
    else: # If file exists and is not empty
        append_file('\n' + UserName + ':', filename)
        user_artist_pref = input("Enter an artist that you like (Enter to finish): \n")
        user_input_sort_and_add_to_file(user_artist_pref)
        Dictionary = read_preferences(filename)
        user_letter = input("Enter a letter to choose an option: \ne - Enter preferences \nr - Get recommendations \np - Show most popular artists \nh - How popular is the most popular \nm - Which user has the most likes \ns - Show Preferences \nq - Save and quit\n")
        while user_letter == '':
            user_letter = input("Enter a letter to choose an option: \ne - Enter preferences \nr - Get recommendations \np - Show most popular artists \nh - How popular is the most popular \nm - Which user has the most likes \ns - Show Preferences \nq - Save and quit\n")

publicDictionary = {} # Dictionary with user inputs that do not end with $
'''
Initializes public dictionary
'''
Dictionary_keys = list(Dictionary.keys())
for key in Dictionary_keys:
     if key[len(key)-1] != "$":
        publicDictionary[key] = Dictionary[key]
        
####################################################################################################################
def menu(user_letter, UserName, Dictionary, publicDictionary):
    """ Display menu and asks user for user_letter input.
    Input: One of the letters from menu, UserName, The dictionary of user astist list keys, the public dictionary of user artists list keys
    Action: Cycles through and runs the whole program
    """
    if user_letter == "e": # Enter preferences -- Ethan Kalika
        '''
        Ethan Kalika
        '''
        new_preferences = input("Enter an artist that you like (Enter to finish): \n")
        new_prefs=[]
        while new_preferences != "":
            new_prefs.append(new_preferences) # prefs is a list of artists the user has entered
            new_preferences = input("Enter an artist that you like (Enter to finish): \n")
        sorted_new_prefs = standard_sort_list(new_prefs)
        Dictionary[UserName] = sorted_new_prefs
        if UserName[len(UserName)-1] != "$":
            publicDictionary[UserName] = sorted_new_prefs
        user_letter = input("Enter a letter to choose an option: \ne - Enter preferences \nr - Get recommendations \np - Show most popular artists \nh - How popular is the most popular \nm - Which user has the most likes \ns - Show Preferences \nq - Save and quit\n")
        while user_letter == '':
            user_letter = input("Enter a letter to choose an option: \ne - Enter preferences \nr - Get recommendations \np - Show most popular artists \nh - How popular is the most popular \nm - Which user has the most likes \ns - Show Preferences \nq - Save and quit\n")
        menu(user_letter, UserName, Dictionary, publicDictionary)


    if user_letter == "r": # Get recommendations -- Ethan Kalika
        '''
        Ethan Kalika
        '''
        user_artist_list = Dictionary[UserName]
        all_users = list(publicDictionary.keys())
        other_users = []

        rec_counts = []
        
        for user in all_users:
            if user != UserName:
                other_users += [user]

        for user in other_users:
            rec_counts += [getSimilarities(Dictionary[UserName],publicDictionary[user])]

        if rec_counts == []:
            print("No recommendations available at this time.")
        if rec_counts != []:
            if max(rec_counts) == 0:
                print("No recommendations available at this time.")
            else:
                max_index = rec_counts.index(max(rec_counts))
                L = publicDictionary[other_users[max_index]] # List of artists from user with max overlap
                if L == user_artist_list:
                    rec_counts[max_index] = 0 # Do not include users whose artists are the same
                    max_index = rec_counts.index(max(rec_counts))
                    L = publicDictionary[other_users[max_index]]
                n=0
                for artist in L:
                    if artist not in user_artist_list:
                        n += 1
                if n > 0:
                    for artist in L:
                        if artist not in user_artist_list:
                            print(artist)
                else:
                    print("No recommendations available at this time.")
                
        user_letter = input("Enter a letter to choose an option: \ne - Enter preferences \nr - Get recommendations \np - Show most popular artists \nh - How popular is the most popular \nm - Which user has the most likes \ns - Show Preferences \nq - Save and quit\n")
        menu(user_letter, UserName, Dictionary, publicDictionary)


    if user_letter == "p": # Show most popular artist -- Michelle Wang
        '''
        Michelle Wang
        '''

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
            print(total_artists_list[first_index])
            print(total_artists_list[second_index])
            print(total_artists_list[third_index])
                
                        
        user_letter = input("Enter a letter to choose an option: \ne - Enter preferences \nr - Get recommendations \np - Show most popular artists \nh - How popular is the most popular \nm - Which user has the most likes \ns - Show Preferences \nq - Save and quit\n")
        menu(user_letter, UserName, Dictionary, publicDictionary)



    if user_letter == "h": # How popular is the most popular -- Michelle Wang
        '''
        Michelle Wang
        '''
        """ Print the number of likes the most popular artist received."""
        total_artists_list = create_total_artists_list(publicDictionary)
        counter_list = counter_list = create_counter_list(publicDictionary)
        if total_artists_list == ['']:
            print("Sorry, no artists found.")
        else:
            print(max(counter_list))    
        user_letter = input("Enter a letter to choose an option: \ne - Enter preferences \nr - Get recommendations \np - Show most popular artists \nh - How popular is the most popular \nm - Which user has the most likes \ns - Show Preferences \nq - Save and quit\n")
        menu(user_letter, UserName, Dictionary, publicDictionary)

    if user_letter == "m": # Which user has the most likes -- Jack Piccirillo
        '''
        Jack Piccirillo
        '''
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
        user_letter = input("Enter a letter to choose an option: \ne - Enter preferences \nr - Get recommendations \np - Show most popular artists \nh - How popular is the most popular \nm - Which user has the most likes \ns - Show Preferences \nq - Save and quit\n")
        menu(user_letter, UserName, Dictionary, publicDictionary)



    if user_letter == "s": # Michelle Wang
        '''
        Michelle Wang
        '''
        artistsList = Dictionary[UserName]
        for artist in artistsList:
            print(artist)

    if user_letter == "q": # Save and quit, clear text file and resave the contents of Dictionary -- Jack Piccirillo
        '''
        Jack Piccirillo
        '''
        keysList = list(Dictionary.keys())
        keysList.sort()
        keysList = sorted(keysList, key=lambda v: v.upper())
        values = list(Dictionary.values())
        Dictionary2={}
        for key in keysList:
            Dictionary2[key] = Dictionary[key] # Create new Dictionary2 with sorted keys and get values from Dictionary[keys]
        Dic={}
        Dic = Dictionary2
        L = list(Dic.keys())
        last_key = L[len(L)-1]
        with open("musicrecplus.txt", 'w') as f:
            for key, value in Dic.items():
                    if key != last_key:
                        f.write('%s:%s\n' % (key, ",".join(value)))
                    else:
                        f.write('%s:%s' % (key, ",".join(value)))
        sys.exit()
    
    else: # Michelle Wang
        '''
        Michelle Wang
        '''
        user_letter = input("Enter a letter to choose an option: \ne - Enter preferences \nr - Get recommendations \np - Show most popular artists \nh - How popular is the most popular \nm - Which user has the most likes \ns - Show Preferences \nq - Save and quit\n")
        menu(user_letter, UserName, Dictionary, publicDictionary)
    
menu(user_letter, UserName, Dictionary, publicDictionary)
