import random
import time

teams = ["Team 1", "Team 2", "Team 3", "Team 4", "Team 5", "Team 6", "Team 7", "Team 8"]
draw_numbers = [1, 2, 3, 4, 5, 6, 7, 8]
leagues = ["Premier League", "Premier League", "Championship", "Championship", "League One", "League One", "League Two", "League Two"]

def generate_fixtures(selected_teams):
    fixtures = []

    for i in range(0, len(selected_teams), 2):
        home_team = selected_teams[i]
        away_team = selected_teams[i+1]
        fixture = (home_team[1], away_team[1])
        fixtures.append(fixture)

    return fixtures

def display_quarter_finals():
    print("Quarter-Finals Teams:")
    for draw_number, team, league in zip(draw_numbers, teams, leagues):
        time.sleep(0.5)
        print(f"Pick: {draw_number} | Team: {team} | League: {league}")

def display_selected_team(selected_team):
    time.sleep(0.5)
    draw_number, team_name = selected_team
    print(f"Pick: {draw_number} | Selected Team: {team_name}")

def display_fixture(fixture):
    home_team, away_team = fixture
    print("------------------------------------------------")
    time.sleep(0.5)
    print(f"Fixture: {home_team} vs {away_team}")
    print("------------------------------------------------")

def ordinal(n):
    suffix = "th"
    if 11 <= (n % 100) <= 13:
        suffix = "th"
    else:
        suffix = ["th", "st", "nd", "rd", "th"][min(n % 10, 4)]
    return f"{n}{suffix}"

def main():
    display_quarter_finals()

    selected_teams = [(draw_numbers[i], teams[i]) for i in range(len(teams))]
    random.shuffle(selected_teams)

    for i, selected_team in enumerate(selected_teams, start=1):
        display_selected_team(selected_team)

        if i % 2 == 0:
            fixture = (selected_teams[i - 2][1], selected_teams[i - 1][1])
            display_fixture(fixture)

main()
