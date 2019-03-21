# Documentation

## Index
- [Directory Structure](https://github.com/manacute/Runtime-Terror-C4/blob/master/README.md#directory-structure)
- [Classes and Functions](https://github.com/manacute/Runtime-Terror-C4/blob/master/README.md#classes-and-functions)
- [Extending the Game](https://github.com/manacute/Runtime-Terror-C4/blob/master/README.md#extending-the-game)

## Directory Structure


## Classes and Functions
### Main
The file main.py is the base game instance. This handles the game states and transitioning between menus. The fucnction called play is the main gameplay loop. This file can be seen as the setup before the game is running.

### Model
This is a parent class that is inherited my the Model classes. This allows the classes to recieve input. Using this input the functions can draw things to the screen and update the screen.

### BoardModel
This model is how the game interface screen is displayed as well as tracking the board using a 2D array. The function draw() draws the board onto the screen and the pieces are dropped in the corresponding coloumns.

### MenuModel and HelpModel
These are the menus for the game. These classes inherit Model and create the visual representation by drawing things to the screen such as buttons and text.

### Move
This class defines how a user makes a move. It tracks their mouse position and which users turn it is.

### MoveController
This class is what controls the move and whether or not it is executed. There are checks to see if the move is valid, which piece will fall, and if the move will win the game. 

### Button
The file Button.py is what we used in order to create the buttons in the menus. To create a button, create an instance of this class and fill in the needed parameters. The functions within this class let the program know whether the users mouse is over the button.

### Piece
This class is used to fill the array which is the board representation. The class allows the user to check which piece is on which team or if it is an empty piece.


## Extending the Game