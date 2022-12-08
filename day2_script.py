f = open("Day2.txt", "r")

#creating a copy of the list given to us
item_list = []

#stripping unwanted characters in each item
for item in f:
    item = item.strip()
    item_list.append(item)

#following the strategy guide
score = 0
# A, X for Rock value of 1 
# B, Y for Paper value of 2
# C, Z for Scissors value of 3 

# Function that converts the letters to numbers
def letter_to_num(letter):
    value = 0
    if letter == 'A' or letter == 'X':
        value = 1
    elif letter == 'B' or letter == 'Y':
        value = 2
    elif letter == 'C' or letter == 'Z':
        value = 3

    return value   

def code_to_value(opponents_letter, outcome):
    #if the outcome is to draw
    my_letter = 0
    if outcome == 2:
        my_letter = opponents_letter
    #if the outcome is to lose
    elif outcome == 1:
        matrix = {
            2: 1,
            3: 2,
            1: 3
        }
        my_letter = matrix[opponents_letter]
    #if the outcome is to win
    else:
        matrix = {
            1: 2,
            2: 3,
            3: 1
        }
        my_letter = matrix[opponents_letter]
    return my_letter


# 1 - 2 = -1 win
# 2 - 3 = -1 win
# 3 - 1 = 2 win
# n - n =  0 tie
# 2 - 1 = 1 lose
# 3 - 2 = 1 lose
# 1 - 3 = -2 lose
# Outcome values 
# 0 for loss, 3 for draw, 6 for win
strategy = []
for item in item_list:
    # if I win
    # 1 - 2 = -1
    # if they win 
    # 2 - 1 = 1
    # if draw
    # 3 - 3 = 0
    # This means we can subtitute the letters for numbers then
    # calculate the outcome based on that.
    item_container = []
    for letter in item:
        letter = letter_to_num(letter)
        item_container.append(letter)
    strategy.append([item_container[0], code_to_value(item_container[0],item_container[2])])

for pair in strategy:
    result = pair[0] - pair[1] 
    score_added = 0
    #winning condition
    if result == -1 or result == 2:
        score_added = pair[1] + 6
        score += score_added
        print('We won. The pair is {0}. Current score is {1}'.format(pair, score_added))
    #losing condition
    elif result == 1 or result == -2:
        score_added = pair[1] + 0
        score += score_added
        print('We lost. The pair is {0}. Current score is {1}'.format(pair, score_added))
    #tie condition
    else:
        score_added = pair[1] + 3
        score += score_added
        print('We drew. The pair is {0}. Current score is {1}'.format(pair, score_added))
    
print(score)