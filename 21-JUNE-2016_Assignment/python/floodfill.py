def floodfill(canvas, origin, val):
    val_at_origin = canvas[origin[0]][origin[1]]

    if canvas[origin[0]][origin[1]] != val:
        canvas[origin[0]][origin[1]] = val

        if (len(canvas) > origin[0] + 1) and (canvas[origin[0] + 1][origin[1]] == val_at_origin):
            floodfill(canvas, [origin[0] + 1, origin[1]], val)

        if (0 <= origin[0] - 1) and (canvas[origin[0] - 1][origin[1]] == val_at_origin):
            floodfill(canvas, [origin[0] - 1, origin[1]], val)

        if (len(canvas[0]) > origin[1] + 1) and (canvas[origin[0]][origin[1] + 1] == val_at_origin):
            floodfill(canvas, [origin[0], origin[1] + 1], val)

        if (0 <= origin[1] - 1) and (canvas[origin[0]][origin[1] - 1] == val_at_origin):
            floodfill(canvas, [origin[0], origin[1] - 1], val)

canvas = [
[3,2,3,4,3],
[2,3,3,4,0],
[7,3,3,5,3],
[6,5,3,4,1],
[1,2,3,3,3]
]

print("Canvas before filling:")
for i in range(len(canvas)):
    print canvas[i]

origin = [0,2]
new_value = 2

print "~" * 30
print("Origin is {} and new_value is {}").format(origin, new_value)
print "~" * 30

floodfill(canvas, origin, new_value)
print("Canvas after filling:")
for i in range(len(canvas)):
    print canvas[i]
print "~" * 30

origin = [0,2]
new_value = 1

print "~" * 30
print("Origin is {} and new_value is {}").format(origin, new_value)
print "~" * 30

floodfill(canvas, origin, new_value)
print("Canvas after filling second time:")
for i in range(len(canvas)):
    print canvas[i]
print "~" * 30
