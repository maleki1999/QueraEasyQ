points = str(input()).split()
if int(points[0]) == int(points[2]):
    print("Vertical")
elif int(points[1]) == int(points[3]):
    print("Horizontal")
else:
    print("Try again")