# Name: Kyle Hsu
# email: hsukt@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date:   11/14/24
# Course #/Section:   IS 4010 001
# Semester/Year:   Fall 2024
# Brief Description of the assignment:  Collaborate to create a project that takes an API and turns it readable and outputs data and saves to a CSV

# Brief Description of what this module does. main statement is entry point that instantiates api.py class. Goes through all the steps to make the API
# readable for the stock AAPL
# Citations: w3 schools, stackoverflow
# Anything else that's relevant: N/A

# main.py

import requests
import csv
from apiPackage.api import API

API_KEY = 'a1bd1e2876ca38ce51fdc546e239d308'
SYMBOL = 'AAPL'

def main():
    # Instantiate the API class
    api_handler = API(api_key=API_KEY, symbol=SYMBOL)
    
    # Fetch data from the API
    api_handler.fetch_data()
    
    # Parse the data and store the result
    parsed_data = api_handler.parse_data()
    
    # Save the parsed data to a CSV file
    api_handler.save_to_csv(parsed_data)

if __name__ == "__main__":
    main()


