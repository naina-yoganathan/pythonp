found = False

sing_digit = 0
doub_digit = 0
trip_digit = 0

ele1 = input("Enter element: ")
if len(str(ele1)) == 3:
        trip_digit += 1
elif len(str(ele1)) == 2:
        doub_digit += 1
elif len(str(ele1)) == 1:
        sing_digit += 1
if ele1 == "0":
    found = True

max = ele1
min = ele1

while not found:
    ele = input("Enter element: ")
    if ele == "0":
        found = True
        break
    else:
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

print("Greatest number is: ",max)
print("Least number is: ",min)

print("No. of Single digit elements: ",sing_digit)
print("No. of Double digit elements: ",doub_digit)
print("No. of Triple digit elements: ",trip_digit)


