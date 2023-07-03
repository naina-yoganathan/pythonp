"""
    sort by number of wins 
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
        info = (int(row[3]), row[0])
        captains_wins.append(info)

    captains_wins.sort()
    for captain in captains_wins:
        print(f"{captain[1]:14}{captain[0]:>3}")

    print("first captain is: ", captains_wins[0][1])
    print("last captain is: ", captains_wins[-1][1])

    for captain in captains_wins:
        if captain[1] == "V Kohli":
            print("No. of wins for V kohli: ", captain[0])
            break
