# Assignment 2: Volume Calculator
# Tristan Katwaroo (251033194)

# Task:
# Write a program that computes the volume of a cube, a pyramid, and an ellipsoid.
# Program should consist of volumes.py and main.py
# Volumes.py should prompt the user for the necessary dimensions required and perform
# the calculations. Each function should calculate the volume of the shape it
# corresponds to, and print out a message for that shape.

# Algorithm:
# 1. Prompts user for the shape they are interested in
# 2. Checks for valid input
# 3. If invalid, prompts user for a correct input
# 4. If valid, uses the corresponding function from volumes.py
# 5. Prompts the user to enter specific values required to determine the volume of selected shape
#       Cube: a**3 ; where a is the length of a side
#       Pyramid: (1/3) * (b**2) * h ; where b is base length and h is height
#       Ellipsoid: (4/3) * pi * x * y * z ; where each variable is used to represent the 3 radii
# 6. Computes volume
# 7. Returns an output message containing the dimension and volume
# 8. Adds calculated volume to a list
# 9. Repeats steps 1 - 9 until user enters "quit" as shape input
# 10. Prints the list of volumes for each shape, in sorted order, from lowest to highest
# 11. If no calculations were done for a specific shape, a statement is printed
# 11. If user enters "quit" before calculating any volumes, a statement is printed

import volumes                                                                     # Imports the volumes file

# Defines variables
status = 0                                                                                 # Sets status to 0
shape_type = 0                                                                         # Sets shape_type to 0
totalCalculations = 0                                                           # Sets totalCalculations to 0

# Creates a list for each shape
cubeList = []
pyramidList = []
ellipsoidList = []

# status was previously defined as 0 so the while loop is indefinite
while status != 1:
    shape = input('What shape would you like to calculate the volume for?')                 # Get shape input
    shape = shape.lower()                                                             # Ignore capitalization

    if (shape == "q") | (shape == "quit"):                     # The loop breaks if user inputs "q" or "quit"
        break
    else:                                                                                    # Loop continues
        if (shape == "c") | (shape == "cube"):                 # If user inputs "c" or "cube", shape_type = 1
            shape_type = 1                                       # shape_type = 1 is associated with the cube
            totalCalculations += 1                                  # Used for "No calculations..." statement
        elif (shape == "p") | (shape == "pyramid"):         # If user inputs "p" or "pyramid", shape_type = 2
            shape_type = 2                                    # shape_type = 2 is associated with the pyramid
            totalCalculations += 1                                  # Used for "No calculations..." statement
        elif (shape == "e") | (shape == "ellipsoid"):     # If user inputs "e" or "ellipsoid", shape_type = 3
            shape_type = 3                                  # shape_type = 3 is associated with the ellipsoid
            totalCalculations += 1                                  # Used for "No calculations..." statement
        else:                                                      # Return error message and end the program
            print("Invalid shape input, please try again.")
            exit()

    # Uses function from volumes.py
    x = volumes.function(shape_type)                                          # cubeVolume is returned as "x"

    if shape_type == 1:                         # If volume was of a cube, appends the volume to the cubeList
        cubeList.append(x)
    elif shape_type == 2:                 # If volume was of a pyramid, appends the volume to the pyramidList
        pyramidList.append(x)
    elif shape_type == 3:            # If volume was of an ellipsoid, appends the volume to the ellipsoidList
        ellipsoidList.append(x)

cubeList.sort()                                                              # Sorts the list of cube volumes
pyramidList.sort()                                                        # Sorts the list of pyramid volumes
ellipsoidList.sort()                                                    # Sorts the list of ellipsoid volumes

cubeElements = len(cubeList)                                                # Counts the list of cube volumes
pyramidElements = len(pyramidList)                                       # Counts the list of pyramid volumes
ellipsoidElements = len(ellipsoidList)                                 # Counts the list of ellipsoid volumes

# shape_type will always be greater than or equal to zero so this message will be printed every time
if shape_type >= 0:
    print("You have reached the end of your session.")

# Whenever a shape input was given, 1 was added to the totalCalculations (ex. line 51)
# If user inputs "q" or "quit" before any calculations are done, print the statement below
if totalCalculations == 0:
    print("You did not perform any volume calculations.")

# Whenever a shape input was given, 1 was added to the totalCalculations (ex. line 51)
# If program performed 1 or more calculations, print the statement below and proceed with the outputs
if totalCalculations > 0:
    print("The volumes calculated for each shape are:")
    if cubeElements == 0:                                    # Prints a message if cubeList has zero elements
        print("Cube: No shapes entered")
    else:
        print("Cube: " + str(cubeList)[1:-1])                       # Prints cubeList without square brackets

    if pyramidElements == 0:                              # Prints a message if pyramidList has zero elements
        print("Pyramid: No shapes entered")
    else:
        print("Pyramid: " + str(pyramidList)[1:-1])              # Prints pyramidList without square brackets

    if ellipsoidElements == 0:                          # Prints a message if ellipsoidList has zero elements
        print("Ellipsoid: No shapes entered")
    else:
        print("Ellipsoid: " + str(ellipsoidList)[1:-1])        # Prints ellipsoidList without square brackets

