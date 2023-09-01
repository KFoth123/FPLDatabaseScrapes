import requests
import csv

def get_standings(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()['standings']['results']
    else:
        print(f"Error getting standings: {response.status_code}")
        return []

def get_player_details(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        player_details = response.json()
        for player_codes in player_details['elements']:
            if player_codes['id'] == player_id:
                players = player_codes['code']
                return players
    else:
        print(f"Error getting player details: {response.status_code}")
        return []

def get_picked_players(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()['picks']
    else:
        print(f"Error getting picked players: {response.status_code}")
        return []
    
def get_transfer_cost(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()['entry_history']
    else:
        print(f"Error getting transfer cost: {response.status_code}")
        return []

def get_individual_player_points(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        player_data = response.json()
        for player_points in player_data['elements']:
            if player_points['id'] == player_id:
                stats = player_points['stats']
                total_points = stats['total_points']
                return total_points

    else:
        print(f"Error getting individual player points: {response.status_code}")
        return []

def save_to_csv(data, filename):
    with open(f"C:\FPL Database\SQL Journal\Python Scrape\Gameweek{gameweek}.csv", 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['TeamCode', 'GameWeek','PlayerCode', 'GameWeekPoints', 'Multiplier','TransferCost']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

if __name__ == "__main__":
    league_standings_url = "https://fantasy.premierleague.com/api/leagues-classic/247748/standings/"


    league_standings = get_standings(league_standings_url)
    print("Retrieving League Details")


    data = []


    for entry in league_standings:
        manager_id = entry['entry']
        team_name = entry['entry_name']
        manager_name = entry['player_name']
        gameweek = 3  # Replace with the desired gameweek

        picked_players_url = f"https://fantasy.premierleague.com/api/entry/{manager_id}/event/{gameweek}/picks/"
        team_transfer_cost = get_transfer_cost(picked_players_url)['event_transfers_cost']
        picked_players = get_picked_players(picked_players_url)
        print("Retrieving Picked Players for",team_name)

        for pick in picked_players:
            player_id = pick['element']
            multiplier = pick['multiplier']

            player_details_url = f"https://fantasy.premierleague.com/api/bootstrap-static/"#New
            player_details = get_player_details(player_details_url)#Stuff
            player_code = player_details#Here

            player_points_url = f"https://fantasy.premierleague.com/api/event/{gameweek}/live/"
            player_points_data = get_individual_player_points(player_points_url)
            print("Retrieving Points",player_points_data)

            # Extract the player's points based on their ID from player_points_data

            # Calculate player's gameweek points based on their points and multiplier

            data.append({
                'TeamCode':manager_id,
                'GameWeek':gameweek,
                'PlayerCode':player_code,
                'GameWeekPoints':player_points_data,
                'Multiplier':multiplier,
                'TransferCost':team_transfer_cost
            })

    save_to_csv(data, "C:\FPL Database\SQL Journal\Python Scrape\Gameweek{gameweek}.csv")
    print("Data saved to C:\FPL Database\SQL Journal\Python Scrape\Gameweek",gameweek,".csv")