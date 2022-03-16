# creating an empty list
points = [[] for i in range(2)]

# Read coordinates of a point
def read_coordinates(point, i):
    x1 = float(input("Unesite x koordinatu {}. tocke: ".format(i+1)))
    points[i].append(x1)

    y1 = float(input("Unesite y koordinatu {}. tocke: ".format(i+1)))
    points[i].append(y1)

# Print line equation
def print_line_equation(points):
    #find the slope and intersect
    k = (points[1][1]-points[0][1])/(points[1][0]-points[0][0])
    l = -k*points[0][0]+points[0][1]

    # Print line equation for different cases
    print("Jednadzba pravca:")
    if(l>0):
        print("y={0:.2f}x+{1:.2f}".format(k,l))
    elif(l<0):
        print("y={0:.2f}x{1:.2f}".format(k,l))
    else:
        print("y={:.2f}x".format(k))

for i in range(0,2):
    read_coordinates(points, i)

print_line_equation(points)
