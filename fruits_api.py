import requests
import pandas as pd

genus = []
name = []
fruit_id = []
family = []
order = []
nt_classes = []
acc_resp = ['genus', 'name', 'fruit id', 'family', 'order', 'carbohydrates', 'protein', 'fat', 'calories', 'sugar']


def greet_user():
    """
    Greet the user once the program starts, and take the user's name
    Store the user's name in a global variable to be accessed by all functions
    """
    message = "Welcome! What is your name?\n"
    u_name = input(message)
    print(f"\nThank you. We're glad you're here, {u_name}.\nLet's get you started!")


def get_data():
    """Obtain data in json format from the API"""
    url = "https://fruityvice.com/api/fruit/all"  # api url
    response = requests.get(url)
    return response.json()  # json object to be parsed to obtain detailed columns in parse_json()


def parse_json(response):
    """Parse information to get individual columns of data"""
    for i in range(0, len(response)):
        genus.append(response[i]['genus'])
        name.append(response[i]['name'])
        fruit_id.append(response[i]['id'])
        family.append(response[i]['family'])
        order.append(response[i]['order'])
        nt_classes.append(response[i]['nutritions'])

    return


def give_info():
    """Inform the user about the table and what information is available"""
    print("The Fruits table has the following information about fruits.\n\t1. Genus\n\t2. Name\n\t3. ID\n\t"
          "4. Order\n\t5. Nutrition Information")
    print("The nutrition information includes the following:\n\t"
          "1. Carbohydrates\n\t2. Protein\n\t3. Fat\n\t4. Calories\n\t5. Sugar")


def user_input():
    """Obtains user input on what information is required"""

    info = input()

    if isinstance(info, str):  # check if the user input has alphabet characters only
        print(f"You have chosen to view the {info}")
        return info.lower()
    else:
        print("Please enter valid input.")
        return None


def create_dataframe():
    """
    Create the full dataframe from the parsed data.
    Run get_data() and parse_data() within this function, and run user_input() to get desired column.
    """
    parse_json(get_data())
    nutr_df = pd.DataFrame(nt_classes).reset_index(drop=True)
    name_df = pd.DataFrame(list(zip(fruit_id, name, order, family, genus)),
                           columns=['Fruit ID', 'Name', 'Order', 'Family', 'Genus'],
                           ).reset_index(drop=True)
    name_df.reset_index(drop=True, inplace=True)
    nutr_df.reset_index(drop=True, inplace=True)
    full_fruit_df = pd.concat([name_df, nutr_df], axis=1)
    full_fruit_df.set_index('Fruit ID', inplace=True)
    return full_fruit_df


def save_data(data_frame):
    """Save the created dataframe into a csv file"""
    data_frame.to_csv('fruit_info.csv', index=False)


def select_columns():
    """Takes user input and filters the dataframe to give the specified data"""
    filter_list = []

    print("What information do you need?")
    column = user_input()
    if column is not None:  # Checks if the user input was accepted in user_input
        if column in filter_list:
            print("You have already added that entry to your requested information.")
        else:
            filter_list.append(column)  # first entry appended to filter_list

            flag = True
            while flag:
                msg1 = input("Would you like to view something else? [Y/N]\n")  # check if user wants more columns
                if msg1 == 'n':
                    print("You have selected to view the following:")  # consider moving/calling from display_selection
                    for crit in filter_list:
                        print(f"\t{crit}")
                    flag = False
                elif msg1 == 'y':
                    msg2 = input("What else do you need?\n")
                    # print("Okay")
                    if msg2 not in filter_list:
                        filter_list.append(msg2)
                    else:
                        break
                    # filter_list.append(msg2) if msg2 not in filter_list else flag = False
                    # print("Your filters have been updated")

    return filter_list


def display_selection():
    """Displays columns that have been chosen by the user"""


# parse_json((get_data()))
# print(nt_classes)
# user_input()
# print(create_dataframe())
# greet_user()
