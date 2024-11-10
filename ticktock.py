# DOCSTRING
from tkinter import *
import time
import threading
import sqlite3
import matplotlib.pyplot as plt

# CREATING TKINTER ROOT
root = Tk()
root.title('Chess Clock and Tracker') # Titling the root: Chess Clock and Tracker
root.state('zoomed') # Creating root state = zoomed

# CREATING SQLITE DATABASE CONNECTION
conn = sqlite3.connect("Chess_Tracker.db")
c = conn.cursor()

# FUNCTION: Displays a user's win/loss/draw in a matplotlib piechart
def show_player_statistics():
    """
    Display a pie chart showing win/loss/draw percentages for a specified user ID.
    Retrieves player statistics from the database, creates a pie chart, and displays it.
    """
    try:
        user_id = int(stats_id_entry.get())
    except ValueError:
        print("Invalid user ID. Please enter a valid integer.")
        return
    # Getting player statistics for the specified ID
    c.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    player_data = c.fetchone()
    if player_data: # Creating pie chart
        win_percent = player_data[4]
        loss_percent = player_data[5]
        draw_percent = player_data[6]
        labels = 'Win', 'Losses', 'Draws'
        sizes = [win_percent, loss_percent, draw_percent]
        colors = ['gold', 'lightcoral', 'lightskyblue']
        explode = (0.1, 0, 0)
        plt.figure(figsize=(8, 8))
        plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
        plt.axis('equal')
        plt.title('Win/Loss/Draw Percentages')
        plt.show()
    else:
        print(f"No user found with ID {user_id}")
        label_user_id.config(text=f"No user found with ID {user_id}")


# GUI: GENERAL FRAMES AND WIDGETS
player_info_frame = Frame(root, bg='green', width=1440, height=900)
player_info_frame.place(x=0, y=0)
home_frame = Frame(root, bg='grey', width=1440, height=900)
home_frame_label = Label(home_frame, text="Home Page", font=('Bookman', 80))
game_stats_frame = Frame(root, bg='grey', width=1440, height=900)
game_stats_label = Label(game_stats_frame, text="Game Statistics", font=('Bookman', 80))
black_label = Label(game_stats_frame, text="BLACK", font=("Bookman", 35))
white_label = Label(game_stats_frame, text="WHITE", font=("Bookman", 35))
id_label= Label(game_stats_frame, text="ID", font=("Bookman", 35))
game_number_label = Label(game_stats_frame, text="Games Played", font=("Bookman", 35))
game_moves_label = Label(game_stats_frame, text="Game Moves", font=("Bookman", 35))
time_move_label = Label(game_stats_frame, text="Time Per Move", font=("Bookman", 35))
capture_pawn_label = Label(game_stats_frame, text="1st Pawn Capture", font=("Bookman", 35))
capture_minor_label = Label(game_stats_frame, text="1st Minor Capture", font=("Bookman", 35))
capture_rook_label = Label(game_stats_frame, text="1st Rook Capture", font=("Bookman", 35))
capture_queen_label = Label(game_stats_frame, text="1st Queen Capture", font=("Bookman", 35))
home_gs_button = Button(game_stats_frame, text="HOME", bg='blue', font=("Bookman", 22), width=3, height=1, command=lambda: raise_frame(home_frame))
player_stats_frame = Frame(root, bg='red', width=1440, height=900)
player_stats_label = Label(player_stats_frame, text="Player Statistics", font=('Bookman', 80))
stats_first_name_label = Label(player_stats_frame, text="Firstname", font=("Bookman", 35))
stats_last_name_label = Label(player_stats_frame, text="Lastname", font=("Bookman", 35))
stats_games_played = Label(player_stats_frame, text="Games Played", font=("Bookman", 35))
stats_win_label = Label(player_stats_frame, text="Win Percentage", font=("Bookman", 35))
stats_loss_label = Label(player_stats_frame, text="Loss Percentage", font=("Bookman", 35))
stats_tie_label = Label(player_stats_frame, text="Tie Percentage", font=("Bookman", 35))
stats_moves_label= Label(player_stats_frame, text="Mean Moves Per Game", font=("Bookman", 35))
stats_time_label = Label(player_stats_frame, text="Mean Time Per move", font=("Bookman", 35))
next_ps_button = Button(player_stats_frame, text="NEXT", bg='purple', font=("Bookman", 22), width=3, height=1, command=lambda: raise_frame(home_frame))
home_ps_button = Button(player_stats_frame, text="HOME", bg='blue', font=("Bookman", 22), width=3, height=1, command=lambda: raise_frame(home_frame))
new_game_button = Button(home_frame, text="New Game", font=("Bookman", 32), width=15, height=6, command=lambda: raise_frame(game_player_frame))
new_player_button = Button(home_frame, text="Register New Player", font=("Bookman", 32), width=15, height=6, command=lambda: raise_frame(new_player_frame))
player_stats_button = Button(home_frame, text="Check Player Statistics", font=("Bookman", 32), width=15, height=6, command=lambda: raise_frame(player_info_frame))
game_mode_frame = Frame(root, bg='grey', width=1440, height=900)
game_mode_label = Label(game_mode_frame, text="New Game", font=('Bookman', 80))
select_game_label = Label(game_mode_frame, text="Select Gamemode", font=("Bookman", 32))
stats_id_entry = Entry(player_info_frame)
stats_id_entry.place(x=800, y=10)

