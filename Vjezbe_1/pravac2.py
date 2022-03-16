import numpy as np
import matplotlib.pyplot as plt

# Define function that prints the line equation
def print_line_equation(points, save = False, saveName=""):
    #find the slope and intersect
    k = (points[1][1]-points[0][1])/(points[1][0]-points[0][0])
    l = -k*points[0][0]+points[0][1]

    # Print the line equation for different cases
    print("Jednadzba pravca:")
    if(l>0):
        print("y={0:.2f}x+{1:.2f}".format(k,l))
    elif(l<0):
        print("y={0:.2f}x{1:.2f}".format(k,l))
    else:
        print("y={:.2f}x".format(k))

    # Prepare figure and axis
    fig = plt.figure()
    ax = plt.axes()

    # Draw line and optimize axis range
    x = np.linspace(min(points[0][0],points[1][0]) - 0.2*abs(min(points[0][0],points[1][0])), max(points[0][0],points[1][0]) + 0.2*abs(max(points[0][0],points[1][0])), 1000)
    ax.plot(x, k*x+l)

    # Draw two points as red circles
    plt.plot(points[0][0], points[0][1], marker='o', markersize=3, color="red")
    plt.plot(points[1][0], points[1][1], marker='o', markersize=3, color="red")

    # Show or save figure
    if(save):
        fig.savefig("{}.pdf".format(saveName))
    else:
        plt.show()

# User code
points = [[1.5,0.],[-2,5.0]]
print_line_equation(points, True, "pravac")
