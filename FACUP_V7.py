import random
import sys
import time
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

start_draw_button = None  # Global variable for start_draw_button
# Add a global variable for the simulate button
simulate_button = None  # Global variable for simulate button

# Function to read teams from a file
def read_teams_from_file(file_path):
    with open(file_path, "r") as file:
        teams = file.readlines()
    return [team.strip() for team in teams]

# Function to generate fixtures from selected teams
def generate_fixtures(selected_teams):
    fixtures = []
    for i in range(0, len(selected_teams), 2):
        home_team = selected_teams[i]
        away_team = selected_teams[i+1]
        fixture = (home_team, away_team)
        fixtures.append(fixture)
    return fixtures

# Function to display the quarter-finals teams
def display_quarter_finals(selected_teams):
    text = "Selected Teams:\n"
    for team in selected_teams:
        text += f"{team}\n"
    return text

# Function to display the selected team
def display_selected_team(selected_team):
    team_name = selected_team
    text = f"Pick {draw_index + 1}: {team_name}\n"
    return text

# Function to display the fixture
def display_fixture(fixture):
    home_team, away_team = fixture
    text = f"{home_team} vs {away_team}\n"
    return text

# Function to simulate matches
def simulate_matches(fixtures):
    winning_teams = []
    for fixture in fixtures:
        # Simulate the result of each match (replace with your own logic)
        home_team, away_team = fixture
        winner = random.choice([home_team, away_team])
        winning_teams.append(winner)
    return winning_teams

# Function to display the scores of the fixtures
def display_scores(fixtures, winning_teams):
    scores_window = tk.Toplevel(window)
    scores_window.title("Fixture Scores")
    scores_window.attributes('-fullscreen', True)

    scores_text = tk.Text(scores_window, height=10, width=20)
    scores_text.pack(fill=tk.BOTH, expand=True)

    scores_text.insert(tk.END, "Fixture Scores:\n")
    for i, fixture in enumerate(fixtures):
        home_team, away_team = fixture
        winner = winning_teams[i]
        score_text = f"{home_team} vs {away_team}: {winner} wins\n"
        scores_text.insert(tk.END, score_text)

    # Proceed to next round button
    proceed_to_next_round_button = tk.Button(scores_window, text="Proceed to Next Round",
                                             command=lambda: open_draw_window(winning_teams))
    proceed_to_next_round_button.pack(pady=10)

# Function to draw the team
def draw_team(selected_teams):
    global draw_index, pick_text, fixture_text, start_draw_button

    if len(selected_teams) == 1:
        winner = selected_teams[0]
        display_winner(winner)
        return

    if draw_index >= len(selected_teams):
        # Current round is finished, display the button to proceed to the next round
        proceed_to_next_round_button.pack(pady=10)
        start_draw_button.configure(state=tk.NORMAL)  # Enable the start draw button
        return

    selected_team = selected_teams[draw_index]
    selected_text = display_selected_team(selected_team)
    pick_text.insert(tk.END, selected_text)

    if draw_index % 2 == 1:
        fixture = (selected_teams[draw_index-1], selected_teams[draw_index])
        fixture_text.insert(tk.END, display_fixture(fixture))

    draw_index += 1
    window.after(1000, draw_team, selected_teams)

# Function to simulate the results
def simulate_results():
    global proceed_to_next_round_button, start_draw_button

    # Simulate the matches and display the scores
    fixtures = generate_fixtures(selected_teams)
    winning_teams = simulate_matches(fixtures)
    display_scores(fixtures, winning_teams)

    # Enable the button to proceed to the next round
    proceed_to_next_round_button.configure(state=tk.NORMAL)
    start_draw_button.configure(state=tk.NORMAL)  # Enable the start draw button

# Function to start the draw
def start_draw(teams):
    global selected_teams, draw_index, start_draw_button, simulate_button

    selected_teams = teams

    # Disable the start draw button once it is clicked
    start_draw_button.configure(state=tk.DISABLED)

    # Disable the simulate button until the draw is completed
    simulate_button.configure(state=tk.DISABLED)

    draw_index = 0
    pick_text.delete("1.0", tk.END)
    fixture_text.delete("1.0", tk.END)

    # Start the draw simulation
    draw_team(selected_teams)

    # Enable the simulate button as the draw is completed
    simulate_button.configure(state=tk.NORMAL)

# Function to open the draw window
def open_draw_window(teams):
    window.withdraw()
    main(teams)

# Function to display the winner
def display_winner(winner):
    messagebox.showinfo("FA Cup Winner", f"The winner of the FA Cup is {winner}!")
    sys.exit(0)

# Function to center the main window
def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")

# Main function
def main(teams=None):
    if not teams:
        # Ask the user to select the number of teams
        num_teams = simpledialog.askinteger("Number of Teams", "Select the number of teams (8, 16, 32, 64):")
        if num_teams is None or num_teams not in [8, 16, 32, 64]:
            messagebox.showerror("Error", "Invalid number of teams selected.")
            return
        file_path = "teams.txt"  # Specify the path to your file
        all_teams = read_teams_from_file(file_path)
        selected_teams = random.sample(all_teams, num_teams)
    else:
        selected_teams = teams

    # Initialize Tkinter window
    global window, pick_text, fixture_text, draw_index, start_draw_button, simulate_button
    window = tk.Tk()
    window.title("Team Selection and Fixtures")
    center_window(window)  # Center the main window
    window.attributes('-fullscreen', True)

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

    pick_text = tk.Text(middle_frame, height=10, width=20)
    pick_text.pack(fill=tk.BOTH, expand=True)  # Scale to fit frame

    fixture_text = tk.Text(right_frame, height=10, width=30)
    fixture_text.pack(fill=tk.BOTH, expand=True)  # Scale to fit frame

    # Display the quarter-finals teams
    quarter_finals_text = display_quarter_finals(selected_teams)
    teams_text.insert(tk.END, quarter_finals_text)

    # Add pick numbers to the selected teams
    draw_index = 0

    # Start the draw simulation
    start_draw_button = tk.Button(middle_frame, text="Start Draw", command=lambda: start_draw(selected_teams))
    start_draw_button.pack(pady=10)

    # Simulate results button
    simulate_button = tk.Button(right_frame, text="Simulate Results", command=simulate_results)
    simulate_button.pack(pady=10)
    simulate_button.configure(state=tk.DISABLED)  # Disable the button initially

    # Proceed to next round button (initially disabled)
    proceed_to_next_round_button = tk.Button(right_frame, text="Proceed to Next Round", command=lambda: open_draw_window(selected_teams))
    proceed_to_next_round_button.pack(pady=10)
    proceed_to_next_round_button.configure(state=tk.DISABLED)  # Disable the button initially

    window.mainloop()

if __name__ == "__main__":
    main()
