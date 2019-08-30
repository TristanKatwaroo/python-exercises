from string import ascii_letters                        # Imports the letters of the alphabet from the string function

# This function processes the tweets and keywords, then outputs happiness averages and total number of tweets
def compute_tweets(tweets, keywords):

    tFile = open(tweets, "r", encoding="utf‐8", errors='ignore')           # Opens the tweets file from main or driver
    tLine = tFile.readline()                                                                      # Reads line in file

    keyDictionary = keyDict(keywords)                                          # Defines a dictionary for the keywords

    # Variables used for the sum of each timezone's happiness
    estHappiness = 0
    cstHappiness = 0
    mtHappiness = 0
    pstHappiness = 0
    # Variables used for the total tweet count for each timezone
    estTotal = 0
    cstTotal = 0
    mtTotal = 0
    pstTotal = 0
    # Variable used to determine the end of the file, in order to stop the while loop
    endOfFile = ''

    ALPHABET = ascii_letters                                           # Constant used to give a name to ascii_letters

    try:

        while tLine != endOfFile:               # Loop continues until the tweets.txt line reaches the end of the file

            lat = determineLat(tLine, tFile)           # Identifies function "determineLat" as a variable for latitude
            long = determineLong(tLine)              # Identifies function "determineLong" as a variable for longitude
            lat = float(lat)                                                       # Converts latitude values to float
            long = float(long)                                                    # Converts longitude values to float

            # Uses the boundaries of the Eastern timezone to determine the origins of a tweet
            if 24.660845 < lat < 49.189787 and -87.518395 < long < -67.444574:                  # If tweet is from EST
                sentiment = determineHappiness(tLine, keyDictionary, ALPHABET)          # Gets sentiment from function
                if sentiment > 0:                              # This line allows us to ignore tweets without keywords
                    estHappiness += sentiment                               # Adds the sentiment value to estHappiness
                    estTotal += 1                # Adds 1 to the total to track the number of tweets for this timezone

            # Uses the boundaries of the Central timezone to determine the origins of a tweet
            elif 24.660845 < lat < 49.189787 and -101.998892 < long < -87.518395:               # If tweet is from CST
                sentiment = determineHappiness(tLine, keyDictionary, ALPHABET)          # Gets sentiment from function
                if sentiment > 0:                              # This line allows us to ignore tweets without keywords
                    cstHappiness += sentiment                               # Adds the sentiment value to estHappiness
                    cstTotal += 1                # Adds 1 to the total to track the number of tweets for this timezone

            # Uses the boundaries of the Mountain timezone to determine the origins of a tweet
            elif 24.660845 < lat < 49.189787 and -115.236428 < long < -101.998892:               # If tweet is from MT
                sentiment = determineHappiness(tLine, keyDictionary, ALPHABET)          # Gets sentiment from function
                if sentiment > 0:                              # This line allows us to ignore tweets without keywords
                    mtHappiness += sentiment                                 # Adds the sentiment value to mtHappiness
                    mtTotal += 1                 # Adds 1 to the total to track the number of tweets for this timezone

            # Uses the boundaries of the Pacific timezone to determine the origins of a tweet
            elif 24.660845 < lat < 49.189787 and -125.242264 < long < -115.236428:              # If tweet is from PST
                sentiment = determineHappiness(tLine, keyDictionary, ALPHABET)          # Gets sentiment from function
                if sentiment > 0:                              # This line allows us to ignore tweets without keywords
                    pstHappiness += sentiment                               # Adds the sentiment value to pstHappiness
                    pstTotal += 1                # Adds 1 to the total to track the number of tweets for this timezone

            tLine = tFile.readline()                                       # Proceeds to the next line until loop ends

        estAvg = estHappiness / estTotal                   # Calculates the average happiness for the Eastern timezone
        cstAvg = cstHappiness / cstTotal                   # Calculates the average happiness for the Central timezone
        mtAvg = mtHappiness / mtTotal                     # Calculates the average happiness for the Mountain timezone
        pstAvg = pstHappiness / pstTotal                   # Calculates the average happiness for the Pacific timezone

        # This segment prints the results in a readable format
        pEstAvg = print("Eastern happiness average is: " + str(estAvg))
        pEstTotal = print("Eastern total number of tweets tweets is: " + str(estTotal))
        pCstAvg = print("Central happiness average is: " + str(cstAvg))
        pCstTotal = print("Central total number of tweets is: " + str(cstTotal))
        pMtAvg = print("Mountain happiness average is: " + str(mtAvg))
        pMtTotal = print("Mountain total number of tweets is: " + str(mtTotal))
        pPstAvg = print("Pacific happiness average is: " + str(pstAvg))
        pPstTotal = print("Pacific total number of tweets is: " + str(pstTotal))

        # This segment combines all the averages together and the totals together
        averages = pEstAvg and pCstAvg and pMtAvg and pPstAvg
        totals = pEstTotal and pCstTotal and pMtTotal and pPstTotal

        # This segment combines the averages and totals
        results = averages and totals

        return results                                                       # Returns results to main.py or driver.py

    # This segment handles various errors with the use of exceptions
    except IOError:
        print("TWEET COUNT ZERO: One or more files were not found. Empty list returned, please try again.")
    except ValueError:
        print("TWEET COUNT ZERO: file contents invalid, please try again.")
    except ZeroDivisionError:
        print("TWEET COUNT ZERO: No tweets found, please try again.")
    except RuntimeError as error:
        print("Error:", str(error))
    except IndexError:
        print("Error: List index out of range")

# This function creates a dictionary with the keywords file
def keyDict(keywords):
    dict = {}                                                                              # Dictionary is initialized
    with open(keywords, "r", encoding="utf-8", errors='ignore') as keywordFile:                  # Opens keywords file
        for line in keywordFile:
            line = line.split(",")                       # Splits either end of commas in keywords file to make a list
            keys = line[0]                                                            # Identifies index 0 as the keys
            vals = line[1]                                                          # Identifies index 1 as the values
            dict[keys] = vals                               # Creates a dictionary with the identified keys and values
        return dict                                                                           # Returns the dictionary

# This function allows us to determine the latitude
def determineLat(tLine, tFile):
    tLine = tLine.split()                                                     # Splits the tweet file line into a list
    tLine = [element.strip("[,") for element in tLine]                                # Gets rid of the square bracket
    return tLine[0]                                               # Returns latitude as index 0 of the tweet file line

# This function allows us to determine the longitude
def determineLong(tLine):
    tLine = tLine.split()                                                     # Splits the tweet file line into a list
    tLine = [element.strip("]") for element in tLine]                                 # Gets rid of the square bracket
    return tLine[1]                                              # Returns longitude as index 1 of the tweet file line

# This function allows us to determine the happiness of a tweet
def determineHappiness(tLine, keyDictionary, ALPHABET):
    allowed = set(ALPHABET + ' ')               # Defines the allowed characters as letters of the alphabet and spaces
    tweetList = tLine.split()                                                                  # Splits the tweet list
    sentiment = 0                                                                        # Defines the sentiment value
    for key in tweetList:
        key = ''.join(l for l in str(key) if l in allowed)                     # Only read characters that are allowed
        key = key.lower()                                                                 # Converts text to lowercase
        if key in keyDictionary:
            sentiment = sentiment + int(keyDictionary[key])                # Calculates the sentiment value of a tweet
    return sentiment                                                                     # Returns the sentiment value


