import numpy as np

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

def curve_points(start, middle, end, time_function):
    for t in np.linspace(0, 1)

def get_curve(start, end, middle_point_variation):
    return