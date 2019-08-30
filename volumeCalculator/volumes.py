# Imports the math file (Used for formula involving pi)
import math

def function(shape_type):                                                                 # Defines the function

    # Cube is associated with the number 1, so shape_type is cube
    if shape_type == 1:                                                                  # If shape_type is cube;
        sideLength = float(input('What is the side length of the cube?'))                        # Get dimension;
        # Take the absolute dimension input and yield a calculated result rounded to 2 decimal places;
        cubeVolume = round((abs(sideLength) ** 3), 2)
        # Print the calculated volume;
        print("The volume of a cube with side length {} is: {}".format(sideLength, cubeVolume))
        return cubeVolume                                              # Calculated value is returned to main.py

    # Pyramid is associated with the number 2, so shape_type is pyramid
    elif shape_type == 2:                                                             # If shape_type is pyramid;
        baseLength = float(input('What is the base length of the pyramid?'))                     # Get dimension;
        height = float(input('What is the height of the pyramid?'))                              # Get dimension;
        # Take the absolute dimension inputs and yield a calculated result rounded to 2 decimal places;
        pyramidVolume = round((((abs(baseLength) ** 2) * abs(height))/3), 2)
        # Print the calculated volume;
        print("The volume of a pyramid with base length {} and height {} is: {}".format(baseLength, height, pyramidVolume))
        return pyramidVolume                                           # Calculated value is returned to main.py

    # Ellipsoid is associated with the number 3, so shape_type is ellipsoid
    elif shape_type == 3:                                                           # If shape_type is ellipsoid;
        radius1 = float(input('What is the radius along the x axis of the ellipsoid?'))          # Get dimension;
        radius2 = float(input('What is the radius along the y axis of the ellipsoid?'))          # Get dimension;
        radius3 = float(input('What is the radius along the z axis of the ellipsoid?'))          # Get dimension;
        # Take the absolute dimension inputs and yield a calculated result rounded to 2 decimal places;
        ellipsoidVolume = round(((math.pi * abs(radius1) * abs(radius2) * abs(radius3)) * 4/3), 2)
        # Print the calculated volume;
        print("The volume of an ellipsoid with x radius of {}, y radius of {} and z radius of {} is: {}".format(radius1, radius2, radius3, ellipsoidVolume))
        return ellipsoidVolume                                         # Calculated value is returned to main.py

