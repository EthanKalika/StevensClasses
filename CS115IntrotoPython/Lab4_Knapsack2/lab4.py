# Ethan Kalika
# "I pledge my honor that I have abided by the Stevens Honor System"

def knapsack(capacity, itemList):
    """
    Input: a capacity and a list containing lists of item weight and cist pairs
    Output: a list whose first element is a number representing the cost of all the stolen items,
    and whose second element is a list containting lists of all the item weights and cost pairs of all the items stolen
    """
    if capacity < 0:
        return [float('-inf'), []]
    elif itemList == [] or capacity == 0:
        return [0, []]
    else:
        var1 = knapsack(capacity - itemList[0][0], itemList[1:])
        use_it = [itemList[0][1] + var1[0], [itemList[0]] + var1[1]]
        loose_it = knapsack(capacity, itemList[1:])
        if use_it[0] >= loose_it[0]:
            return use_it
        return loose_it
