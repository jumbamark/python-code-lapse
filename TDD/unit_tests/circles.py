from math import pi


def circle_area(r):
    """
    Function that computes the area of a circle
    """
    if type(r) not in [int, float]:
        raise TypeError("The radius must be a non-negative real number")
    if r < 0:
        raise ValueError("The radius cannot be negative.")
    return pi*(r**2)


# Test function
# Assuming the function will work with any input since there is no docstring
# to suggest otherwise
# j is the square root of -1 in python

if __name__ == "__main__":
    radii = [2, 0, -3, 2 + 5j, True, "radius"]
    message = "Area of circle(s) with r = {radius} is {area}."

    for r in radii:
        A = circle_area(r)
        print(message.format(radius=r, area=A))


########
## OUTPUT BEFORE unittest:
## The area is correct for a circle of radius 2
## Area of circle with radius 0 is zero
## The function computes the area of a circle with negative radius, regrettable)
## Function returns a complex area for a circle with complex radius, Hoo-boy
## The area of a circle with radius "True" is pie, insane
## Thankfully the function gives an error when you try finding the area of a circle with "string" as radius
########

"""
The function is a grave dissapointment
Write unit tests to check that the function works properly
Test the function before submitting for review

After unittests:
    - the test fails when checking for negatives (raise ValueError)
    - 
"""
