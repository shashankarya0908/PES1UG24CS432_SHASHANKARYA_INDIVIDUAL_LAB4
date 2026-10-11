# Target Shooting Lab

This project implements a simple target-shooting game in Python using Pygame. The lab exercises click hit detection, moving targets, combo-based scoring, and a timed round system.

## Prerequisites

- Python 3.10 or newer
- Pygame
- pytest (for running the included tests)

## Setup

```bash
cd target-shooting
python -m pip install -r requirements.txt
```

## Run the game

```bash
cd target-shooting
python main.py
```

## Run tests

```bash
cd target-shooting
pytest -q
```

## Gameplay

- Left-click inside a visible target to score points.
- Consecutive hits increase the combo multiplier.
- Misses reset the combo.
- A 30 second round ends automatically and shows the final score.
- Press `R` after time expires to restart the round.
