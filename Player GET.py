import requests
import csv
from datetime import date

# URL for the API endpoint to retrieve player data
url_players = "https://fantasy.premierleague.com/api/bootstrap-static/"

# Make a GET request to the API endpoint
response_players = requests.get(url_players)

# If the request was successful
if response_players.status_code == 200:
    # Extract the JSON data from the response
    json_data_players = response_players.json()

    # Extract the player data from the JSON data
    elements_players = json_data_players["elements"]

    with open(f"C:\FPL Database\SQL Journal\Python Scrape\Players{date.today().strftime('%y-%m-%d')}.csv", "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ['PlayerName', 'Team', 'TeamCode']
            writer = csv.writer(csvfile)

            # Loop through the player data and write their name, team name, and total points for the gameweek to the CSV file
            for player in elements_players:
                player_name = f"{player['first_name']} {player['second_name']}"
                team_code = player['team_code']
                position = player["element_type"]
                code = player['code']
                
                # Map position IDs to human-readable positions
                positions = {
                    1: "Goalkeeper",
                    2: "Defender",
                    3: "Midfielder",
                    4: "Forward"
                }
                position = positions.get(position, "Unknown")
                
                writer.writerow([player_name, team_code, position, code])
    print("Saving Players to C:\FPL Database\SQL Journal\Python Scrape\Players",{date.today().strftime('%y-%m-%d')},".csv")
else:
    # If the request was unsuccessful, print an error message
    print("Error retrieving player data:", response_players.status_code)