# FUNCTION: Raises frames and is called by home/next pages
def raise_frame(frame):
    frame.tkraise()

# VARIABLES: Declaring Global Variables and setting them equal to 0
global whitescore
whitescore = 0
global blackscore
blackscore = 0
def w_capture_queen(score):
    global whitescore
    whitescore += 9
    global blackscore
    blackscore -= 9
    print(whitescore)
    white_score.config(text=f'Material Status: {whitescore}',font=("Bookman", 15))
    black_score.config(text=f'Material Status: {blackscore}', font=("Bookman", 15))
def w_capture_pawn(score):
    print('white captured pawn')
    global whitescore
    whitescore += 1
    global blackscore
    blackscore -= 1
    print(whitescore)
    white_score.config(text=f'Material Status: {whitescore}',font=("Bookman", 15))
    black_score.config(text=f'Material Status: {blackscore}', font=("Bookman", 15))
def w_capture_minor(score):
    print('white captured minor piece')
    global whitescore
    whitescore += 3
    global blackscore
    blackscore -= 3
    print(whitescore)
    white_score.config(text=f'Material Status: {whitescore}',font=("Bookman", 15))
    black_score.config(text=f'Material Status: {blackscore}', font=("Bookman", 15))
def w_capture_rook(score):
    print('white captured rook')
    global whitescore
    whitescore += 5
    global blackscore
    blackscore -= 5
    print(whitescore)
    white_score.config(text=f'Material Status: {whitescore}',font=("Bookman", 15))
    black_score.config(text=f'Material Status: {blackscore}', font=("Bookman", 15))
def b_capture_queen(score):
    print('black captured queen')
    global blackscore
    blackscore += 9
    global whitescore
    whitescore -= 9
    print(blackscore)
    black_score.config(text=f'Material Status: {blackscore}', font=("Bookman", 15))
    white_score.config(text=f'Material Status: {whitescore}',font=("Bookman", 15))
def b_capture_pawn(score):
    print('black captured pawn')
    global blackscore
    blackscore += 1
    global whitescore
    whitescore -= 1
    print(blackscore)
    black_score.config(text=f'Material Status: {blackscore}', font=("Bookman", 15))
    white_score.config(text=f'Material Status: {whitescore}',font=("Bookman", 15))
def b_capture_minor(score):
    print('black captured minor piece')
    global blackscore
    blackscore += 3
    global whitescore
    whitescore -= 3
    print(blackscore)
    black_score.config(text=f'Material Status: {blackscore}', font=("Bookman", 15))
    white_score.config(text=f'Material Status: {whitescore}',font=("Bookman", 15))
def b_capture_rook(score):
    print('black captured major piece')
    global blackscore
    blackscore += 5
    global whitescore
    whitescore -= 5
    print(blackscore)
    black_score.config(text=f'Material Status: {blackscore}', font=("Bookman", 15))
    white_score.config(text=f'Material Status: {whitescore}',font=("Bookman", 15))

# HOME: FRAME AND WIDGETS
home_frame.place(x=0, y=0)
home_frame_label.place(x=500, y=20)
new_game_button.place(x=90, y=350)
new_player_button.place(x=550, y=350)
player_stats_button.place(x=1020, y=350)

# GAME - PLAYERS: FRAME AND WIDGETS
game_player_frame = Frame(root, bg='grey', width=1440, height=900)
game_player_label = Label(game_player_frame, text="New Game", font=('Bookman', 80))
game_register_label = Label(game_player_frame, text="Register Players", font=("Bookman", 32))
white_id_label = Label(game_player_frame, text="WHITE PLAYER ID", font=("Bookman Bold", 30))
id_entry_white = Entry(game_player_frame, font=("Bookman Bold", 30))
black_id_label = Label(game_player_frame, text="BLACK PLAYER ID", font=("Bookman Bold", 30))
id_entry_black = Entry(game_player_frame, font=("Bookman Bold", 30))
home_gp_button = Button(game_player_frame, text="HOME", bg='grey', font=("Bookman", 22), width=3, height=1, command=lambda: raise_frame(home_frame))
game_player_frame.place(x=0, y=0)
game_player_label.place(x=535, y=20)
game_register_label.place(x=600, y=140)
white_id_label.place(x=100, y=400)
id_entry_white.place(x=100, y=450)
black_id_label.place(x=900, y=400)
id_entry_black.place(x=900, y=450)
home_gp_button.place(x=0, y=820)

