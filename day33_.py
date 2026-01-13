# spams = ['apples', 'bananas', 'tofu', 'cats', 'dogs']
# # spams = []

# def org_list(lsts):
#     if not lsts:
#         return ""
#     string = ""
#     for lst in lsts:
#         if lst != lsts[-1]:
#             string += lst
#             string += ", "
#         else:
#             string += "and "
#             string += lst
#     return string


# print(org_list(spams))

"""Coin Flip Streaks"""

import random

number_of_streaks = 0

for experiment_number in range(10000):  # Run 100,000 experiments total.
    # Code that creates a list of 100 'heads' or 'tails' values
    rand_lst = [random.choice(["H", "T"]) for i in range(100)]
    # Code that checks if there is a streak of 6 heads or tails in a row
    for i in range(100):
        if rand_lst[i:i+6] == ['T','T','T','T','T','T'] or \
        rand_lst[i:i+6] == ['H','H','H','H','H','H']:
            number_of_streaks += 1
            break

print('Chance of streak: %s%%' % (number_of_streaks / 100))
