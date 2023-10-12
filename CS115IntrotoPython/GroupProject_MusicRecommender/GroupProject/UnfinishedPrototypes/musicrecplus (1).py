# Music recommender system group project
# Group members: Ethan Kalika, Jack Piccirillo, and Michelle Wang
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.

# TO DO:
# If file has stuff in it, make all artists in standard format

filename = "musicrecplus.txt"
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

def read_preferences(filename): # Ethan Kalika
    memo = {}
    for element in read_preferences_List(filename):
        [username, singers] = element
        memo[username] = singers
    return memo

def read_preferences_List(filename):
    masterList = []
    with open(filename, "r") as f:
        for line in f:
            [username, singers] = line.strip().split(":")
            singersList = singers.split(",")
            masterList += [[username, singersList]]
        masterList.sort()
    return masterList

def standard_sort_list(L):
    """ Sort an input list of artists in alphabetical order with the first letter capitalized."""
    sortedL=[]
    for item in L:
        sortedL.append(item.strip().title())
        sortedL.sort()
    return sortedL

def user_input_sort_and_add_to_file():  # Ethan Kalika
    """ Follows input("Enter an artist that you like (Enter to finish): \n").
        Will keep taking inputs until the user returns Enter.
        Save the user inputs into our text file named filename.
    """
    prefs = []
    user_artist_pref = input("Enter an artist that you like (Enter to finish): \n")
    while user_artist_pref != "":
        prefs.append(user_artist_pref) # prefs is a list of artists the user has entered
        user_artist_pref = input("Enter an artist that you like (Enter to finish): \n")
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

def getNextUserLetter():    # Ethan Kalika
    """
    Input: None
    Ouptut: The next action letter the user chooses
    """
    user_letter = input("Enter a letter to choose an option : \ne - Enter preferences \nr - Get recommendations \np - Show most popular artists \nh - How popular is the most popular \nm - Which user has the most likes \nq - Save and quit\n")
    while not (user_letter == 'e' or user_letter == 'r' or user_letter == 'p' or user_letter == 'h' or user_letter == 'm' or user_letter == 'q'):    # Should't this say while user_letter is not equal to any of the desired letters
        print("Enter a letter to choose an option : \ne - Enter preferences \nr - Get recommendations \np - Show most popular artists \nh - How popular is the most popular \nm - Which user has the most likes \nq - Save and quit\n")
        user_letter = input()
    return user_letter

def getUserName():  # Ethan Kalika
    UserName = input("Enter your name (put a $ symbol after your name if you wish your preferences to remain private): \n")
    while UserName == "":
        UserName = input("Enter your name (put a $ symbol after your name if you wish your preferences to remain private): \n")
    return UserName

def getSimilarities(lst1, lst2): # Ethan Kalika
    """
    Input: Two sorted lists
    Output: The number of common elements between the lists
    """
    count = 0
    element2Index = 0
    for element1 in lst1:
        if element2Index == len(lst2):
            return count
        elif element1 == lst2[element2Index]:
            count += 1
            element2Index += 1
        else:
            element2Index += 1
    return count

def terminateQ():   # Save and quit, clear text file and resave the contents of Dictionary
    with open("musicrecplus.txt", 'w') as f:
            for key, value in Dictionary.items():
                if key == list(Dictionary.keys())[-1]:
                    f.write('%s:%s' % (key, ",".join(value)))
                else:
                    f.write('%s:%s\n' % (key, ",".join(value)))
    print(Dictionary)
    print(publicDictionary)

def menu(user_letter):
    while user_letter != 'q':
        if user_letter == "e": # Enter preferences
            print("Enter an artist that you like (Enter to finish): \n")
            new_preferences = input('')
            new_prefs = []
            while new_preferences != "":
                new_prefs.append(new_preferences) # prefs is a list of artists the user has entered
                print("Enter an artist that you like (Enter to finish): \n")
                new_preferences = input("")
            sorted_new_prefs = standard_sort_list(new_prefs)
            Dictionary[UserName] = sorted_new_prefs
            if UserName[len(UserName)-1] != "$":
                publicDictionary[UserName] = sorted_new_prefs

        elif user_letter == "r": # Get recommendations    # Ethan Kalika
            compareList = Dictionary[UserName]
            if compareList == [] or list(publicDictionary.keys()) == [UserName]:
                print('No recommendations available at this time.')
            else:
                similarUser = None
                similarities = 0
                for user in publicDictionary:
                    currentSimilarities = getSimilarities(publicDictionary[UserName], publicDictionary[user])
                    if currentSimilarities >= similarities and currentSimilarities != len(publicDictionary[user]):
                        similarities = currentSimilarities
                        similarUser = user
                for artist in publicDictionary[similarUser]:
                    if not(artist in publicDictionary[UserName]):
                        print(artist)

        elif user_letter == "p": # Show most popular artist

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

        elif user_letter == "h": # How popular is the most popular
            """ Print the number of likes the most popular artist received."""
            total_artists_list = create_total_artists_list(publicDictionary)
            counter_list = counter_list = create_counter_list(publicDictionary)
            if total_artists_list == ['']:
                print("Sorry, no artists found.")
            else:
                print(max(counter_list))    

        elif user_letter == "m": # Which user has the most likes
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
        user_letter = getNextUserLetter()
    
######################################################################################################################
    
UserName = getUserName()
Dictionary = {}

import os.path
file_exists = os.path.exists(filename)

import os

if file_exists == False:
    append_file(UserName + ':', filename)
    user_input_sort_and_add_to_file()
    Dictionary = read_preferences(filename)
    user_letter = getNextUserLetter()
else:
    Dictionary = read_preferences(filename)
    Existing_users = list(Dictionary.keys())
    if UserName in Existing_users:
        user_letter = getNextUserLetter()
    elif os.stat(filename).st_size == 0: # If file exists but is empty
        append_file(UserName + ':', filename)
        user_input_sort_and_add_to_file()
        Dictionary = read_preferences(filename)
        user_letter = getNextUserLetter()
    else: # If file exists and is not empty
        append_file('\n' + UserName + ':', filename)
        user_input_sort_and_add_to_file()
        Dictionary = read_preferences(filename)
        user_letter = getNextUserLetter()

publicDictionary = {} # Dictionary with user inputs that do not end with $
Dictionary_keys = list(Dictionary.keys())
for key in Dictionary_keys:
     if key[len(key)-1] != "$":
        publicDictionary[key] = Dictionary[key]
        
menu(user_letter)
terminateQ()