# GAME - CLOCK: FRAME AND WIDGETS
game_clock_frame = Frame(root, bg='grey', width=1440, height=900)
game_clock_frame.place(x=0, y=0)
white_queen = Button(game_clock_frame, text="Queen Captured (Q)", font=("Bookman", 19), width=14, height=6, command=lambda: [game_stats.capture_piece("white", "queen"), w_capture_queen(whitescore)])
white_queen.place(x=300, y=520)
white_pawn = Button(game_clock_frame, text="Pawn Piece\nCaptured (A)", font=("Bookman", 19), width=14, height=6, command=lambda: [game_stats.capture_piece("white", "pawn"), w_capture_pawn(whitescore)])
white_pawn.place(x=300, y=674)
white_minor = Button(game_clock_frame, text="Minor Piece\nCaptured (W)", font=("Bookman", 19), width=14, height=6, command=lambda: [game_stats.capture_piece("white", "minor"), w_capture_minor(whitescore)])
white_minor.place(x=510, y=520)
white_rook = Button(game_clock_frame, text="Rook Piece\nCaptured (S)", font=("Bookman", 19), width=14, height=6, command=lambda: [game_stats.capture_piece("white", "rook"), w_capture_rook(whitescore)])
white_rook.place(x=510, y=674)
white_score = Label(game_clock_frame, text=f'Material Status: {whitescore}', font=("Bookman", 15))
white_score.place(x=300, y=20)
black_queen = Button(game_clock_frame, text="Queen Captured (P)", font=("Bookman", 19), width=14, height=6, command=lambda: [game_stats.capture_piece("black", "queen"), b_capture_queen(blackscore)])
black_queen.place(x=730, y=520)
black_pawn = Button(game_clock_frame, text="Pawn Piece\nCaptured (:)", font=("Bookman", 19), width=14, height=6, command=lambda: [game_stats.capture_piece("black", "pawn"), b_capture_pawn(blackscore)])
black_pawn.place(x=730, y=674)
black_minor = Button(game_clock_frame, text="Minor Piece\nCaptured (W)", font=("Bookman", 19), width=14, height=6, command=lambda: [game_stats.capture_piece("black", "minor"), b_capture_minor(blackscore)])
black_minor.place(x=940, y=520)
black_major = Button(game_clock_frame, text="Major Piece\nCaptured (L)", font=("Bookman", 19), width=14, height=6, command=lambda: [game_stats.capture_piece("black", "rook"), b_capture_rook(blackscore)])
black_major.place(x=940, y=674)
black_score = Label(game_clock_frame, text=f'Material Status: {blackscore}',font=("Bookman", 15))
black_score.place(x=1000, y=20)

# GAME - STATS: FRAME AND WIDGETS
game_stats_frame.place(x=0, y=0)
game_stats_label.place(x=485, y=20)
black_label.place(x=1150, y=200)
white_label.place(x=800, y=200)
id_label.place(x=470, y=270)
game_number_label.place(x=370, y=340)
game_moves_label.place(x=370, y=410)
time_move_label.place(x=370, y=480)
capture_pawn_label.place(x=370, y=550)
capture_minor_label.place(x=370, y=620)
capture_rook_label.place(x=370, y=690)
capture_queen_label.place(x=370, y=760)
home_gs_button.place(x=0, y=820)

# NEW PLAYER: FRAME AND WIDGETS
new_player_frame = Frame(root, bg='grey', width=1440, height=900)
new_player_label = Label(new_player_frame, text="Register Player", font=('Bookman', 80))
first_name_label = Label(new_player_frame, text="Firstname", font=("Bookman", 35))
last_name_label = Label(new_player_frame, text="Lastname", font=("Bookman", 35))
# email_label = Label(new_player_frame, text="Email", font=("Bookman", 35))
first_name_entry = Entry(new_player_frame, font=("Bookman", 35))
last_name_entry = Entry(new_player_frame, font=("Bookman", 35))
# email_entry = Entry(new_player_frame, font=("Bookman", 35))
reminder_label = Label(new_player_frame, text="", font=("Bookman", 35))
enter_button = Button(new_player_frame, text="Enter", font=("Bookman", 35), command=lambda: enter_user())
next_np_button = Button(new_player_frame, text="NEXT", bg='green', font=("Bookman", 22), width=3, height=1,command=lambda: raise_frame(home_frame), state=DISABLED)
home_np_button = Button(new_player_frame, text="HOME", bg='blue', font=("Bookman", 22), width=3, height=1, command=lambda: raise_frame(home_frame))
new_player_frame.place(x=0, y=0)
new_player_label.place(x=485, y=20)
first_name_label.place(x=270, y=300)
last_name_label.place(x=270, y=400)
# email_label.place(x=270, y=500)
first_name_entry.place(x=510, y=300)
last_name_entry.place(x=510, y=400)
# email_entry.place(x=510, y=500)
reminder_label.place(x=650, y=700)
enter_button.place(x=510, y=600)
next_np_button.place(x=1365, y=820)
home_np_button.place(x=0, y=820)

# PLAYER STATS: FRAME AND WIDGETS
player_stats_frame.place(x=0, y=0)
player_stats_label.place(x=485, y=20)
stats_first_name_label.place(x=670, y=300)
stats_last_name_label.place(x=60, y=370)
stats_games_played.place(x=670, y=440)
stats_win_label.place(x=670, y=510)
stats_loss_label.place(x=670, y=580)
stats_loss_label.place(x=670, y=650)
stats_moves_label.place(x=670, y=720)
stats_time_label.place(x=670, y=790)
next_ps_button.place(x=1365, y=820)
home_ps_button.place(x=0, y=820)

# FUNCTION: Creating function for printing tables
def print_table_data(conn, table_name):
    c = conn.cursor()
    c.execute(f"SELECT * FROM {table_name}")
    rows = c.fetchall()
    for row in rows:
        print(row)

