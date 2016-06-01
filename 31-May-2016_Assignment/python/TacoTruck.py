def placeTruck(arr):
    x = []
    y = []
    truck_x = None
    truck_y = None

    for i in range(len(arr)):
        x.append(arr[i][0])
        y.append(arr[i][1])

    x_max = max(x)
    x_min = min(x)
    y_max = max(y)
    y_min = min(y)

    x_sum = reduce((lambda a,b: a + abs(b)), x, 0)
    y_sum = reduce((lambda a,b: a + abs(b)), y, 0)

    for i in range(x_min, x_max+1):
        tempsum = reduce((lambda a,b: a + abs(b - i)), x, 0)
        if x_sum >= tempsum:
            x_sum = tempsum
            truck_x = i

    for j in range(y_min, y_max+1):
        tempsum = reduce((lambda a,b: a + abs(b - j)), y, 0)
        if y_sum >= tempsum:
            y_sum = tempsum
            truck_y = j

    truck_x = (0 if not truck_x else truck_x)
    truck_y = (0 if not truck_y else truck_y)

    return [[truck_x, truck_y], x_sum+y_sum]

myLocations = [ [10,0], [-1,-10], [2,4] ]
result = placeTruck(myLocations)
print ("The customer locations are {}").format(myLocations)
print ("The optimal position for the truck is {}").format(result[0])
print ("The minimum distance to be covered by customers is {}").format(result[1])
