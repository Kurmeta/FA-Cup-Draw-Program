import random
import time
import tkinter as tk

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
    text = "Quarter-Finals Teams:\n"
    for i, team in enumerate(selected_teams, start=1):
        text += f"Pick: {i} | Team: {team}\n"
    return text

def display_selected_team(selected_team):
    pick_number, team_name = selected_team
    text = f"Pick: {pick_number} | Selected Team: {team_name}\n"
    return text

def display_fixture(fixture):
    home_team, away_team = fixture
    text = f"Fixture: {home_team} vs {away_team}\n"
    return text

def main():
    # Read teams from file
    file_path = "teams.txt"  # Specify the path to your file
    all_teams = read_teams_from_file(file_path)

    # Randomly select eight teams
    selected_teams = random.sample(all_teams, 8)

    # Initialize Tkinter window
    window = tk.Tk()
    window.title("Team Selection and Fixtures")
    window.geometry("400x400")

    # Create text widget for displaying information
    text_widget = tk.Text(window, height=20, width=40)
    text_widget.pack()

    # Display the quarter-finals teams
    quarter_finals_text = display_quarter_finals(selected_teams)
    text_widget.insert(tk.END, quarter_finals_text)
    text_widget.update()

    # Add pick numbers to the selected teams
    selected_teams = [(i + 1, team) for i, team in enumerate(selected_teams)]

    for i, selected_team in enumerate(selected_teams, start=1):
        selected_text = display_selected_team(selected_team)
        text_widget.insert(tk.END, selected_text)
        text_widget.update()

        if i % 2 == 0:
            fixture = (selected_teams[i - 2][1], selected_teams[i - 1][1])
            fixture_text = display_fixture(fixture)
            text_widget.insert(tk.END, fixture_text)
            text_widget.update()

        time.sleep(0.5)

    window.mainloop()

main()