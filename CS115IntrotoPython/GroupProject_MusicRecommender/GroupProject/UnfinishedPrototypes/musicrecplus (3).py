# Music recommender system group project
# Group members: Ethan Kalika, Jack Piccirillo, and Michelle Wang
# Pledge: I pledge my honor that I have abided by the Stevens Honor System. # Put quotes around the pledge

# TO DO:
# If file has stuff in it, make all artists in standard format

filename = "musicrecplus_ex2_a.txt" # Fix the file name
Dictionary = {}

#Helper functions

def write_file(string, filename):
    myfile = open(filename, "w")
    myfile.write(string)
    myfile.close()
    
def append_file(string, filename):
    myfile = open(filename, "a")
    myfile.write(string)
    myfile.close()

def read_preferences(filename):
    memo = {}
    with open(filename, "r") as f:
        for line in f:
            [username, singers] = line.strip().split(":")
            singersList = singers.split(",")
            memo[username] = singersList
    return memo

def standard_sort_list(L):
    """ Sort an input list of artists in alphabetical order with the first letter capitalized."""
    sortedL=[]
    for item in L:
        sortedL.append(item.strip().title())
        sortedL.sort()
    return sortedL

def user_input_sort_and_add_to_file(user_artist_pref):
    """ Follows input("Enter an artist that you like ( Enter to finish ): \n").
        Will keep taking inputs until the user returns Enter.
        Save the user inputs into our text file named filename.
    """
    prefs = []
    while user_artist_pref != "":
        prefs.append(user_artist_pref) # prefs is a list of artists the user has entered
        user_artist_pref = input("Enter an artist that you like ( Enter to finish ): \n")   # Remove spaces directly in teh parenthesis
    sortedPrefs = standard_sort_list(prefs)
    append_file(",".join(sortedPrefs), filename)

