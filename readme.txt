This is a CLI version of the popular board game "Trouble". In Trouble, there are four players (red, blue, green, and yellow) with 4 pieces each. All pieces begin in a "start" position off the board and can only be activated and moved onto the board by one space after rolling a 6. Landing on an opponent's piece sends that piece back to start, and you can't land on your own pieces. All pieces move clockwise around the board until they reach their "pivot point" (one space behind their start space) and from then will move into their home paths. Pieces can move through home as long as their move roll would not put them past their last available coordinate. Once a player gets all four of their pieces into home, they win and the game ends.

Known bugs:
When multiple pieces are in home, determining possible moves has odd behavior. This is possibly caused by collision detection returning a True value when colliding with allied piece, and then passing that to possible moves.

Future goals:
Computer players
Add continuation after someone wins. (Red player wins, but the remaining 3 players want to continue to compete)
GUI
Varied game modes such as 
Netplay
