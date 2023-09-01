import requests
import csv

# Static URL to pull team list from API
url_team = "https://fantasy.premierleague.com/api/bootstrap-static/"

#Make a GET Call to url_team
response_teams = requests.get(url_team)

#Successfull Response
if response_teams.status_code == 200:
    #Extract json data from URL
    json_teams = response_teams.json()

    #Extract Team data from json
    elements_teams = json_teams["teams"]
    
    with open(f"C:\FPL Database\SQL Journal\Python Scrape\Teams.csv", "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)

            #Loop through and pull out Team details from API
            for team in elements_teams:
                team_name = team["name"]
                abbrv = team["short_name"]
                code = team["code"]

                writer.writerow([team_name,abbrv,code])
    print("Saving Teams")
else: #If unsuccessful then print message
    print("You've fucked it somewhere lad")