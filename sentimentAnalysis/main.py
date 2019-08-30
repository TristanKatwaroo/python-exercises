from sentiment_analysis import compute_tweets                  # Imports the function from the sentiment_analysis file

done = False                                                                                   # Defines done as false

while not done:                                                                   # Loop runs as long as done is false

    try:

        print()
        keywords = input("Please enter the name of the file containing keywords")      # Prompts user for keyword file
        tweets = input("Please enter the name of the file containing tweets")           # Prompts user for tweets file
        results = compute_tweets(tweets, keywords)                  # Calls the compute_tweets function to get results
        print("** Sentiment analysis complete! **")                                         # End statement is printed
        print(results)                                                                           # Results are printed
        print()

        done = True                                                  # Makes done become true and exits the while loop

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
