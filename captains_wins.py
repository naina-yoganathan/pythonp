"""
    sort by captain names
"""

import csv
with open("captains.txt") as FH:
    data = csv.reader(FH)
    header = next(data)
    captains_wins = list()
    for row in data:
        # row[0] is captain name
        # row[3] is no. of wins
        # print(f"{row[0]:14} {row[3]:>3}") 
        info = (row[0], row[3])
        captains_wins.append(info)

    captains_wins.sort()
    for captain in captains_wins:
        print(f"{captain[0]:14}{captain[1]:>3}")

    print("first captain is: ", captains_wins[0][0])
    print("last captain is: ", captains_wins[-1][0])
    
