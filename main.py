from eda_utils import basic_info_dataframe, rec_fuction, numeric_information, numeric_information_selection
from categorical_information import counting_information

class Menu:

    def __init__(self, dataframe):
        self.dataframe = dataframe

    def start(self):

        while True:

            print("")
            print("------------- EDA MENU -------------")
            print("1. Basic Information about Data")
            print("2. Information about a Particular Column")
            print("3. Exit")
            print("------------------------------------")

            choice = input("Enter your choice: ")

            if choice == "1":

                basic_info_dataframe(self.dataframe)

            elif choice == "2":

                column = rec_fuction(self.dataframe)

                datatype = ["int32", "int64", "float32", "float64"]

                if self.dataframe[column].dtype in datatype:

                    # numeric_information_selection(self.dataframe, column)
                    numeric_information(self.dataframe, column)

                else:

                    counting_information(self.dataframe, column)

            elif choice == "3":

                print("Exiting Program...")
                break

            else:

                print("Invalid Choice. Please try again.")
