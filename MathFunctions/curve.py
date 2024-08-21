import numpy as np
import math
import random
import matplotlib.pyplot as plt
import time
def quadratic_interpolation(start, mid, end, t):
    """
    Calculate a point along the quadratic curve defined by the start, mid, and end points.
    
    Parameters:
        start (tuple): The start point (x0, y0).
        mid (tuple): The midpoint (x1, y1).
        end (tuple): The end point (x2, y2).
        t (float): The interpolation parameter, where 0 <= t <= 1.
        
    Returns:
        tuple: The interpolated point (x, y) on the quadratic curve.
    """
    if not (0 <= t <= 1):
        raise ValueError("Parameter t must be between 0 and 1")

    x0, y0 = start
    x1, y1 = mid
    x2, y2 = end

    # Compute the interpolated x and y
    x = (1 - t) ** 2 * x0 + 2 * (1 - t) * t * x1 + t ** 2 * x2
    y = (1 - t) ** 2 * y0 + 2 * (1 - t) * t * y1 + t ** 2 * y2

    return (x, y)

def get_curve_points(start, middle, end, time_function):
    points = []
    for t in np.linspace(0, 1, 250):
        x = time_function(t)
        point = quadratic_interpolation(start,middle,end, x)
        points.append((math.floor(point[0]), math.floor(point[1])))

    return points


def get_mid_point(start, end, variation):
    line_mid = ((start[0]+end[0])/2,(start[1]+end[1])/2)
    #angle
    alpha=2*math.pi*random.random()
    #radius
    r = variation*math.sqrt(random.random())
    

    x=r*math.cos(alpha) + line_mid[0]
    y=r*math.sin(alpha) + line_mid[1]
    return (x,y)

def convert_curve_to_relative(curve,start_pos):
    new_curve=[]
    new_curve.append((curve[0][0]-start_pos[0], curve[0][1]-start_pos[1]))
    for i in range(len(curve)-1):
        new_curve.append((curve[i+1][0]-curve[i][0], curve[i+1][1]-curve[i][1]))
    return new_curve
def get_curve(start, end, middle_point_variation, time_function, middle_of_screen):
    midpoint = get_mid_point(start, end, middle_point_variation)
    points = get_curve_points(start, midpoint, end, time_function)
    relative = convert_curve_to_relative(points, middle_of_screen)
    return relative

def sigmoid_time_func(x):
    return 1/(1+(10000**(-x+0.5)))


"""while True:
    curve = get_curve((0,0),(1,1), 0.75, sigmoid_time_func)
    x=np.array([i[0] for i in curve])
    y=np.array([i[1] for i in curve])
    plt.plot(x, y, 'o')
    plt.show()
    time.sleep(2)
    plt.close()"""