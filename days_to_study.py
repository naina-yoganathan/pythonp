booked = [ 1, 3, 9, 12, 13, 18, 26, 27, 28, 29 ]
travel = [ 4, 5, 15, 16, 21, 22 ]
study = []
month = range(1, 31)

Busy = booked + travel
for day in month:
    if day not in Busy:
        study.append(day)

study = [day for day in month if day not in booked + travel]
print(study)