"""Class that has all the attributes so the clock work """
class Clock:
    def __init__(self, game_clock_frame, game_stats):  # Add game_clock_frame as a parameter
        self.master = game_clock_frame
        self.game_clock_frame = game_clock_frame

        self.start_button = Button(self.game_clock_frame, font=("Helvetica", 30), text="Start", command=self.start_thread)
        self.start_button.place(x=660, y=440)

        self.master = game_clock_frame
        self.game_clock_frame = game_clock_frame
        self.game_stats = game_stats  # Reference to the GameStats instance
        self.switch_button_white = Button(self.game_clock_frame, font=('Helvetica', 25), text="MOVE (L Shift)", height=10, width=17, command=self.switch)  # Adding switch buttons for white and black
        self.switch_button_white.place(x=20, y=520)
        self.w_warning_label = Label(self.game_clock_frame, font=('Helvetica', 50), background = "red", text="")
        self.w_warning_label.place(x=300, y=100)
        self.b_warning_label = Label(self.game_clock_frame, font=('Helvetica', 50), background = "red", text="")
        self.b_warning_label.place(x=900, y=100)
        self.switch_button_black = Button(self.game_clock_frame, font=('Helvetica', 25), text="MOVE (R Shift)", height=10, width=17, command=self.switch)
        self.switch_button_black.place(x=1150, y=520)
        self.time_label = Label(self.game_clock_frame, font=("Helvetica", 100), text="W: 00:00:00")
        self.time_label.place(x=20, y=200)
        self.time_label2 = Label(self.game_clock_frame, font=("Helvetica", 100), text="B: 00:00:00")
        self.time_label2.place(x=900, y=200)
        self.time_entry = Entry(self.game_clock_frame, font=("Helvetica", 30))
        self.time_entry.place(x=550, y=10)
        self.label_entry = Label(self.game_clock_frame, text='Enter Time', font=("Helvetica", 30))
        self.label_entry.place(x=700, y=80)



        self.stop_button = Button(self.game_clock_frame, font=("Helvetica", 30), text="Stop", command=self.stop)
        self.stop_button.place(x=660, y=400)
        self.pause_button = Button(self.game_clock_frame, font=('Helvetica', 30), text="Pause", command=self.pause_timer)
        self.pause_button.place(x=660, y=340)
        self.stop_loop = False
        self.paused = False
        self.activetimer = False
        self.bindings() # functon being called

    # Clock: FUNCTION: Key binds which allows user to use shifts instead of buttons
    def bindings(self):
        root.bind('<Shift_L>', lambda event: self.switch())  # for left shift key
        root.bind('<Shift_R>', lambda event: self.switch())  # for right shift key

    # Clock: FUNCTION: Starts threading for clocks
    def start_thread(self):
        t = threading.Thread(target=self.start)
        t.start()

    # Clock: FUNCTION: Update warning labels
    def update_warning_labels(self, label, remaining_seconds):
        original_seconds = self.w_starttime if self.activetimer else self.b_starttime
        threshold_75_percent = 0.75 * original_seconds
        threshold_50_percent = 0.5 * original_seconds
        threshold_25_percent = 0.25 * original_seconds

        if remaining_seconds <= threshold_75_percent:
            label.config(text="Time Reminder", background='Green')
            print('1 MADE IT')
        if remaining_seconds <= threshold_50_percent:
            label.config(text="Half Time", background='Orange')
            print('2 MADE IT')
        if remaining_seconds <= threshold_25_percent:
            label.config(text="LOW TIME", background='Red')  # Adjust the color as needed
            print('3 MADE IT')
        if remaining_seconds > threshold_75_percent:
            label.config(text="")  # Or let the label stay
            print('4 MADE IT')

    # CLASS: FUNCTION: Start the clock and countdown
    def start(self):
        self.stop_loop = False
        hours, minutes, seconds = 0, 0, 0
        hours2, minutes2, seconds2 = 0, 0, 0
        string_split = self.time_entry.get().split(":")
        if len(string_split) == 3:
            hours = int(string_split[0]) # Look through the time format and assign
            # values to corresponding variables
            minutes = int(string_split[1])
            seconds = int(string_split[2])
            hours2 = int(string_split[0])
            minutes2 = int(string_split[1])
            seconds2 = int(string_split[2])
        elif len(string_split) == 2:
            minutes = int(string_split[0])
            seconds = int(string_split[1])
            minutes2 = int(string_split[0])
            seconds2 = int(string_split[1])
        elif len(string_split) == 1:
            seconds = int(string_split[0])
            seconds2 = int(string_split[0])
        else: # IF/Else that displays error message for an invalid time format
            messagebox.showerror("Invalid Time", "Invalid time format")
            print("Invalid time, invalid format")
            return

        full_seconds = (hours * 3600) + (minutes * 60) + seconds # Calculate total
        # seconds for each player's clock
        full_seconds2 = (hours2 * 3600) + (minutes2 * 60) + seconds2
        self.w_starttime = full_seconds # Storing initial time values
        self.b_starttime = full_seconds2

        # Main loop: Countdown until time is up or loop is stopped
        while (full_seconds > 0 or full_seconds2 > 0) and not self.stop_loop:
            if not self.paused: # Countdown while loop is not paused
                if self.activetimer:
                    if full_seconds > 0:
                        full_seconds -= 1 # Take away 1 second
                        minutes, seconds = divmod(full_seconds, 60)
                        hours, minutes = divmod(minutes, 60)
                        self.time_label.config(text=f"W: {hours:02d}:{minutes:02d}:{seconds:02d}") # Reformat time labels
                        self.update_warning_labels(self.w_warning_label, full_seconds) # Update warning labels
                else:
                    if full_seconds2 > 0:
                        full_seconds2 -= 1
                        minutes2, seconds2 = divmod(full_seconds2, 60)
                        hours2, minutes2 = divmod(minutes2, 60)
                        self.time_label2.config(text=f"B: {hours2:02d}:{minutes2:02d}:{seconds2:02d}")
                        self.update_warning_labels(self.b_warning_label, full_seconds2)
                        self.game_clock_frame.update()
                time.sleep(1)
                self.move_start_time = time.time()
                self.w_total_time = (int(self.w_starttime) - full_seconds)
                self.b_total_time = (int(self.b_starttime) - full_seconds2)

            # if full_seconds or full_seconds2 == 0:
            #     messagebox.showinfo("Countdown Timer", "Time's UP!")

        # Display a message when the time is up
        if not self.stop_loop:
            print('Time is up')
            messagebox.showinfo("Countdown Timer", "Time's UP!")

    # Clock: FUNCTION: Pause the timer
    def pause_timer(self):
        self.paused = not self.paused

    # Clock: FUNCTION: Stop the timer
    def stop(self):
        self.stop_loop = True
        self.game_stats.update_avg_time(self.w_total_time, self.b_total_time)  # Pass the total times
        self.time_label.config(text="W: 00:00:00") # Rest clocks to neutral display
        self.time_label2.config(text="B: 00:00:00") # Rest clocks to neutral display
        self.move_start_time = time.time()

    # Clock: FUNCTION: Switch the timer
    def switch(self, event=None):
        print('switch called')
        self.activetimer = not self.activetimer
        if self.activetimer:
            self.game_stats.update_move("black") # updating the game_stats class
        else:
            self.game_stats.update_move("white")

