import requests
import pandas as pd

genus = []
name = []
fruit_id = []
family = []
order = []
nt_classes = []


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


def user_input():
    """Obtains user input on what information is required"""

    print("The Fruits table has the following information:\n\t1. Genus\n\t2. Name\n\t3. ID\n\t"
          "4. Order\n\t5. Nutrition Information")
    info = input("What information do you need?\n")

    if isinstance(info, str):  # check if the user input has alphabet characters only
        if info.lower().strip() == 'nutrition information':
            print("Which nutrition information do you need?\n\t"
                  "1. Carbohydrates\n\t2. Protein\n\t3. Fat\n\t4. Calories\n\t5. Sugar")
            nutr = input().lower()
            print(f"You have selected to view {nutr} information.")
            return nutr
        else:
            print(f"You have selected to view the {info}.")  # inform user of choice before table is displayed
            return info.lower()
    else:
        print("Please enter valid input.")


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
    return full_fruit_df


def save_data(data_frame):
    """Save the created dataframe into a csv file"""
    data_frame.to_csv('fruit_info.csv', index=False)


# parse_json((get_data()))
# print(nt_classes)
# user_input()
# create_dataframe()
# greet_user()
