entered = []
found = False

while not found:
    element = input("Enter element: ")
    if element == "0":
        found = True
    else:
        entered.append(int(element))

max = entered[0]
min = entered[0]

sing_digit = 0
doub_digit = 0
trip_digit = 0

for ele in entered:
    if ele > max:
        max = ele
    if ele < min:
        min = ele
    if len(str(ele)) == 3:
        trip_digit += 1
    elif len(str(ele)) == 2:
        doub_digit += 1
    elif len(str(ele)) == 1:
        sing_digit += 1
    

print("Greatest element is: ",max)
print("Least element is: ",min)

print("No. of Single digit elements: ",sing_digit)
print("No. of Double digit elements: ",doub_digit)
print("No. of Triple digit elements: ",trip_digit)
