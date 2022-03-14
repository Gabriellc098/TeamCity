from math import pi

def circle_area(r):
    if type(r) not in [int, float]:
        raise TypeError("The radius must be real number")
    if r < 0:
        raise ValueError("The value cannot be negative")
    return pi*(r**2)

def circle():
    radius = [3, 2.6, -5, 2j, True]
    for r in radius:
        A = circle_area(r)
        print(f"The area of a circle with r = {r} is {A}")

if (__name__ == '__main__'):
    circle()