"""Class used for gamestats that calculate metrics"""
class GameStats:
    """ Initialize the game statistics frame and counter
    Private attributes used to encapsulate data within class"""
    def __init__(self, game_stats_frame): # Initialize the game statistics frame and counters
        # Dictionary that counts captures pieces for both white and black.
        self.w_captures = {'pawn': 0, 'minor': 0, 'rook': 0, 'queen': 0}
        self.b_captures = {'pawn': 0, 'minor': 0, 'rook': 0,'queen': 0}

        # GUI elements to display statistics
        self.game_stats_frame = game_stats_frame
        self.games_played = 0
        # Moves and captures
        self.w_moves_number = 0
        self.b_moves_number = 0
        self.w_moves_pawn_capture = 0
        self.b_moves_pawn_capture = 0
        self.w_moves_minor_capture = 0
        self.b_moves_minor_capture = 0
        self.w_moves_rook_capture = 0
        self.b_moves_rook_capture = 0
        self.w_moves_queen_capture = 0
        self.b_moves_queen_capture = 0
        # Variables used to cacluate average time per move
        self.w_avg_time = 0
        self.b_avg_time = 0
        self.w_total_time = 0
        self.b_total_time = 0
        self.w_avg_time_per_move_float = 0.0
        self.b_avg_time_per_move_float = 0.0
        self.init_labels()
    """capture_piece function which updates the dictionary and calculates moves until a piece is captured """
    def capture_piece(self, color, piece_type):
        color_captures = self.w_captures if color == "white" else self.b_captures
        color_moves_number = self.w_moves_number if color == "white" else self.b_moves_number
        color_moves_label = {
            'pawn': self.w_moves_pawn_label if color == "white" else self.b_moves_pawn_label,
            'minor': self.w_moves_minor_label if color == "white" else self.b_moves_minor_label,
            'rook': self.w_moves_rook_label if color == "white" else self.b_moves_rook_label,
            'queen': self.w_moves_queen_label if color == "white" else self.b_moves_queen_label,
        }

        color_captures[piece_type] += 1
        moves_until_capture = color_moves_number
        if piece_type in color_moves_label:
            color_moves_label[piece_type].config(text=str(moves_until_capture))

    def init_labels(self): # Initialize labels for displaying statistics on the frame
        self.w_moves_label = Label(self.game_stats_frame, font=("Helvetica, 30"), text=self.w_moves_number)
        self.w_moves_label.place(x=800, y=400)
        self.b_moves_label = Label(self.game_stats_frame, font=("Helvetica, 30"), text=self.b_moves_number)
        self.b_moves_label.place(x=1150, y=400)
        self.w_time_label = Label(self.game_stats_frame, font=("Helvetica, 30"), text='00:00:00')
        self.w_time_label.place(x=800, y=485)
        self.b_time_label = Label(self.game_stats_frame, font=("Helvetica, 30"), text='00:00:00')
        self.b_time_label.place(x=1150, y=485)
        self.w_moves_pawn_label = Label(game_stats_frame, font=('Helvetica', 30), text=self.w_moves_pawn_capture)
        self.b_moves_pawn_label = Label(game_stats_frame, font=('Helvetica', 30), text=self.b_moves_pawn_capture)
        self.w_moves_minor_label = Label(game_stats_frame, font=('Helvetica', 30), text=self.w_moves_minor_capture)
        self.b_moves_minor_label = Label(game_stats_frame, font=('Helvetica', 30), text=self.b_moves_minor_capture)
        self.w_moves_rook_label = Label(game_stats_frame, font=('Helvetica', 30), text=self.w_moves_rook_capture)
        self.b_moves_rook_label = Label(game_stats_frame, font=('Helvetica', 30), text=self.b_moves_rook_capture)
        self.w_moves_queen_label = Label(game_stats_frame, font=('Helvetica', 30), text=self.w_moves_queen_capture)
        self.b_moves_queen_label = Label(game_stats_frame, font=('Helvetica', 30), text=self.b_moves_queen_capture)
        self.w_moves_pawn_label.place(x=800, y=550)
        self.b_moves_pawn_label.place(x=1150, y=550)
        self.w_moves_minor_label.place(x=800, y=630)
        self.b_moves_minor_label.place(x=1150, y=630)
        self.w_moves_rook_label.place(x=800, y=700)
        self.b_moves_rook_label.place(x=1150, y=700)
        self.w_moves_queen_label.place(x=800, y=750)
        self.b_moves_queen_label.place(x=1150, y=750)
    # CLASS: FUNCTION: Update move count based on the color
    def update_move(self, color): # Update move count based on the color
        if color == "black":
            self.w_moves_number += 1
            self.w_moves_label.config(text=self.w_moves_number)
        elif color == "white":
            self.b_moves_number += 1
            self.b_moves_label.config(text=self.b_moves_number)
    # CLASS: FUNCTION: # Update average time labels for both players
    def update_avg_time(self, w_total_time, b_total_time):
        # Calculate average time for white
        if self.w_moves_number != 0:  # To prevent division by zero
            self.w_avg_time = w_total_time / self.w_moves_number
            mins, remainder = divmod(self.w_avg_time, 60)
            secs, millis = divmod(remainder, 1)
            millis = int(millis * 1000)  # Convert fractional seconds to milliseconds

            # Display on the frame
            self.w_time_label.config(text=f"{int(mins):02d}:{int(secs):02d}.{millis:03d}")

            # Calculate and store the float representation
            self.w_avg_time_per_move_float = mins * 60 + secs + millis / 1000

        # Calculate average time for black
        if self.b_moves_number != 0:  # To prevent division by zero
            self.b_avg_time = b_total_time / self.b_moves_number
            mins, remainder = divmod(self.b_avg_time, 60)
            secs, millis = divmod(remainder, 1)
            millis = int(millis * 1000)  # Convert fractional seconds to milliseconds

            # Display on the frame
            self.b_time_label.config(text=f"{int(mins):02d}:{int(secs):02d}.{millis:03d}")

            # Calculate and store the float representation
            self.b_avg_time_per_move_float = mins * 60 + secs + millis / 1000 # Update average time labels for both players
    # CLASS: FUNCTION: Placeholder for updating average time per move
    def update_avg_time_per_move(self):
        pass