def create_total_artists_list(publicDictionary):
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
    Input: Two sorted lists with no repeated elements
    Output: The number of common elements between the lists
    """
    count = 0
    element2Index = 0
    for element1 in lst1:
        if element1 in lst2:
            count += 1
    return count
    
######################################################################################################################
    
UserName = input("Enter your name (put a $ symbol after your name if you wish your preferences to remain private): \n")

import os.path
file_exists = os.path.exists(filename)

import os
import sys

if file_exists == False:
    while UserName == "":
        UserName = input("Enter your name (put a $ symbol after your name if you wish your preferences to remain private): \n")
    append_file(UserName + ':', filename)
    user_artist_pref = input("Enter an artist that you like ( Enter to finish ): \n")   # Remove spaces directly in teh parenthesis
    user_input_sort_and_add_to_file(user_artist_pref)
    Dictionary = read_preferences(filename)
    user_letter = input("Enter a letter to choose an option : \ne - Enter preferences \nr - Get recommendations \np - Show most popular artists \nh - How popular is the most popular \nm - Which user has the most likes \nq - Save and quit\n")
    while user_letter == '':
        print("Enter a letter to choose an option : \ne - Enter preferences \nr - Get recommendations \np - Show most popular artists \nh - How popular is the most popular \nm - Which user has the most likes \nq - Save and quit\n")
        user_letter = input()
    
else:
    Dictionary = read_preferences(filename)
    Existing_users = list(Dictionary.keys())
    if UserName in Existing_users:
        user_letter = input("Enter a letter to choose an option : \ne - Enter preferences \nr - Get recommendations \np - Show most popular artists \nh - How popular is the most popular \nm - Which user has the most likes \nq - Save and quit\n")
        while user_letter == '':
            user_letter = input("Enter a letter to choose an option : \ne - Enter preferences \nr - Get recommendations \np - Show most popular artists \nh - How popular is the most popular \nm - Which user has the most likes \nq - Save and quit\n")
    elif os.stat(filename).st_size == 0: # If file exists but is empty
        append_file(UserName + ':', filename)
        user_artist_pref = input("Enter an artist that you like ( Enter to finish ): ") # Remove spaces directly in teh parenthesis # Why is there no new line here
        user_input_sort_and_add_to_file(user_artist_pref)
        Dictionary = read_preferences(filename)
        user_letter = input("Enter a letter to choose an option : \ne - Enter preferences \nr - Get recommendations \np - Show most popular artists \nh - How popular is the most popular \nm - Which user has the most likes \nq - Save and quit\n")
        while user_letter == '':
            user_letter = input("Enter a letter to choose an option : \ne - Enter preferences \nr - Get recommendations \np - Show most popular artists \nh - How popular is the most popular \nm - Which user has the most likes \nq - Save and quit\n")
    else: # If file exists and is not empty
        append_file('\n' + UserName + ':', filename)
        user_artist_pref = input("Enter an artist that you like ( Enter to finish ): \n")   # Remove spaces directly in teh parenthesis
        user_input_sort_and_add_to_file(user_artist_pref)
        Dictionary = read_preferences(filename)
        user_letter = input("Enter a letter to choose an option : \ne - Enter preferences \nr - Get recommendations \np - Show most popular artists \nh - How popular is the most popular \nm - Which user has the most likes \nq - Save and quit\n")
        while user_letter == '':
            user_letter = input("Enter a letter to choose an option : \ne - Enter preferences \nr - Get recommendations \np - Show most popular artists \nh - How popular is the most popular \nm - Which user has the most likes \nq - Save and quit\n")

publicDictionary = {} # Dictionary with user inputs that do not end with $
Dictionary_keys = list(Dictionary.keys())
for key in Dictionary_keys:
     if key[len(key)-1] != "$":
        publicDictionary[key] = Dictionary[key]
        
####################################################################################################################
def menu(user_letter):
    if user_letter == "e": # Enter preferences
        new_preferences = input("Enter an artist that you like ( Enter to finish ): \n")    # Remove spaces directly in teh parenthesis
        new_prefs=[]
        while new_preferences != "":
            new_prefs.append(new_preferences) # prefs is a list of artists the user has entered
            new_preferences = input("Enter an artist that you like ( Enter to finish ): \n")    # Remove spaces directly in teh parenthesis
        sorted_new_prefs = standard_sort_list(new_prefs)
        Dictionary[UserName] = sorted_new_prefs
        if UserName[len(UserName)-1] != "$":
            publicDictionary[UserName] = sorted_new_prefs
        user_letter = input("Enter a letter to choose an option : \ne - Enter preferences \nr - Get recommendations \np - Show most popular artists \nh - How popular is the most popular \nm - Which user has the most likes \nq - Save and quit\n")
        while user_letter == '':
            user_letter = input("Enter a letter to choose an option : \ne - Enter preferences \nr - Get recommendations \np - Show most popular artists \nh - How popular is the most popular \nm - Which user has the most likes \nq - Save and quit\n")
        menu(user_letter)


    if user_letter == "r": # Get recommendations
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
                for artist in L:
                    if artist not in user_artist_list:
                        print(artist)  
                
        user_letter = input("Enter a letter to choose an option : \ne - Enter preferences \nr - Get recommendations \np - Show most popular artists \nh - How popular is the most popular \nm - Which user has the most likes \nq - Save and quit\n")
        menu(user_letter)


    if user_letter == "p": # Show most popular artist

        total_artists_list = create_total_artists_list(publicDictionary)
        counter_list = create_counter_list(publicDictionary)

        if len(total_artists_list) <= 3:
            for artist in total_artists_list:
                print(artist)
        elif total_artists_list == ['']:
            print("Sorry, no artists found")
        else:
            initial_max_count = max(counter_list)
            first_index = counter_list.index(max(counter_list))
            printList = [total_artists_list[first_index]]
            counter_list[first_index] = 0

            m=-1

            for count in counter_list:
                m += 1
                if count == initial_max_count:
                    printList += [total_artists_list[m]]
            for element in printList:
                print(element)
                
                        
        user_letter = input("Enter a letter to choose an option : \ne - Enter preferences \nr - Get recommendations \np - Show most popular artists \nh - How popular is the most popular \nm - Which user has the most likes \nq - Save and quit\n")
        menu(user_letter)



    if user_letter == "h": # How popular is the most popular
        """ Print the number of likes the most popular artist received."""
        total_artists_list = create_total_artists_list(publicDictionary)
        counter_list = counter_list = create_counter_list(publicDictionary)
        if total_artists_list == ['']:
            print("Sorry, no artists found.")
        else:
            print(max(counter_list))    
        user_letter = input("Enter a letter to choose an option : \ne - Enter preferences \nr - Get recommendations \np - Show most popular artists \nh - How popular is the most popular \nm - Which user has the most likes \nq - Save and quit\n")
        menu(user_letter)

    if user_letter == "m": # Which user has the most likes
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
        menu(user_letter)

    if user_letter == "q": # Save and quit, clear text file and resave the contents of Dictionary
        with open("musicrecplus.txt", 'w') as f:
            for key, value in Dictionary.items():
                if key == UserName:
                    f.write('%s:%s' % (key, ",".join(value)))
                else:
                    f.write('%s:%s\n' % (key, ",".join(value)))
        sys.exit()
    
    else:
        user_letter = input("Enter a letter to choose an option : \ne - Enter preferences \nr - Get recommendations \np - Show most popular artists \nh - How popular is the most popular \nm - Which user has the most likes \nq - Save and quit\n")
        menu(user_letter)
    
menu(user_letter)
