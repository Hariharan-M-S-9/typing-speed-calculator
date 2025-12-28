# Typing Speed Game

A simple real-time typing speed test game built with Python and Pygame. Test your typing speed and accuracy by typing the displayed sentences as fast as you can.

## Features

- **Real-time Feedback**: Characters light up blue if correct and red if incorrect.
- **WPM Calculation**: Calculates Words Per Minute accurately upon completion.
- **Random Sentences**: Picks random sentences from a customizable file.
- **Smooth Interface**: Clean, dark-themed UI for comfortable typing.

## Prerequisites

- Python 3.6+
- Pygame

## Installation

1. Ensure you have Python installed.
2. Install the required library:
   ```bash
   pip install pygame
   ```

## How to Run

Run the game using Python:

```bash
python typing.py
```

## How to Play

1. The game will display a target sentence.
2. Type the sentence exactly as shown.
    - **Blue** characters are correct.
    - **Red** characters are incorrect.
3. Use `Backspace` to correct mistakes.
4. When you finish the sentence, your **Time** and **WPM** will be shown.
5. Press **Enter** to play again with a new sentence or **Esc** to quit.

## Customization

You can add your own sentences to the game! Open `sentences.txt` and add new sentences, one per line.

## Project Structure

- `typing.py`: Main game logic and Pygame loop.
- `sentences.txt`: Source file for typing sentences.
