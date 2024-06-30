# NHA Database Management System

The NHA Database Management System is a Python application designed to manage various aspects of projects and operations using a graphical user interface (GUI) built with Tkinter. It utilizes SQL Connector to connect with the NHA database for data storage and management.

## Project Overview

This system facilitates the management of data related to projects, tenders, blacklist, power duties, toll taxes, and remarks within the NHA database. It allows users to perform CRUD operations (Create, Read, Update, Delete) seamlessly through a user-friendly interface.

## Functionality

The system includes modules for:

- **Projects:** Manage project details such as ID, title, status, and deadlines.
- **Tenders:** Handle tender information including ID, description, dates, and status.
- **Blacklist:** Maintain records of blacklisted entities with reasons and effective dates.
- **Power Duties:** Manage duties and responsibilities assigned to personnel or departments.
- **Toll Taxes:** Record toll tax information including locations, rates, and collection dates.
- **Remarks:** Capture and track important notes or comments related to projects and operations.

## System Requirements

### Software Requirements:

- Python 3.x
- Tkinter (included with Python installations)
- MySQL(8.3) Connector/Python

### Hardware Requirements:

- Standard desktop or laptop with sufficient RAM and CPU for running Python applications.

## Installation Instructions

### Install Python:

1. Download and install Python 3.x from [python.org](https://www.python.org/downloads/).

### Install MySQL Server:

1. Download and install MySQL Server from [mysql.com](https://dev.mysql.com/downloads/mysql/) if not already installed.

### Install Required Python Libraries:

1. Open Visual Studio or any preferred Python IDE.

2. Install MySQL Connector/Python:
   ```bash
   pip install mysql-connector-python
   ```

3. Tkinter is usually included with Python installations and may not require separate installation.

### Clone the Repository:

```bash
git https://github.com/maliikhassan/NHA-Databse
```

### Database Setup:

1. Import the database schema and initial data from `database.sql` into your NHA database.

2. Modify Database Configuration:
   - Open `config.py` and update the MySQL database configuration settings:
     ```python
     db_config = {
         'host': 'localhost',
         'user': 'root',
         'password': 'your_password',
         'database': 'nha'
     }
     ```

## Usage Instructions

### Run the Application:

1. Navigate to the project directory in Visual Studio.

2. Start the application:
   ```bash
   python main.py
   ```

### Using the Application:

1. The application features a main page with buttons for different modules:
   - Projects
   - Tenders
   - Blacklist
   - Power Duties
   - Remarks
   - Toll Taxes

2. Each module contains pages with functionalities for Insert, Delete, Update, Search, and Show operations specific to their data.

## Code Structure Overview

- `mainpg.py`: Main entry point of the application.
- `project.py`, `tenders.py`, `blacklist.py`, `powerduties.py`, `remarks.py`, `tolltaxes.py`: Module files handling GUI and database operations for each functionality.
- `config.py`: Configuration file for MySQL database connection settings.

## Credits

Team Members: [Muhammad Hassan, Eshna Eman , Niyaz Ali ]

Third-Party Libraries:
- Tkinter: GUI library for Python.
- MySQL Connector/Python: MySQL database connector for Python.
