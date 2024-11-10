The product is a digital chess tool designed to help players integrate the detailed analysis of online chess into their over-the-board (OTB) games. 
It combines a standard chess clock with additional game-tracking features, providing players with both time control and game insights.

Here’s what the product does:

- Time Management: The product functions as a customizable chess clock, displaying each player’s time and automatically switching turns. It offers options to adjust for different game durations and provides low-time warnings, either visually or with sound alerts. The clock’s interface is designed for clarity, using a larger font and bold visuals to make time tracking straightforward, even at a glance.
- Game Tracking: Beyond simply keeping time, the product records important events during the game. It logs each player’s move times, tracks the material status (such as counting pieces captured), and notes key moments, like when certain pieces—queens, major or minor pieces, or pawns—are captured. This allows players to review how the material balance shifted during the game and see when pivotal moves were made.
- Historical Game Records: After each game, the product saves the game details and stores them in a game history log. Players can view past games and analyze data like total time used, move times, and outcomes, helping them see patterns in their play over time.
- Player Analytics and Visual Feedback: The product generates statistics such as win/loss ratios and average time per move, displaying these insights in charts and graphs. Players can quickly understand their performance trends and identify areas for improvement.

Technical Approach:

The product is built using Python, with Tkinter for the user interface, SQLite for data storage, and Matplotlib for visualizing statistics. This combination makes it compatible across platforms (MacOS and Windows) while also being flexible and easy to use.

Description of Scenario

In the fast-paced, dynamic world of competitive chess, where split-second decisions can
make all the difference between victory and defeat, the chess clock remains the ultimate arbiter of
time.
My client is a novice chess player interested in improving her over-the-board chess skills. She
realizes that in order to become a more sophisticated player, she needs to get used to playing with a
chess clock and receive feedback on games. The primary issues are that current digital chess clocks
are “difficult to use”, don’t keep track of past games, and don’t provide feedback or an analysis of
the game.
The current solution my client employs involves using online chess clocks or chess clock
applications. However, the clocks often “don't quite work” due to poor customization and
functionality as well as a lack of “indication or any kind of warning”. The client also plays online
games on Chess.com which gives detailed game feedback, butcher wants to improve her
over-the-board chess skills and has so far not found an application that gives feedback or keeps track
of over-the-board games.
After consulting with the client, it is clear that the current solutions are inadequate due to
various usability issues including learnability, recurring errors and low user-satisfaction.
Additionally, consultations have made it clear that the solution should “mimic online chess”
(Chess.com games). Considering the various factors, it is apparent that the solution must entail a
user-friendly chess clock, a game-tracker and a record of past games and players so that it best suits
my client.

Rationale

The proposed solution would be effective as it would create both a user-friendly chess clock
graphical user interface (GUI) as well as a chess tracker, meeting the clients requirements and
solving the issue. For a start the programming language used would be Python 3 which is justifiable
as it’s a high-level, well known, versatile language that has an extensive library and can be executed
on the “MacOS and Windows” system. The solution would use Tkinter to create the GUI for the
chess clock and tracker. It is the ideal for this because of its cross platform abilities and its wide
range of functions that can be used to make a user-friendly, customizable chess clock and tracker.
SQLite, a commonly used database, would be used to keep track and log players, and game
statistics. It is an optimal DBMS for small-scale databases due to its simplicity, flexibility, efficiency,
and because it's a part of the python library, it has cross platform capabilities. The solution would
use Matplotlib to create and graphs that communicate game statistics such as win/loss percentage
(in a pie-chart) or average time per move per player (bar-graph). Matplotlib is the standard plotting
library for python that contains object oriented API to support various types of graphical
representations that make it ideal for this solution.
Even without considering my proficiency in the programs proposed above, their popularity
and common use means there will be lots of resources available to guide me.
The proposed libraries and toolkits will be optimal for achieving the desired solution but
on a larger scale the libraries and toolkits are all compatible with one another, the programming
language, and the different platforms the user might use.

Success Criteria:

1. The solution must have a functional (as in it records time, switches per player turns, counts
down and stops when a player runs out of time) and customizable two player chess clock
which can be modified for games of different duration
2. The solution must give some sort of warning to the user when they are running low on time
either visually or auditorily or both
3. The solution must use a large, legible font and graphics that are at least 50% larger than the
default graphics and the GUI must take up as much of the screen as possible
4. The solution must have a way to track material status for both players in a game
5. The solution must be able to keep track of the time per move for both players
6. The solution must be able to keep track of key developments in the game including but not
limited to:
a. When a queen vs major piece vs minor piece vs pawn is first captured (the moves
until a capture is first made)
b. When a player has lost or won (either by checkmate, timeout or resignation)
c. When a player has drawn
7. The solution should log and keep track of different players and their past games against
each other
8. The solution must display the information collected above (Success Criteria 5-7) through
graphs, charts or statistics

