# Student Academic Performance Analysis and Visualization System

A Python Flask-based web application designed to manage and visualize student academic performance. The platform provides separate dashboards for students and faculty members, allowing academic record management, attendance tracking, marks analysis and performance visualization.

## Overview

The application provides two different interfaces:

* **Student Dashboard:** Allows students to access their academic records, view subject-wise marks and visualize their performance.
* **Faculty Dashboard:** Allows professors to view student records, analyse attendance and academic performance, and update assessment marks.

The application uses CSV files for storing student and professor records, Pandas for data processing and Matplotlib for generating visualizations.

## Features

### 1. Student Module

* Student login with credential verification.
* Access to individual academic records.
* Subject-wise marks visualization.
* View assessment details across different subjects.
* Graphical representation of academic performance.

### 2. Faculty Module

* Professor login with credential verification.
* View enrolled students and their academic records.
* Analyse student attendance.
* Visualize total marks obtained by students.
* Update student assessment marks.
* Update attendance records.

### 3. Data Visualization

* Student attendance bar charts.
* Total marks comparison.
* Subject-wise academic performance charts.
* Dynamic chart generation using Matplotlib.

### 4. Academic Record Management

* Maintain student information.
* Store subject-wise academic records.
* Manage assessment components:

  * Project
  * Assignment
  * Midsem
  * Endsem
* Track student attendance.

## Technology Stack

| Technology | Application                      |
| ---------- | -------------------------------- |
| Python     | Backend programming              |
| Flask      | Web application framework        |
| Pandas     | Data processing and manipulation |
| Matplotlib | Data visualization               |
| HTML5      | Frontend structure               |
| CSS3       | Frontend styling                 |
| CSV        | Data storage                     |

## Project Structure

```text
Student-Academic-Performance-Analytics/
│
├── app.py
├── requirements.txt
├── README.md
├── backend/
├── templates/
└── static/
    ├── style.css
    └── charts/
```

### Application Architecture

**Frontend:** HTML templates and CSS provide separate interfaces for students and professors.

**Backend:** Flask handles HTTP requests, login verification, academic record retrieval and record updates.

**Data Processing:** Pandas reads, filters and modifies academic datasets stored in CSV files.

**Visualization:** Matplotlib generates attendance, total marks and subject-wise performance charts.

## Installation and Setup

### Prerequisites

* Python 3.x
* pip

### 1. Clone the repository

```bash
git clone https://github.com/PIYUSH1608-ai/Student-Academic-Performance-Analytics.git
```

### 2. Navigate to the project directory

```bash
cd Student-Academic-Performance-Analytics
```

### 3. Create a virtual environment

```bash
python -m venv env
```

### 4. Activate the environment

**Windows:**

```bash
env\Scripts\activate
```

**Linux/macOS:**

```bash
source env/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
python app.py
```

Open the following address in your browser:

```text
http://127.0.0.1:5000/
```

## Application Routes

| Route                                   | Method | Functionality                     |
| --------------------------------------- | ------ | --------------------------------- |
| `/`                                     | GET    | Homepage                          |
| `/sign_in_prof`                         | GET    | Professor login page              |
| `/signin_prof`                          | POST   | Professor credential verification |
| `/sign_in_student`                      | GET    | Student login page                |
| `/signin_student`                       | POST   | Student credential verification   |
| `/student/<email>/<roll>/data_updation` | GET    | Academic data update form         |
| `/student/<email>/<roll>`               | POST   | Update academic records           |

## Screenshots

Screenshots demonstrating the following interfaces can be found in the project:

1. Homepage and navigation.
2. Student login and dashboard.
3. Professor login and dashboard.
4. Attendance and total marks visualizations.
5. Academic record update interface.

## Technical Concepts Demonstrated

* Flask routing and request handling.
* Object-oriented and functional Python programming.
* Data processing using Pandas.
* CSV-based record management.
* Dynamic data visualization.
* HTML template rendering using Jinja.
* Form handling and server-side data updates.
* Basic credential verification.

## Current Limitations and Future Improvements

* Migrate CSV-based storage to SQLite or PostgreSQL.
* Implement session-based authentication and role-based authorization.
* Introduce secure password hashing.
* Expand input validation and error handling.
* Add automated testing.
* Improve dashboard functionality and reporting.

## Project Objective

The project explores practical web application development, backend programming, academic data management and data visualization through a student academic performance management platform.
