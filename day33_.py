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
    # Code that checks if there is a streak of 6 heads or tails in a row

print('Chance of streak: %s%%' % (number_of_streaks / 100))
