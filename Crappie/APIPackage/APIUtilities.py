# Name: Roman Stryjewski
# email: stryjerj@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date:   11/14/24
# Course #/Section:   IS 4010 001
# Semester/Year:   Fall 2024
# Brief Description of the assignment: Creating code to fetch data from an API file and show the results of that data

# Brief Description of what this module does. - Desribes what to take from the data, as well as creating a csv file to put the data fetched in

# Citations: w3 schools, stackoverflow
# Anything else that's relevant:

# APIUtilities.py

import requests
import csv

class API:
    def __init__(self, api_key, symbol="AAPL"):
        """
        Initializes APIHandler with the API key and stock symbol for data requests.
       
        :param api_key: Your API key for the MarketStack API.
        :param symbol: Stock symbol to request data for.
        """
        self.api_key = api_key
        self.symbol = symbol
        self.base_url = "https://api.marketstack.com/v1/eod"
        self.stock_data = None

    def build_url(self):
        """
        Builds the URL for the API request using the base URL, symbol, and API key.
       
        :return: The complete URL for the API request.
        """
        return f"{self.base_url}?access_key={self.api_key}&symbols={self.symbol}"

    def fetch_data(self):
        """
        Makes a request to the API and stores the result in the `stock_data` attribute.
        """
        url = self.build_url()
        response = requests.get(url)
       
        if response.status_code == 200:
            self.stock_data = response.json()
            print(f"Data successfully retrieved for symbol: {self.symbol}")
        else:
            print(f"Failed to retrieve data: {response.status_code} - {response.text}")
            self.stock_data = None

    def parse_data(self):
        """
        Parses and extracts interesting information from the JSON response.
       
        :return: A dictionary of selected stock data.
        """
        if not self.stock_data or 'data' not in self.stock_data:
            print("No data to parse.")
            return None

        latest_data = self.stock_data['data'][0]  # Get the latest available data

        parsed_data = {
            "Symbol": self.symbol,
            "Date": latest_data['date'],
            "Open": latest_data['open'],
            "High": latest_data['high'],
            "Low": latest_data['low'],
            "Close": latest_data['close'],
            "Volume": latest_data['volume']
        }

        print(f"Stock Data for {self.symbol} on {parsed_data['Date']}:")
        for key, value in parsed_data.items():
            print(f"{key}: {value}")
       
        return parsed_data

    def save_to_csv(self, parsed_data, filename="stock_data.csv"):
        """
        Writes parsed data to a CSV file.
       
        :param parsed_data: A dictionary containing the parsed data.
        :param filename: The name of the CSV file to save data.
        """
        if not parsed_data:
            print("No data to save.")
            return
        
        try:
            with open(filename, mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=parsed_data.keys())
                writer.writeheader()
                writer.writerow(parsed_data)
            print(f"Data successfully saved to {filename}")
        except IOError as e:
            print(f"Failed to save data to CSV: {e}")