next_gp_button = Button(game_player_frame, text="NEXT", bg='green', font=("Bookman", 22), width=3, height=1, command=lambda: [collect_user_info(), raise_frame(game_clock_frame)])
next_gp_button.place(x=1365, y=820)

# DATABASE: USERS TABLE: Define the table users if it doesn't exist
c.execute("""CREATE TABLE IF NOT EXISTS users (
    user_id integer PRIMARY KEY,
    first_name text, 
    last_name text,
    games_played integer,
    win_percent integer,
    loss_percent integer,
    draw_percent integer,
    avg_moves_per_game float,
    avg_time_per_move float
)""")
conn.commit()

# FUNCTION: Show player statistics and win/loss/draw
def reveal_player_statistics():
    print('REVEAL STATS!')
    try:
        # Try to convert the user input to an integer
        user_id = int(stats_id_entry.get())
    except ValueError:
        # If the conversion fails, display an error message and return
        print("Invalid user ID. Please enter a valid integer.")
        return

    # Fetch player statistics from the database for the specified user ID
    c.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    player_data = c.fetchone()
    if player_data:
        # Update labels with information from the database
        label_user_id.config(text=f"User ID: {player_data[0]}")
        label_first_name.config(text=f"First Name: {player_data[1]}")
        label_last_name.config(text=f"Last Name: {player_data[2]}")
        label_games_played.config(text=f"Games Played: {player_data[3]}")
        label_win_percent.config(text=f"Win Number: {player_data[4]}")
        label_loss_percent.config(text=f"Loss Number: {player_data[5]}")
        label_draw_percent.config(text=f"Draw Number: {player_data[6]}")
        label_avg_moves.config(text=f"Avg Moves per Game: {player_data[7]}")
        label_avg_time.config(text=f"Avg Time per Move: {player_data[8]}")
    else:
        print(f"No user found with ID {user_id}")
        label_user_id.config(text=f"No user found with ID {user_id}")

