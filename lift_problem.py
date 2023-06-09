weights = [64,80,20,110,75,35,94,70,45,65]
capacity = 400
n_people = 0

for wgt in weights:
    capacity -= wgt
    print(f"{wgt = :3}  {capacity = :^7.2f}")
    if capacity < 0:
        break
    n_people += 1

#print("number of people in the first trip: " + str(n_people))
print("number of people in the first trip:" , n_people)
print("number of people in the first trip: {}".format(n_people))
print(f"number of people in the first trip: {n_people}")       #python3.6+
print(f"number of people in the first trip: {n_people=}")