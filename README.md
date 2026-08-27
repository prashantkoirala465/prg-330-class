# PRG 330

Coursework and notes for PRG 330 — a Python programming class. Each week gets its own folder with class notes, notebooks, and any setup needed for that week's exercises.

## Structure

```
PRG-330/
└── Week 1/
    ├── day-1.md          # Notes: intro to Python, Anaconda, venv, pip, Jupyter
    ├── day-2.ipynb        # Notebook: first Python exercises (variables, loops, f-strings)
    └── requirements.txt    # Python dependencies for this week
```

More `Week N` folders will be added as the course progresses.

## Week 1

**Day 1** covers environment setup: what Python is, installing Anaconda, creating and activating a virtual environment, installing packages with `pip`, and getting Jupyter Notebook running.

**Day 2** is a hands-on notebook covering basic syntax — `print()`, variables, a multiplication-table loop, and f-strings.

## Getting started

From inside a week's folder (e.g. `Week 1`):

```bash
python -m venv .venv
source .venv/bin/activate      # macOS/Linux
python -m pip install -r requirements.txt
jupyter notebook
```

Then open the day's `.ipynb` file in Jupyter.

## Notes

- `.venv`, `.DS_Store`, and `.ipynb_checkpoints` are git-ignored — each week's virtual environment is local and not tracked.
