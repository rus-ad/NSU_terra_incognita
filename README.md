# Labyrinth

**Before starting the game, you need to run on the command line:**
1. git clone https://github.com/rus-ad/terra_incognita.git && cd terra_incognita
2. python -m venv venv
3. venv\Scripts\activate.bat
4. pip install -r requirements.txt
5. python main.py
6. start 14 14

* Implement the "Labyrinth" game (aka "Terra Incognita").
  - [Labyrinth (Wiki)](https://en.wikipedia.org/wiki/Labyrinth_(paper-and-pencil_game))
  - [Terra Incognita](https://www.thegamecrafter.com/games/terra-incognita)

* Design the game using:
  - Interfaces (OOP-like)
  - Inversion of Control
  - Dependency Injection
  - Proper layering
  - Proper project structure
  - Diagrams of classes and interaction between classes

* Maze Objects:
  - River - a player getting into the river moves to the mouth of the river
  - Wall - the player cannot go to this cell
  - Cell - some free space
  - Treasure - the player cannot leave the maze without treasure, the treasure is replaced by an empty cell
  - Exit - exit from the maze, available in the presence of treasure
  
* Commands for moving in the maze:
  - Left - the player takes a step to the left
  - Right - the player takes a step to the right
  - Up - the player takes a step back
  - Down - the player takes a step forward
  
* High Level Commands:
  - Start - create a maze, takes two arguments length and width. The picture of the raw version of the labyrinth consisting of walls and free space is saved.
  - Save - saves the session in pickle in folder save
  - Load - downloads the selected game from the list
  - Exit - ends the game without saving
