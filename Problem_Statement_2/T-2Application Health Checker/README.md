# Application Health Checker

This repository contains scripts for application health checker 
## Contents

- [app-health-checker.py](#application-health-checker) - Script to check and monitor application health via HTTP status codes


## Application Health Checker

`app-health-checker.py` is a Python script that monitors the health of a web application by sending HTTP requests and analyzing the response codes. It can determine if an application is functioning correctly or experiencing issues.

### Features

- Supports both GET and POST HTTP methods
- Handles various connection errors with custom status codes

### Custom HTTP Status Codes

The script uses the following custom status codes to handle various connection scenarios:
- `999`: Connection errors (unable to establish connection)
- `998`: Connection timeout errors (connection attempt timed out)
- `997`: Response timeout errors (connection established but server didn't respond in time)

### Usage

```bash
python3 app-health-checker.py
```

By default, the script monitors a local application at `http://localhost:8000/` with a 4-second interval between checks.


### Dependencies

- Python 3.13 or higher
- Requests library

Install dependencies using:
```bash
pip install requests
```

Inorder to test the script please run the crud-app. Find more details on how to run in crud-app/readme.md

### Testing

To test the script, you'll need to run the CRUD application. See `crud-app/readme.md` for details on how to set up and run the test application.

