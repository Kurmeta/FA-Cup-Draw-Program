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
    team_name = selected_team
    text = f"Pick {draw_index + 1}: {team_name}\n"
    return text


def display_fixture(fixture):
    home_team, away_team = fixture
    text = f"{home_team} vs {away_team}\n"
    return text

def draw_team(selected_teams):
    global draw_index, pick_text, fixture_text

    if draw_index < len(selected_teams):
        selected_team = selected_teams[draw_index]
        selected_text = display_selected_team(selected_team)
        pick_text.insert(tk.END, selected_text)

        if draw_index % 2 == 1:
            fixture = (selected_teams[draw_index-1], selected_teams[draw_index])
            fixture_text.insert(tk.END, display_fixture(fixture))

        draw_index += 1
        window.after(1000, draw_team, selected_teams)


def main():
    # Read teams from file
    file_path = "teams.txt"  # Specify the path to your file
    all_teams = read_teams_from_file(file_path)

    # Randomly select eight teams
    selected_teams = random.sample(all_teams, 8)

    # Initialize Tkinter window
    global window, pick_text, fixture_text
    window = tk.Tk()
    window.title("Team Selection and Fixtures")
    window.geometry("800x400")  # Set the window size

    # Create left frame for teams
    left_frame = tk.Frame(window)
    left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Create middle frame for pick numbers
    middle_frame = tk.Frame(window)
    middle_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Create right frame for fixtures
    right_frame = tk.Frame(window)
    right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Create text widgets for each frame
    teams_text = tk.Text(left_frame, height=10, width=20)
    teams_text.pack(fill=tk.BOTH, expand=True)  # Scale to fit frame

    pick_text = tk.Text(middle_frame, height=10, width=10)
    pick_text.pack(fill=tk.BOTH, expand=True)  # Scale to fit frame

    fixture_text = tk.Text(right_frame, height=10, width=30)
    fixture_text.pack(fill=tk.BOTH, expand=True)  # Scale to fit frame

    # Display the quarter-finals teams
    quarter_finals_text = display_quarter_finals(selected_teams)
    teams_text.insert(tk.END, quarter_finals_text)

    # Add pick numbers to the selected teams
    global draw_index
    draw_index = 0

    # Start the draw simulation
    window.after(1000, draw_team, selected_teams)

    window.mainloop()

main()
