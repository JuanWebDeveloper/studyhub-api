# StudyHub API

StudyHub API is the API component of the StudyHub platform, designed to help students organize and manage their study materials effectively. It provides features such as note-taking, task tracking, and resource management, all in one centralized location.

## Table of Contents

1. [Project Structure](#project-structure)
2. [Installation](#installation)
3. [Virtual Environment](#virtual-environment)

## Project Structure

StudyHub API follows a structured layout to organize its components effectively:

- `database`: Contains database-related files.
- `routes`: Contains the API route handlers.
- `schemas`: Contains data schema definitions.
- `controllers`: Contains controllers for handling business logic.
- `middlewares`: Contains middleware functions.
- `utils`: Contains utility functions.
- `tests`: Contains test cases for the application.

## Installation

To run StudyHub API locally, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/JuanWebDeveloper/studyhub-api.git
cd StudyHub
```

2. Activate the virtual environment:

```bash
source venv/bin/activate
```

3. Run the application:

```bash
uvicorn app.main:app --reload
```

## Virtual Environment

A virtual environment is a self-contained directory that contains a Python installation for a particular version of Python, plus a number of additional packages. It allows you to work on a Python project without affecting the system Python installation.

StudyHub comes with a pre-configured virtual environment located in the `venv` directory. If you haven't activated the virtual environment yet, you can do so by running:

```bash
source venv/bin/activate
```

If the virtual environment is not configured, you can set it up by running the following commands:

```bash
python -m venv venv
source venv/bin/activate
```

Once the virtual environment is activated, you can install the project's dependencies using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

Remember to activate the virtual environment before running the application.
