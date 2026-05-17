
# 📚LessonFlow


![Python](https://img.shields.io/badge/Python-3.12-blue)
![Flask](https://img.shields.io/badge/Flask-Backend-black)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)
![Docker](https://img.shields.io/badge/Docker-Containerization-2496ED)
![Status](https://img.shields.io/badge/Status-In%20Development-orange)

AI-powered lesson plan management platform built with Flask, Bootstrap and PostgreSQL.
<img width="2172" height="724" alt="banner_oficial" src="https://github.com/user-attachments/assets/2318dd9d-f2f9-47c5-8dfb-ba14017b3195" />

## Overview

LessonFlow is an educational platform focused on lesson planning and pedagogical content organization.

The system allows teachers to manage lesson plans efficiently while using AI-powered recommendations to generate complementary teaching content, related topics and suggested tags.

This project was developed as a technical challenge with focus on:

- REST API development
- Full-stack integration
- AI-assisted educational tools
- Modular backend architecture
- Dockerized environment
- Logging and observability
- Professional development workflow

---

## Features

### Lesson Plan Management
- Create lesson plans
- Edit lesson plans
- Delete lesson plans
- Paginated lesson listing
- Search by lesson title
- Filter by subject, tags and planned date
- Sorting by title or creation date

### AI Smart Assist
- AI-generated teaching recommendations
- Suggested complementary topics
- Automatic tag generation
- Structured JSON responses from LLM integration

### Technical Features
- RESTful API
- Form validation
- Structured logging
- Environment variable management
- Docker support
- Health check endpoint
- Responsive interface

---

## Tech Stack

### Backend
- Python
- Flask
- SQLAlchemy
- PostgreSQL / SQLite

### Frontend
- HTML5
- CSS3
- Bootstrap
- JavaScript

### DevOps
- Docker
- Docker Compose
- GitHub Actions

---

## Project Structure

```bash
lessonflow/
│
├── backend/
│   ├── app/
│   │   ├── routes/
│   │   ├── models/
│   │   ├── services/
│   │   ├── schemas/
│   │   ├── utils/
│   │   └── config/
│   │
│   ├── tests/
│   ├── requirements.txt
│   ├── Dockerfile
│   └── run.py
│
├── frontend/
│
├── docker-compose.yml
├── .env.example
├── README.md
└── .github/
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/your-username/lessonflow.git
cd lessonflow
```

---

## Backend Setup

### Create virtual environment

```bash
python -m venv venv
```

### Activate virtual environment

#### Windows
```bash
venv\Scripts\activate
```

#### Linux / Mac
```bash
source venv/bin/activate
```

---

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file inside the backend folder:

```env
FLASK_APP=run.py
FLASK_ENV=development

SECRET_KEY=your_secret_key

DATABASE_URL=postgresql://user:password@localhost:5432/lessonflow

OPENAI_API_KEY=your_api_key
```

---

## Running the Application

```bash
flask run
```

---

## Docker Setup

```bash
docker compose up --build
```

---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | /lesson-plans | List lesson plans |
| GET | /lesson-plans/<id> | Get lesson plan |
| POST | /lesson-plans | Create lesson plan |
| PUT | /lesson-plans/<id> | Update lesson plan |
| DELETE | /lesson-plans/<id> | Delete lesson plan |
| POST | /ai/recommendations | Generate AI suggestions |
| GET | /health | Health check |

---

## Example AI Request

```json
{
  "title": "Introduction to Computer Networks",
  "subject": "Networking",
  "summary": "Basic concepts of IP addressing and routing."
}
```

---

## Screenshots

> Screenshots will be added during development.

---

## Future Improvements

- Authentication and authorization
- User roles
- Unit and integration tests
- CI/CD pipeline improvements
- AI prompt optimization
- Dashboard analytics
- Cloud deployment

---

## Development Practices

- Clean code principles
- Conventional commits
- Environment variable protection
- Modular architecture
- Error handling
- RESTful conventions

---

## Author

Developed by Rafael.
