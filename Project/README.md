
# Caverns of the Golden Isle Game Documentation

## Overview

"Caverns of the Golden Isle" is a text-based adventure game developed in Python. In this game, players embark on a quest as a pirate exploring a series of interconnected locations on a mysterious island in search of treasure.



## Dependencies

This game requires Python 3.6 or later. There are no external dependencies or libraries required to run the game.

## Project Structure

The project consists of several Python modules:

- `game.py`: The main game loop that integrates all other components.
- `backpack.py`: Defines the `Backpack` class, handling the player's inventory.
- `item.py`: Defines the `Item` class, representing items within the game.
- `room.py`: Defines the `Room` class, representing individual rooms or locations.
- `text_ui.py`: Defines the `TextUI` class, managing user input and output.
- `world.py`: Defines the `World` class, setting up the game world and rooms.
- `test_backpack.py`: Unit tests for the `Backpack` class.
- `test_game.py`: Unit tests for the game logic.
- `test_room.py`: Unit tests for the `Room` class.

## Code Explanation

### `Backpack` Class

- Manages inventory with methods to add and remove items.
- Keeps track of the current weight and ensures it does not exceed capacity.

### `Item` Class

- Represents an item with a name, description, and weight.
- Used by the `Backpack` and `Room` classes to manage items.

### `Room` Class

- Represents a location in the game with a description and potential items.
- Stores exits to other rooms allowing player navigation.

### `TextUI` Class

- Handles all text-based interactions with the player.
- Outputs information and retrieves input commands from the player.

### `World` Class

- Initializes and links all rooms in the game.
- Acts as the access point for retrieving specific rooms.

### `Game` Class

- Contains the game loop and processes player commands.
- Manages the current state, including the player's current room and inventory.

## Running the Game

To run the game, navigate to the project directory in the terminal and execute:

\```bash
python game.py
\```

Follow the on-screen instructions to play the game.

## Testing

Unit tests are provided to ensure the reliability of the game components. To run the tests, execute the following command in the project directory:

\```bash
python -m unittest
\```

