width = int(input())
height = int(input())

for lengte in range(0, height):
    for breedte in range(0, width):
        print((lengte * width + breedte) % 10, end = " ")
    print()