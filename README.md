# StudyHub API

StudyHub API is the API component of the StudyHub platform, designed to help students organize and manage their study materials effectively. It provides features such as note-taking, task tracking, and resource management, all in one centralized location.

## Table of Contents

1. [Project Structure](#project-structure)
2. [Installation](#installation)
3. [Virtual Environment](#virtual-environment)
4. [Database Configuration](#database-configuration)

## Project Structure

StudyHub API follows a structured layout to organize its components effectively:

- `database`: Contains database-related files.
- `routes`: Contains the API route handlers.
- `schemas`: Contains data schema definitions.
- `controllers`: Contains controllers to manage the operations of the application.
- `middlewares`: Contains middleware functions.
- `utils`: Contains utility functions.

## Installation

To run StudyHub API locally, follow these steps:

### 1. Clone the repository:

```bash
git clone https://github.com/JuanWebDeveloper/studyhub-api.git
cd StudyHub
```

### 2. Perform the following pre-execution configurations for the proper functioning of the API

Before launching the application, it's crucial to verify that the virtual environment is operational and properly configured. Equally important is the setup of the environment variables, which should be stored in a .env file at the root of the project. This file should contain all the necessary variables for the application to function correctly. Lastly, ensure that the database configuration is correctly established. These steps are vital to guarantee the optimal operation and data integrity within the application.

Please follow the subsequent steps to properly configure these components before proceeding with the execution of the application:

1. Ensure that the virtual environment is active. If you're unsure how to do this, refer to the "Virtual Environment" section of this document.

2. Create the .env file at the root of the project and set up the necessary environment variables. This file should contain at least the following variable:

   ```properties
   DEV_FRONTEND_URL=your_frontend_host
   ```

- Replace `your_frontend_host` with the URL of the host you are using for the frontend.

3. Verify that the database configuration is correctly established. If you need help with this, refer to the "Database Configuration" section of this document.

## Did configuration issues arise?

If you encounter problems with the configurations of the virtual environment component and the database component, please refer to the `Virtual Environment` and `Database Configuration` sections of this document.

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

## Database Configuration

StudyHub API uses MongoDB as its database. The connection to the database is configured in the `connection.py` file located in the `database` directory.

In this file, you will find the following lines of code:

```python
mongo_client = AsyncIOMotorClient('your_mongodb_host')
studyhub_database = mongo_client.your_database_name
```

Replace `your_mongodb_host` with the host where your MongoDB is running and `your_database_name` with the name of your MongoDB database.

The application is configured to use a MongoDB collection named `notes` to store the notes. If you want to use a different collection name, you need to go to the `note_controller.py` file located in the `controllers` directory and change the following line:

```python
notes_collection = studyhub_database.notes
```

Replace `notes` with the name of your desired collection.

Once the virtual environment is active, the .env file is configured with the correct frontend host, and the MongoDB database is set up, you can run the application using the following command:

```bash
uvicorn main:api_app --reload
```

This command starts the application and enables live reloading, which means the application will automatically update as you make changes to the code.
