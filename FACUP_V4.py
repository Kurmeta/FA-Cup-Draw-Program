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
    for team in selected_teams:
        text += f"{team}\n"
    return text

def display_selected_team(selected_team):
    pick_number, team_name = selected_team
    text = f"Pick: {pick_number}\n"
    return text

def display_fixture(fixture):
    home_team, away_team = fixture
    text = f"{home_team} vs {away_team}\n"
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

    # Create left frame for teams
    left_frame = tk.Frame(window)
    left_frame.pack(side=tk.LEFT, padx=10, pady=10)

    # Create middle frame for pick numbers
    middle_frame = tk.Frame(window)
    middle_frame.pack(side=tk.LEFT, padx=10, pady=10)

    # Create right frame for fixtures
    right_frame = tk.Frame(window)
    right_frame.pack(side=tk.LEFT, padx=10, pady=10)

    # Create text widgets for each frame
    teams_text = tk.Text(left_frame, height=10, width=20)
    teams_text.pack()
    pick_text = tk.Text(middle_frame, height=10, width=10)
    pick_text.pack()
    fixture_text = tk.Text(right_frame, height=10, width=30)
    fixture_text.pack()

    # Display the quarter-finals teams
    quarter_finals_text = display_quarter_finals(selected_teams)
    teams_text.insert(tk.END, quarter_finals_text)

    # Add pick numbers to the selected teams
    selected_teams = [(i + 1, team) for i, team in enumerate(selected_teams)]

    for i, selected_team in enumerate(selected_teams, start=1):
        selected_text = display_selected_team(selected_team)
        pick_text.insert(tk.END, selected_text)

        if i % 2 == 0:
            fixture = (selected_teams[i - 2][1], selected_teams[i - 1][1])
            fixture_text.insert(tk.END, display_fixture(fixture))

        time.sleep(0.5)

    window.mainloop()

main()