# PLAYER STATS: Frames and Widgets
button_show_stats = Button(player_info_frame, text="Show Statistics", font=('Bookman', 20), command=lambda: [reveal_player_statistics(), show_player_statistics()])
button_show_stats.place(x=500, y=200)
label_user_id = Label(player_info_frame, text="User ID: ", font=('Bookman', 20), bg='grey')
label_first_name = Label(player_info_frame, text="First Name: ", font=('Bookman', 20), bg='grey')
label_last_name = Label(player_info_frame, text="Last Name: ", font=('Bookman', 20), bg='grey')
label_games_played = Label(player_info_frame, text="Games Played: ", font=('Bookman', 20), bg='grey')
label_win_percent = Label(player_info_frame, text="Win Percentage: ", font=('Bookman', 20), bg='grey')
label_loss_percent = Label(player_info_frame, text="Loss Percentage: ", font=('Bookman', 20), bg='grey')
label_draw_percent = Label(player_info_frame, text="Draw Percentage: ", font=('Bookman', 20), bg='grey')
label_avg_moves = Label(player_info_frame, text="Avg Moves per Game: ", font=('Bookman', 20), bg='grey')
label_avg_time = Label(player_info_frame, text="Avg Time per Move: ", font=('Bookman', 20), bg='grey')
label_user_id.place(x=10, y=10)
label_first_name.place(x=10, y=50)
label_last_name.place(x=10, y=90)
label_games_played.place(x=10, y=130)
label_win_percent.place(x=10, y=170)
label_loss_percent.place(x=10, y=210)
label_draw_percent.place(x=10, y=250)
label_avg_moves.place(x=10, y=290)
label_avg_time.place(x=10, y=330)


# FUNCTION: Generates next User ID
def generate_next_user_id():
    c.execute("SELECT MAX(user_id) FROM users")
    max_id = c.fetchone()[0]
    if max_id is None:
        return 0
    return max_id + 1


def print_users():
    c.execute("SELECT * FROM users")
    rows = c.fetchall()
    for row in rows:
        print(row)
def enter_user():
    if len(first_name_entry.get()) == 0:
        reminder_label.config(text="Please add a first name")
    elif len(last_name_entry.get()) == 0:
        reminder_label.config(text="Please add a last name")
    else:
        user_id = generate_next_user_id()
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        games_played = 0
        win_percent = 0
        loss_percent = 0
        draw_percent = 0
        avg_moves_per_game = 0.0
        avg_time_per_move = 0.0

        c.execute("""INSERT INTO users (user_id, first_name, last_name, 
        games_played, win_percent, loss_percent, draw_percent, avg_moves_per_game, 
        avg_time_per_move) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""", (
        user_id, first_name, last_name, games_played, win_percent, loss_percent,
        draw_percent, avg_moves_per_game, avg_time_per_move))

        conn.commit()  # Commit the changes to the database
        success_message = f"User successfully added! User ID is {user_id}"
        reminder_label.config(text=success_message)
        next_np_button.config(state=NORMAL)
        print_users()

enter_button.config(command=enter_user)
from tkinter import messagebox

"""User_stats dictionary containing all user statistics """
user_stats = {
    'games_played1': 0,
    'win_percent1': 0,
    'loss_percent1': 0,
    'draw_percent1': 0,
    'avg_moves_per_game1': 0,
    'avg_time_per_move1': 0.0,  # Assuming it's a float
    'user_id1': None,  # Initialize to an appropriate default value
    'games_played2': 0,
    'win_percent2': 0,
    'loss_percent2': 0,
    'draw_percent2': 0,
    'avg_moves_per_game2': 0,
    'avg_time_per_move2': 0.0,  # Assuming it's a float
    'user_id2': None  # Initialize to an appropriate default value
}
def retrieve_user_statistics(user_id1, user_id2):
    global user_stats
    c.execute("SELECT games_played, avg_moves_per_game FROM users WHERE user_id = ?", (user_id1,))
    user_info1 = c.fetchone()
    c.execute("SELECT games_played, avg_moves_per_game FROM users WHERE user_id = ?", (user_id2,))
    user_info2 = c.fetchone()
    # Update statistics based on game_stats for user 1
    user_stats['games_played1'] += 1
    user_stats['avg_moves_per_game1'] = int(((user_stats['avg_moves_per_game1'] * (
                user_stats['games_played1'] - 1) + game_stats.w_moves_number) / user_stats['games_played1']))
    # Update statistics based on game_stats for user 2
    user_stats['games_played2'] += 1
    user_stats['avg_moves_per_game2'] = int(((user_stats['avg_moves_per_game2'] * (
                user_stats['games_played2'] - 1) + game_stats.b_moves_number) / user_stats['games_played2']))
def user_statistics_update():
    global user_stats
    print('user-statistics-update called')
    # Calculate average time per move in GameStats
    game_stats.update_avg_time_per_move()
    # Update the db with the new stats for user 1
    c.execute("UPDATE users SET games_played = ?, avg_moves_per_game = ?, avg_time_per_move = ? WHERE user_id = ?",
              (user_stats['games_played1'], user_stats['avg_moves_per_game1'],
               game_stats.w_avg_time_per_move_float, user_stats['user_id1']))

    # Update the db with the new stats for user 2
    c.execute("UPDATE users SET games_played = ?, avg_moves_per_game = ?, avg_time_per_move = ? WHERE user_id = ?",
              (user_stats['games_played2'], user_stats['avg_moves_per_game2'],
               game_stats.b_avg_time_per_move_float, user_stats['user_id2']))
    conn.commit()
    # Show a success message
    messagebox.showinfo("Success", "User statistics updated successfully!")
def collect_user_info():
    white_player_id = id_entry_white.get()
    black_player_id = id_entry_black.get()
    user_stats['user_id1'] = white_player_id
    user_stats['user_id2'] = black_player_id
    print(white_player_id)
    print(black_player_id)
    return white_player_id, black_player_id
