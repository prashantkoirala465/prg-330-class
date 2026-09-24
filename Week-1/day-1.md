# PRG 330 — Day 1: Introduction to Python & Environment Setup

## Class Overview

**Course:** PRG 330
**Day:** 1
**Topic:** Introduction to Python and Development Environment Setup

## Topics Covered

### 1. Introduction to Python

Python is a high-level, general-purpose programming language known for its simple and readable syntax. It is widely used in:

* Web development
* Data science
* Artificial intelligence and machine learning
* Automation and scripting
* Software development
* Scientific computing

We discussed the basic structure and syntax of Python programs and how Python code is executed.

### 2. Basic Python Concepts

We introduced some fundamental Python concepts, including:

* `print()` function
* Basic Python syntax
* Strings
* Numbers
* Variables
* Basic operators
* Simple Python programs

Example:

```python
name = "Prashant"
age = 23

print(name)
print(age)
```

We also practiced using `print()` to display multiple values:

```python
print("Apple", "Banana", "Cherry")
```

### 3. Anaconda Installation

We installed **Anaconda**, a Python distribution commonly used for programming, data science, and scientific computing.

Anaconda provides:

* Python
* Package management through Conda
* Environment management
* Jupyter Notebook
* Common Python libraries and development tools

### 4. Virtual Environment Setup

We learned about virtual environments and why they are useful.

A virtual environment provides an isolated Python environment for a project. This allows different projects to use different Python versions and package versions without conflicts.

We created and configured a virtual environment for the PRG 330 course.

Basic workflow:

```bash
python -m venv .venv
```

Activate the environment on macOS/Linux:

```bash
source .venv/bin/activate
```

After activation, packages can be installed specifically inside the project's environment.

### 5. Package Management

We were introduced to installing Python packages using `pip`.

Example:

```bash
python -m pip install package_name
```

We also learned that project dependencies can be stored in a `requirements.txt` file and installed using:

```bash
python -m pip install -r requirements.txt
```

### 6. Jupyter Notebook

We also set up the environment required to work with Jupyter Notebook for Python programming and practical exercises.

Jupyter Notebook allows Python code to be written and executed interactively in separate cells, making it useful for learning, experimentation, and data analysis.

## Key Takeaways

By the end of Day 1, we covered:

* What Python is and where it is used
* Basic Python syntax and the `print()` function
* Variables and basic data types
* Installation and use of Anaconda
* The purpose of virtual environments
* Creating and activating a Python virtual environment
* Installing packages with `pip`
* Setting up Jupyter Notebook for Python development

## Practical Work

During the class, we:

1. Installed Anaconda.
2. Set up the Python development environment.
3. Created a virtual environment for PRG 330.
4. Activated the virtual environment.
5. Installed the required Python packages.
6. Ran basic Python programs.
7. Set up Jupyter Notebook for future practical exercises.

## Day 1 Summary

Day 1 focused on establishing the Python development environment and introducing the fundamentals of Python programming. The main objective was to ensure that the required tools and environment were properly configured before moving into more advanced Python programming concepts in subsequent classes.
