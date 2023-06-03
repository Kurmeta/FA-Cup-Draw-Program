import random
import time

def read_teams_from_file(file_path):
    with open(file_path, "r") as file:
        teams = file.readlines()
    return [team.strip() for team in teams]

def generate_fixtures(selected_teams):
    fixtures = []

    for i in range(0, len(selected_teams), 2):
        home_team = selected_teams[i]
        away_team = selected_teams[i+1]
        fixture = (home_team, away_team)
        fixtures.append(fixture)

    return fixtures

def display_quarter_finals(selected_teams):
    print("Quarter-Finals Teams:")
    for i, team in enumerate(selected_teams, start=1):
        time.sleep(0.5)
        print(f"Pick: {i} | Team: {team}")

def display_selected_team(selected_team):
    time.sleep(0.5)
    pick_number, team_name = selected_team
    print(f"Pick: {pick_number} | Selected Team: {team_name}")

def display_fixture(fixture):
    home_team, away_team = fixture
    print("------------------------------------------------")
    time.sleep(0.5)
    print(f"Fixture: {home_team} vs {away_team}")
    print("------------------------------------------------")

def main():
    # Read teams from file
    file_path = "teams.txt"  # Specify the path to your file
    all_teams = read_teams_from_file(file_path)

    # Randomly select eight teams
    selected_teams = random.sample(all_teams, 8)

    # Display the quarter-finals teams
    display_quarter_finals(selected_teams)

    # Add pick numbers to the selected teams
    selected_teams = [(i + 1, team) for i, team in enumerate(selected_teams)]

    for i, selected_team in enumerate(selected_teams, start=1):
        display_selected_team(selected_team)

        if i % 2 == 0:
            fixture = (selected_teams[i - 2][1], selected_teams[i - 1][1])
            display_fixture(fixture)

main()
