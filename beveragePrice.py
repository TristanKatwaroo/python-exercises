# Task:
# Write a program that computes the cost of a beverage, while factoring in drink type,
# drink size, and drink flavour. Program should also calculate taxes and state when
# an input is invalid.

#Small price ($1.50) will be used as default. Each size up will increase price respectively.
#0 is the default beverage type. Coffee will be 1, and tea will be 2.
price = 1.5
beverage_type = 0

#Program adds additional information onto the output line as inputs are collected.
output = "Order for "

#First the user is prompted to enter their name.
name = input('What is your name? ')
#This if statement allows the program to send an error message if the user enters a space.
if ' ' in name:
    print("Invalid name input, please try again.")
    exit                                              #Ends the code. User must try again.
output += name + ", "                                  #Adds user's name onto output line.

#Next the user is prompted to enter their preferred beverage. Incorrect spelling is not
#accepted and will return an error message.
beverage = input('Would you like coffee or tea? ')
beverage = beverage.lower()                      #Allows program to ignore capitalization.
if (beverage == "c") | (beverage == "coffee"):              #Gives user two input options.
    beverage_type = 1                                       #Adds coffee onto output line.
elif (beverage == "t") | (beverage == "tea"):               #Gives user two input options.
    beverage_type = 2                                          #Adds tea onto output line.
else:
    print("Invalid beverage input, please try again.")
    exit()                                            #Ends the code. User must try again.

#Next the user is prompted to enter their preferred size. Incorrect spelling is not
#accepted and will return an error message.
size = input('What size would you like? ')
size = size.lower()                              #Allows program to ignore capitalization.
if (size == "s") | (size == "small"):                       #Gives user two input options.
    price += 0                        #Does not add anything to output (Default is small).
    output += "a small "
elif (size == "m") | (size == "medium"):                    #Gives user two input options.
    price += 1                                                #Adds medium to output line.
    output += "a medium "
elif (size == "l") | (size == "large"):                     #Gives user two input options.
    price += 1.75                                              #Adds large to output line.
    output += "a large "
else:
    print("Invalid size input, please try again.")
    exit()                                            #Ends the code. User must try again.

#Next the user is prompted to enter their preferred flavour. Incorrect spelling is not
#accepted and will return an error message.
flavour = input('What flavour would you like? ')
flavour = flavour.lower()                        #Allows program to ignore capitalization.
#This section adds flavouring to the user's drink. User is only allowed to enter flavours
#for their respective drink.
if (beverage_type == 1) & ((flavour == "v") | (flavour == "vanilla")):
    price += 0.25                                                     #Adds $0.25 to cost.
    output += "coffee with vanilla flavouring"
elif (beverage_type == 1) & ((flavour == "c") | (flavour == "chocolate")):
    price += 0.75                                                     #Adds $0.75 to cost.
    output += "coffee with chocolate flavouring"
elif (beverage_type == 2) & ((flavour == "l") | (flavour == "lemon")):
    price += 0.25                                                     #Adds $0.25 to cost.
    output += "tea with lemon flavouring"
elif (beverage_type == 2) & ((flavour == "m") | (flavour == "mint")):
    price += 0.5                                                      #Adds $0.50 to cost.
    output += "tea with mint flavouring"
elif (flavour == "") | (flavour == "none"):                         #Adds nothing to cost.
    if beverage_type == 1:
        output = output + "coffee, "
    elif beverage_type == 2:
        output = output + "tea, "
    output += "no flavouring"
else:
    print("Invalid flavour input, please try again.")
    exit()                                            #Ends the code. User must try again.

#Lastly, the program must add tax to the final cost.
output += ". This will cost: $" + format((price + (price * 0.13)), '0.2f')

print(output)
