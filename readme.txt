3/25/19

Almost fully functional. Currently keeping physical documentation for practice purposes and looking to typing it out.
Collision detection working almost perfectly. Modifying movement for win paths was a little tricky but was a simple solution in hindsight. Doing code cleanups as I go and trying to keep everything as modular as possible. Would like to add statistics eventually, maybe by writing things like spaces moved and wins to spreadsheets with player names and colors. Might be a fun opportunity to learn about structuring data in graphs. All of that would come after GUI, tho. Happy with the progress so far, can't wait to see what else I can do with this. Next readme will be less diary-like and more informative. 

3/23/19

This is my first 'serious' programming project, and it's based off the board game 'Trouble'. I didn't want to put this onto a repository until it was 'complete' (able to play the game without bugs or errors, while input and output are all handled in terminal, i.e. board state being printed rather than 'refreshed'). However, once I made the decision to change the board into an object rather than storing it in a single variable, I had to change quite a bit. I didn't want to scrap and rewrite anything, and I sure as heck didn't want to botch what I had already worked on if I found I took the wrong approach. And it only started to send me into panic when I had multiple copies of the same (mostly) code and keeping track of all of them. Thus, I finally started learning to utilize version control. I didn't know repositories could be private (oof) which this one will remain until it is nearing playability.

I hope to keep working on this project after the initial goal is met. It has taught helped solidified my fundamentals in programming and Python, and has cultivated a dormant passion I forgot I had. I never thought a 4 person, one board, one dice board game would offer so much to think about.

Current goals are, but not limited to:

Insert coordinate check into turn sequence in appropriate places:
	BEFORE moving out a piece from start
	If that space is occupied, select another piece
	After moving a piece in a 'regular' turn (no activated pieces)


Incorporate win paths. Every player has a pivot coordinate (the last space they are able to be sent back to start)
	This coordinate will need to be checked NOT at the end of the turn, but DURING the function that evaluates 		coordinates. (Function in logicboard: will need to be at the end of every iteration in for loop)

Change piece representation (R) into the piece number (1) printed in the color of that piece/player 

Future (big) goals are, but not limited to:
	GUI
	Special or unique game modes
	Cross platform
	Netplay/local play