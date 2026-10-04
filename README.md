# PRG 330

Coursework and notes for PRG 330 — a Python programming class. Each week gets its own folder with class notes, notebooks, and any setup needed for that week's exercises.

## Structure

```
PRG-330/
├── Week-1/
│   ├── day-1.md                 # Notes: intro to Python, Anaconda, venv, pip, Jupyter
│   ├── day-2.ipynb              # Notebook: first Python exercises (variables, loops, f-strings)
│   ├── Week-1-Assignment.ipynb  # Week 1 assignment notebook
│   └── requirements.txt         # Python dependencies for this week
├── Week-2/
│   └── Assignments/
│       ├── week-2-question-1.ipynb  # Attendance percentage calculator
│       └── week-2-question-2.ipynb  # Tuition and scholarship calculator
├── Week-3/
│   ├── week-3-day-1-and-2.ipynb # Data handling and Python scripting
│   ├── main.py, grade.py, etc.  # Python script modules
│   └── data.ipynb               # Further data exploration
├── Week-4/
│   ├── Classwork/               # Modular programming classwork (loops, conditions, files)
│   └── Assignment/              # Retail sales data analysis with modules
├── Week-5/
│   ├── Classwork/               # Pandas basics: student performance analysis
│   └── Assignment/              # Google Play Store dataset analysis
├── Week-6/
│   ├── Classwork/               # Data visualization and further analysis
│   └── Assignment/              # Advanced data manipulation assignments
└── Final-Project/
    ├── Daraz_Final_Project.ipynb
    └── Daraz_Modular_Final_Project/ # Modularized end-to-end data analysis pipeline
```

More `Week N` folders will be added as the course progresses.

## Week 1

**Day 1** covers environment setup: what Python is, installing Anaconda, creating and activating a virtual environment, installing packages with `pip`, and getting Jupyter Notebook running.

**Day 2** is a hands-on notebook covering basic syntax — `print()`, variables, a multiplication-table loop, and f-strings.

**Week-1-Assignment** is the submitted assignment notebook for the week.

## Week 2

**Assignments** contains two notebooks:

- **Question 1** — reads classes attended out of 16, calculates the attendance percentage and number of missed classes, and reports whether the student can move to the next session.
- **Question 2** — reads tuition, GPA, student type, payment method, and enrollment timing, then computes a combined scholarship/discount and prints the final tuition.

## Week 3

Covers basic Python scripts, control flow, functions, and module imports, organizing code across multiple `.py` files to create larger applications.

## Week 4

Focuses on **Modular Programming**.

- **Classwork** breaks down concepts into separate modules for loops, conditions, functions, and file I/O.
- **Assignment** applies modular programming to generate a sales report from a retail sales dataset.

## Week 5

Focuses on data manipulation with **Pandas**.

- **Classwork** covers cleaning and analyzing a student performance dataset.
- **Assignment** involves a comprehensive EDA (Exploratory Data Analysis) on the Google Play Store dataset, including data cleaning, transformations, and summary aggregations.

## Week 6

Focuses on advanced data handling and visualization techniques.

- **Classwork** and **Assignment** continue exploring dataset processing and generating insights using various Python libraries.

## Final Project

The **Daraz E-commerce Analysis Project** is the culminating work of the course.
It applies an end-to-end data analysis pipeline on Daraz's "Watches Bags Accessories" dataset.
Includes:
- An integrated Jupyter Notebook (`Daraz_Final_Project.ipynb`).
- A **Modularized Version** (`Daraz_Modular_Final_Project/`) dividing the process into separate scripts for variables, loops, conditions, functions, data cleaning, pandas analysis, numpy analysis, visualization, and findings.

## Getting started

From inside a week's folder (e.g. `Week-1`):

```bash
python -m venv .venv
source .venv/bin/activate      # macOS/Linux
python -m pip install -r requirements.txt
jupyter notebook
```

Then open the day's `.ipynb` file in Jupyter.

## Notes

- `.venv`, `.DS_Store`, and `.ipynb_checkpoints` are git-ignored — each week's virtual environment is local and not tracked.
