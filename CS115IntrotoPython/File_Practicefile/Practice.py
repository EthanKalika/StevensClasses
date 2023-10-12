def createDictionaryFromFile(filename):
    """
    Input: Filename
    Dictionary: Containig contents of file
    """
    Ourdict = {}
    with open(filename, "r") as f:
        for line in f:
            list1 = line.strip().split(":")
            key = list1[0]
            list2 = list1[1].split(",")
            Ourdict[key] = list2
        return Ourdict
