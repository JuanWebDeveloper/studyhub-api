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
uvicorn app.main:api_app --reload
```

## Virtual Environment

A virtual environment is a self-contained directory that contains a Python installation for a particular version of Python, plus a number of additional packages. It allows you to work on a Python project without affecting the system Python installation.

StudyHub comes with a pre-configured virtual environment located in the `venv` directory. If you haven't activated the virtual environment yet, you can do so by running:

```bash
source venv/bin/activate
```

If the virtual environment is not set up, you can set it up by running the following commands:

```bash
python -m venv venv
source venv/bin/activate
```

Once the virtual environment is activated, you can install the project dependencies using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

Before running the application, you need to create a `.env` file at the root of the project to store environment variables. This file should contain the following variable:

```properties
# Frontend server URL in the development environment
DEV_FRONTEND_URL=your_frontend_host
```

Replace `your_frontend_host` with the URL of the host you are using for the frontend.

This `.env` file is used to store sensitive information that should not be publicly exposed, such as API keys, passwords, etc. Therefore, this file is included in the `.gitignore` file to prevent it from being accidentally uploaded to public repositories.

Remember to activate the virtual environment and set up the `.env` file before running the application.

Once the `.env` file is set up with the correct frontend host, you can run the application using the following command:

```bash
uvicorn main:api_app --reload
```

This command starts the application and enables live reloading, which means the application will automatically update as you make changes to the code.
