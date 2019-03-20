# 4-in-a-row
An adaptation of the famed board game Connect-4

## Index
- [About the game](https://github.com/manacute/Runtime-Terror-C4/blob/master/README.md#about-the-game)
- [Demo](https://github.com/manacute/Runtime-Terror-C4/blob/master/README.md#demo)
	- [Screenshots](https://github.com/manacute/Runtime-Terror-C4/blob/master/README.md#screenshots)
- [Game Features](https://github.com/manacute/Runtime-Terror-C4/blob/master/README.md#game-features)
	- [Controls](https://github.com/manacute/Runtime-Terror-C4/blob/master/README.md#controls)
- [Installation](https://github.com/manacute/Runtime-Terror-C4/blob/master/README.md#installation)
	- [For Windows](https://github.com/manacute/Runtime-Terror-C4/blob/master/README.md#for-windows)
	- [For MAC OS X](https://github.com/manacute/Runtime-Terror-C4/blob/master/README.md#for-mac-os-x)
- [Contributing](https://github.com/manacute/Runtime-Terror-C4/blob/master/README.md#contributing)
	- [Contributors](https://github.com/manacute/Runtime-Terror-C4/blob/master/README.md#contributors)
	- [To-do](https://github.com/manacute/Runtime-Terror-C4/blob/master/README.md#to-do)
- [License](https://github.com/manacute/Runtime-Terror-C4/blob/master/README.md#license)

## About the game
4-in-a-row is a game played on a board with 7 columns and 6 rows of slots, where two players take turns placing coloured tokens into the board. The first player to get at least 4 consecutive tokens of their colour in a row wins the game.

A four-in-a-row can be made horizontally, vertically, or diagonally, and do not wrap around the edges of the board. Tokens are dropped down a column onto the board, and can stack on top of each other. If a column has all 6 slots filled, you cannot place another token on top. The game ends if one of the players is able to make a four-in-a-row or the entire board gets filled (resulting in a stalemate).

## Demo
### Screenshots
![Main Menu](https://user-images.githubusercontent.com/47199055/54650981-2ac36680-4a87-11e9-92e1-a6bf399dcb3c.PNG)
![Help Menu](https://user-images.githubusercontent.com/47199055/54650984-2c8d2a00-4a87-11e9-8f3c-a41f28b22fa3.PNG)
![New Game](https://user-images.githubusercontent.com/47199055/54682643-e1eeca80-4ae5-11e9-87ee-6a297da0bc95.PNG)
![Mid Game](https://user-images.githubusercontent.com/47199055/54682646-e2876100-4ae5-11e9-8cda-35d313580333.PNG)
![Winning Game](https://user-images.githubusercontent.com/47199055/54682649-e4e9bb00-4ae5-11e9-9989-d1f5cc5a7eb6.PNG)
![Stalemate](https://user-images.githubusercontent.com/47199055/54682651-e5825180-4ae5-11e9-806c-db24d395d268.PNG)

## Game Features
- Custom Sounds for placing counter, winning, stalemate and reverting a move
- Undo ability to revert a move

### Controls
Use the `mouse` to navigate the game interface and play the game.

## Installation
To play 4-in-a-row, you must have Python and Pygame installed.

### For Windows
Download the folder of the repo (all files must be present). Once that is
done open the folder and double-click the 'main.py' file to play.
Happy Playing!

### For Mac OS X
Download the folder, open main.py and run the module in python.

## Contributing
### Contributors
- Amit Ohm
- Maxmilian Huang
- Kim Thien Le
- Peter Del Fatti
- Syeda Sani-e-Zehra

### To-do
- [x] Create Main Menu
- [x] Create Help Menu
- [x] Create Undo Feature
- [x] Add Sound Effects to dropping and removing tokens
- [x] Add Sound Effects for winning game and stalemate
- [ ] Create Player vs computer mode (Virtual player)
- [ ] Add backgrund music
- [ ] Add option to reset game mid-play
- [ ] Add option to go to menu mid-play


## License
Copyright 2019 Peter Del Fatti, Maximilian Huang, Kim Thien Le, Amit Ohm, Syeda Sani-e-Zehra

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
