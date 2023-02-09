"""
Main program to run all the code and involved logic.
Import functions &/ classes from fruits_api.py file
"""

import fruits_api as fa

while True:  # Main program loop/logic
    fa.greet_user()
    fa.give_info()

    cont = input("Would you like to proceed? [Y/N]\n")

    if cont.lower() == "n":  # Terminate program
        break
    else:  # Proceed with the rest of the program logic
        print("Let's continue!")

        fa.parse_json(fa.get_data())  # Send request, parse json response, store in lists in fruits_api module
        print("Data downloaded and parsed successfully.")

        res1 = input("Would you like to view a sample of the data? [Y/N]\n")

        if res1.lower() == "n":  # Proceed with program logic
            print("Thank you. You may proceed.")
        else:  # Get the dataframe and print first 5 rows
            sample_df = fa.create_dataframe()
            print(sample_df.head())

        main_df = fa.create_dataframe()
        fa.select_columns()

        break
