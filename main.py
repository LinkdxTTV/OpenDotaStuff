import opendota
import json
from datetime import datetime

# pip install pyopendota

linkdx = "33579516"


def main():
    # Init some background data
    with open('heroes.json') as heroes:
        data = json.load(heroes)

    client = opendota.OpenDota()
    matches = client.get_player_matches(linkdx, days=1)
    for match in matches:
        date = datetime.fromtimestamp(match['start_time'])
        print("On", date, "Linkdx played")
        print("    "+data[str(match['hero_id'])]['localized_name'])


main()

# https://docs.opendota.com/#tag/matches%2Fpaths%2F~1matches~1%7Bmatch_id%7D%2Fget
# https://pyopendota.readthedocs.io/en/latest/readme.html#get-common-entities
# https://github.com/odota/dotaconstants
