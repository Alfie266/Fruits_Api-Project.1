"""
Main program to run all the code and involved logic.
Import functions &/ classes from fruits_api.py file
"""

import fruits_api as fa

while True:  # Main program loop/logic
    fa.greet_user()
    fa.give_info()

    cont = input("Would you like to proceed? [Y/N]\n")  # Continuation prompt

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
        df_col_filter = fa.select_columns()
        # print(df_filter)

        print("A sample of the information you have chosen is displayed below:")
        filtered_col_df = main_df.filter(df_col_filter)
        print(filtered_col_df)

        cont2 = input("Would you like to find information about specific fruits? [Y/N]\n")  # Continuation prompt
        df_row_filter = fa.select_rows()
        print(df_row_filter)
        # final_df = filtered_col_df[filtered_col_df['Name'].isin(df_row_filter)]
        # print(final_df)
        print("The filtered information you require is displayed below:")
        final_df = filtered_col_df.query('Name in @df_row_filter')
        print(final_df)

        break
