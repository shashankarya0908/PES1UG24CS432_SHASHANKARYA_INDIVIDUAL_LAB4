 #Target Shooting Lab

A Python and Pygame target-shooting game. The lab implementation is complete: targets move and bounce within the play area, accurate circular hit detection is used, hits build a combo score, and each round lasts 30 seconds.

## Completed features

- **Circular hit detection:** A shot hits only when its click position lies inside a target's visible circle, including clicks near its edge.
- **Moving targets:** Targets move at varied speeds and bounce off the play-area boundaries.
- **Combo scoring:** Each hit earns 10 points multiplied by the current combo. Consecutive hits increase the multiplier; a miss resets it.
- **Timed rounds:** The game displays a 30-second countdown, rejects shots after time expires, and displays the final score.
- **Round restart:** Press `R` after the round ends to start over with the score, combo, targets, and timer reset.

## Prerequisites

- Python 3.10 or newer
- Pygame
- pytest (to run the tests)

## Setup

From this directory, install the dependencies:

```bash
python -m pip install -r requirements.txt
```

## Run the game

```bash
python main.py
```

Left-click targets to shoot. When the round ends, press `R` to play again.

## Run tests

```bash
python -m pytest -q
```