game_end_frame = Frame(root, bg='grey', width=1440, height=900)
game_end_frame.place(x=0,y=0)
game_end_label = Label(game_end_frame, text="End of Game", font=('Bookman', 80))
game_end_label.place(x=485, y=20)
win_var = StringVar()
client_win_checkmate = Radiobutton(game_end_frame, text="Win by Checkmate", font=("Bookman", 32), variable=win_var, value="Checkmate Win", width=30, height=4)
client_win_checkmate.place(x=80, y=200)
client_win_timeout = Radiobutton(game_end_frame, text="Win by Timeout", font=("Bookman", 32), variable=win_var, value="Timeout Win", width=30, height=4)
client_win_timeout.place(x=80, y=400)
client_win_resign = Radiobutton(game_end_frame, text="Win by Resignation", font=("Bookman", 32), variable=win_var, value="Resign Win", width=30, height=4)
client_win_resign.place(x=80, y=600)
lose_var = StringVar()
client_lose_checkmate = Radiobutton(game_end_frame, text="Lose by Checkmate", font=("Bookman", 32), variable=lose_var, value="Checkmate Loss", width=30, height=4)
client_lose_checkmate.place(x=760, y=200)
client_lose_timeout = Radiobutton(game_end_frame, text="Lose by Timeout", font=("Bookman", 32), variable=lose_var, value="Timeout Loss", width=30, height=4)
client_lose_timeout.place(x=760, y=400)
client_lose_resign = Radiobutton(game_end_frame, text="Lose by Resignation", font=("Bookman", 32),variable=lose_var, value="Resign Loss",  width=30, height=4)
client_lose_resign.place(x=760, y=600)
draw_var = StringVar()
client_draw = Radiobutton(game_end_frame, text="Draw", font=("Bookman", 32), width=20, height=2, variable=draw_var, value="Draw")
client_draw.place(x=560, y=770)
enter_ge_button = Button(game_end_frame, text="ENTER ", bg='green', font=("Bookman", 22), width=3, height=1, command=lambda: user_add_game())
enter_ge_button.place(x=1385, y=820)
next_ge_button = Button(game_end_frame, text="NEXT", bg='green', font=("Bookman", 22), width=3, height=1, command=lambda: raise_frame(game_stats_frame))
next_ge_button.place(x=1365, y=820)
home_ge_button = Button(game_end_frame, text="HOME", bg='grey', font=("Bookman", 22), width=3, height=1, command=lambda: raise_frame(home_frame))
home_ge_button.place(x=0, y=820)

def update_user_outcome(win_var, lose_var, draw_var):
    user_id1 = user_stats['user_id1']  # Assuming user_id1 is the relevant user's ID
    user_id2 = user_stats['user_id2']  # Assuming user_id1 is the relevant user's ID

    if win_var is not None:
        c.execute("UPDATE users SET win_percent = win_percent + 1 WHERE user_id = ?", (user_id1,))
        c.execute("UPDATE users SET loss_percent = loss_percent + 1 WHERE user_id = ?", (user_id2,))
    elif lose_var is not None:
        c.execute("UPDATE users SET loss_percent = loss_percent + 1 WHERE user_id = ?", (user_id1,))
        c.execute("UPDATE users SET win_percent = win_percent + 1 WHERE user_id = ?", (user_id2,))
    elif draw_var is not None:
        c.execute("UPDATE users SET draw_percent = draw_percent + 1 WHERE user_id = ?", (user_id1,))
        c.execute("UPDATE users SET draw_percent = draw_percent + 1 WHERE user_id = ?", (user_id2,))

    # Commit the changes to the database
    conn.commit()
# When calling the function, pass all three variables
next_gs_button = Button(game_stats_frame, text="ENTER", bg='green', font=("Bookman", 22), width=3, height=1, command=lambda: [update_user_outcome(win_var.get(), lose_var.get(), draw_var.get()), user_statistics_update(), print_users()])
next_gs_button.place(x=1355, y=820)
next_gc_button = Button(game_clock_frame, text="NEXT", bg='green', font=("Bookman", 22), width=3, height=1, command=lambda: [raise_frame(game_end_frame), retrieve_user_statistics(id_entry_white.get(), id_entry_black.get())])
next_gc_button.place(x=1365, y=820)
home_gc_button = Button(game_clock_frame, text="HOME", bg='blue', font=("Bookman", 22), width=3, height=1, command=lambda: raise_frame(home_frame))
home_gc_button.place(x=0, y=820)

c.execute("""
CREATE TABLE IF NOT EXISTS game_log (
    user_id integer,
    moves integer,
    time_per_move date,
    moves_till_pawn integer,
    moves_till_minor integer,
    moves_till_rook integer,
    moves_till_queen integer,
    FOREIGN KEY(user_id) REFERENCES users(user_id)
)
""")

def print_enter_game_stats():
    c.execute("SELECT * FROM game_log")
    rows = c.fetchall()
    for row in rows:
        print(row)

# Create the clock object, passing the game_stats object as an argument
game_stats = GameStats(game_stats_frame)
clock = Clock(game_clock_frame, game_stats)

user_id = id_entry_white.get()
print(user_id)
# my_database.update_avg_moves_per_game(user_id)

game_clock_frame.focus_set()

home_frame.tkraise()
root.update()
root.mainloop()



