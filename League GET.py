import csv
import requests

def get_league(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()['standings']['results']
    else:
        print ("Shit's fucked mate")
        return []

def write_to_csv(data,filename):
    with open(f"C:\FPL Database\SQL Journal\Python Scrape\LeagueTeams.csv", 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Season','Name','Manager','ExternalCode']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

data = []

league_url = "https://fantasy.premierleague.com/api/leagues-classic/247748/standings/"
league = get_league(league_url)
for teams in league:
    season = '23/24'
    name = teams['entry_name']
    manager = teams['player_name']
    code = teams['entry']

    data.append({
        'Season':season,
        'Name':name,
        'Manager':manager,
        'ExternalCode':code
    })
write_to_csv(data,"C:\FPL Database\SQL Journal\Python Scrape\LeagueTeams.csv")
print("Saving the league to ""C:\FPL Database\SQL Journal\Python Scrape\LeagueTeams.csv""")