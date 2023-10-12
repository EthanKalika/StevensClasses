#"I pledge my honor that I have abided by the Stevens Honor System"
#Ethan Kalika

def change(amount, coins):
    """
    Input: an integer amount that must be reached and a list of possible coin values (the first element is assumed to always be 1)
    Output: The minimum number of coins with which ammount can be made
    """
    if amount == 0:
        return 0
    elif amount < 0 or coins == []:
        return float("inf")
    else:
        use_it = 1 + change(amount - coins[0], coins)
        loose_it = change(amount, coins[1:])
        return min(use_it, loose_it)
