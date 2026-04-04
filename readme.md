## Overview

This project is a FastAPI-based backend application that integrates with the GitHub REST API. It allows users to authenticate using a Personal Access Token (PAT) and perform operations such as fetching repositories, creating issues, and listing issues.

The goal of this project is to demonstrate backend development skills including API integration, authentication handling, and clean architecture design.

---

## Features

* Authenticate with GitHub using Personal Access Token
* Fetch repositories of a user
* Create issues in a repository
* List issues from a repository
* Structured and modular backend design
* Proper error handling using HTTP exceptions

---

## Tech Stack

* Python
* FastAPI
* Requests
* Pydantic
* Uvicorn

---

## Project Structure

```
github-connector/
│
├── app/
│   ├── main.py
│   ├── routes/
│   │   └── github.py
│   ├── services/
│   │   └── github_service.py
│   ├── core/
│   │   └── config.py
│   ├── models/
│   │   └── schemas.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Setup Instructions

### 1. Clone the repository

```
git clone <your-repo-url>
cd github-connector
```

### 2. Create virtual environment

```
python -m venv venv
```

Activate it:

Windows

```
venv\Scripts\activate
```

Mac/Linux

```
source venv/bin/activate
```

---

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

### 4. Configure environment variables

Create a `.env` file in the root directory and add:

```
GITHUB_TOKEN=your_personal_access_token
```

Note:

* Use a Personal Access Token (Classic)
* Enable `repo` scope

---

### 5. Run the application

```
uvicorn app.main:app --reload
```

---

### 6. Access API documentation

Open:

```
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### 1. Fetch Repositories

GET `/github/repos/{username}`

Description: Fetch all repositories of a given GitHub user.

---

### 2. Create Issue

POST `/github/create-issue`

Request Body:

```
{
  "owner": "username",
  "repo": "repository-name",
  "title": "Issue title",
  "body": "Issue description"
}
```

---

### 3. List Issues

GET `/github/issues/{owner}/{repo}`

Description: Retrieve all issues from a repository.

---

## Error Handling

* Returns appropriate HTTP status codes
* Handles GitHub API errors (403, 404, etc.)
* Validates request body using Pydantic models

---

## Security

* GitHub token is stored in environment variables
* `.env` file is excluded using `.gitignore`
* No sensitive data is hardcoded

---

## Future Improvements

* OAuth 2.0 authentication
* Async API calls using httpx
* Docker containerization
* Logging and monitoring
* Additional GitHub actions (pull requests, commits, etc.)

---
