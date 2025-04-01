# Application Health Monitoring Tools

This repository contains scripts for monitoring application health and system performance, created as part of the Accuknox DevOps assessment.

## Contents

- [app-health-checker.py](#application-health-checker) - Script to check and monitor application health via HTTP status codes
- [shm.py](#system-health-monitor) - System health monitoring script that tracks CPU, memory, and disk usage
- [system_health.log](#logs) - Log file containing system health monitoring results

## Application Health Checker

`app-health-checker.py` is a Python script that monitors the health of a web application by sending HTTP requests and analyzing the response codes. It can determine if an application is functioning correctly or experiencing issues.

### Features

- Continuously monitors application health with configurable intervals
- Supports both GET and POST HTTP methods
- Handles various connection errors with custom status codes
- Provides clear up/down status reporting

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

### Configuration

You can modify the following variables in the `main()` function:
- `url`: The base URL of the application to monitor
- `interval`: Time between health checks (in seconds)

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


## License

[MIT License](LICENSE)
