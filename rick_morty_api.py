import pandas as pd
import requests

url = "https://rickandmortyapi.com/api/"
end_pt = "character"


def main_request(base_url, end_point, x):  # x represents the page number to be returned in the response
    """Call for data from the API"""
    response = requests.get(base_url+end_point + f'?page={x}')
    return response.json()


def get_pages(response):  # the API returns paginated responses
    """Gets the number of pages from the response"""
    pages = response['info']['pages']
    return pages


def parse_json(response):  # response includes a collection of lists
    """Parse json data to obtain required information"""
    char_list = []
    for item in response['results']:
        char = {
            'id': item['id'],
            'name': item['name'],
            'no_eps': len(item['episode'])
        }  # episode is stored as a list in the API
        char_list.append(char)
    return char_list


main_list = []  # list to carry all character id's, names and episode count
data = main_request(url, end_pt, 1)
for i in range(1, get_pages(data)+1):
    print(i)  # to visually see as the program parses the information
    main_list.extend(  # similar to append()
        parse_json(main_request(url, end_pt, i))
    )

df = pd.DataFrame(main_list)
df.to_csv('character_list.csv', index=False)
