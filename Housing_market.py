import pandas as pd

class HousingMarketAnalyzer:
    def __init__(self, data_file):
        # Initializing the class with data from the csv file
        self.data = pd.read_csv(data_file)
        self.keep_going = True

    def display_menu(self):
        # The main menu, The program will consist 
        # of 3 options of activities to view and perform 
        # to help with your home search.
        print()
        print("Welcome to Realistic Housing")
        print("Please select which option you would like to explore")
        print("1. Se based on price")
        print("2. Se based on wants")
        print("3. Se based on average")
        print()

    def find_homes_by_price(self):
        # this is option 1, find homes by price.
        print()
        max_price = input("Please enter the Maximum amount amount you want to spend:$ ")
        max_price = float(max_price)
        
        # this Filters through the data set using the maximum price given 
        # as a search reference. The information is then stored in selected_columns
        # then sorted, and displayed.
        affordable_homes = self.data[self.data["price"] <= max_price]
        selected_columns = ["bedroom_count", "net_sqm", "floor", "age", "price"]
        sorted_homes = affordable_homes[selected_columns].sort_values(by="price", ascending=True)

        print("House Available for Less than or Equal to ${}:".format(max_price))
        print(sorted_homes)

        # Checks to verify if the user wants to leave the program.
        stop_or_go = input("Stop looking or keep going? (s/g): ").strip().lower()
        if stop_or_go != "g":
            self.keep_going = False

    def find_homes_by_preferences(self):
        # This is for option 2 find homes by preferences. This is 
        # using The participants given information to sort through, 
        # and Find homes that will best suit their wants.
        print()
        print("please tell us a little bit about your dream home!")
        
        # Collects and stores, the three main attributes of ("footage", 
        # "number of bedrooms", and "age of home") to be used in looking
        # through our data set.
        desired_footage = float(input("what is the Square footage in meters(example 10,or 43, or 22.234): "))
        desired_bedrooms = int(input("Number of bedrooms(example 1, or 5): "))
        desired_age = int(input("Age of the house(example 30, or 5): "))
        
        # This is comparing the Desired item for the home to the list 
        # of data and combining them to create a similarity score. i am
        # squaring each item to keep it from canceling each other out.
        self.data["similarity_score"] = (
            (self.data["net_sqm"] - desired_footage) ** 2 +
            (self.data["bedroom_count"] - desired_bedrooms) ** 2 +
            (self.data["age"] - desired_age) ** 2
        )
        
        # This is sorting through the similarities in the data to give
        # us a list of the closest matching homes to the users dream home.
        sorted_data = self.data.sort_values(by="similarity_score")
        
        # organizing the desire data to display in a readable order for the 
        # user to better understand what they were looking at. I am selecting
        # to only show the top few lines, or the closest matches when displayed.
        closest_matches = sorted_data[["net_sqm", "bedroom_count", "age", "price"]].head()
        
        # in case there are no matches this will give the user 
        # some feedback.
        if not closest_matches.empty:
            print("Closest Matches:")
            print(closest_matches)
        else:
            print("No matching houses found.")
        
        # Checks to verify if the user wants to leave the program.
        stop_or_go = input("Stop looking or keep going? (s/g): ").strip().lower()
        if stop_or_go != "g":
            self.keep_going = False

    def find_average_home_price(self):
        # This is option 3 Finding the average home price in the data set.
        # This is selecting and storing the information given under "price" 
        # Running through The lines of numbers and identifying the average 
        # and Storing it in a variable. Then printing the information.
        average_price = self.data["price"].mean()
        print("Average cost of a home in the dataset: ${:.2f}".format(average_price))
    
        # Checks to verify if the user wants to leave the program.
        stop_or_go = input("Stop looking or keep going? (s/g): ").strip().lower()
        if stop_or_go != "g":
            self.keep_going = False

    def run(self):
        # This is a loop that pulls from each of the functions, 
        # to Provide a main menu and instructions for use. 
        # As well as providing a closing thank you.
        while self.keep_going:
            self.display_menu()
            option_selection = input("Please input: 1, 2, or 3: ")

            if option_selection == "1":
                self.find_homes_by_price()

            elif option_selection == "2":
                self.find_homes_by_preferences()

            elif option_selection == "3":
                self.find_average_home_price()

        print()
        print("Thank you, come again")

if __name__ == "__main__":
    # This is where I entered the data set. i am using 
    # a data set from kaggle call housing market prices
    # Which I have renamed "hous.csv"
    analyzer = HousingMarketAnalyzer("house.csv")
    analyzer.run()
