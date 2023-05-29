"""
Script that allows users to interact with the API.
The function is given a "Character Name" it returns info about the
character, location and the "episode/s" where is present
"""

import requests
from pprint import pprint

def character_info_extractor(character_name):
    sut_url = "https://rickandmortyapi.com/api"  # base url

    # getting character data from character resource using character_name param
    response = requests.get(f"{sut_url}/character/?name={character_name}")
    if response.status_code != 200:
        print("Error: Character not found!!!")
        return
    character_data = response.json()["results"][0]  # first position of results tag

    # getting the location data from location resource
    location_url = character_data["location"]["url"]
    response = requests.get(location_url)
    location_data = response.json()

    # getting the episodes data from episode resource
    episodes = character_data["episode"]
    episode_data = []
    for episode_url in episodes:
        response = requests.get(episode_url)
        episode_info = response.json()
        # I search and save in var the values of fields: id, name and length of characters tag
        episode_data.append({
            "episode_id": episode_info["id"],
            "episode_name": episode_info["name"],
            "characters_count": len(episode_info["characters"])
        })

    # I build the response using the tags.
    # First Character info, second Location info, and third Episode info.
    response = {
        "Character info": {
            "status": character_data["status"],
            "species": character_data["species"],
            "gender": character_data["gender"],
        },
        "Location info": {
            "name": location_data["name"],
            "type": location_data["type"],
            "dimension": location_data["dimension"],
            "residents": location_data["residents"],
        },
        "Episode info": episode_data,
    }

    return response


# print the response function in order to see results in screen
result = character_info_extractor("Jerry Smith")
pprint(result)
