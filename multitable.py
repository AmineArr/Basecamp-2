lengte = 11
breedte = 11

for row in range(1, lengte):
    print(row, end=" ")
    for col in range(1, breedte):
        print(row * col, end=" ")
    print()
