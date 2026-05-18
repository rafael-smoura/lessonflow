# 📚 LessonFlow

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Flask](https://img.shields.io/badge/Flask-Backend-black)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)
![Docker](https://img.shields.io/badge/Docker-Containerization-2496ED)
![Status](https://img.shields.io/badge/Status-In%20Development-orange)

AI-powered lesson plan management platform built with Flask, Bootstrap and PostgreSQL.

<img width="2172" height="724" alt="banner_oficial" src="https://github.com/user-attachments/assets/2318dd9d-f2f9-47c5-8dfb-ba14017b3195" />

---

# 🚀 Overview

LessonFlow is a full-stack educational platform focused on lesson planning, pedagogical organization and AI-assisted teaching workflows.

The platform allows teachers to:

- create and manage lesson plans
- organize educational content
- search and filter lessons
- receive AI-generated recommendations
- improve teaching productivity

This project was developed as a technical challenge with focus on professional backend architecture, REST APIs and AI integration.

---

# ✨ Features

## 📖 Lesson Plan Management

- Create lesson plans
- Edit lesson plans
- Delete lesson plans
- Paginated lesson listing
- Search by lesson title
- Filter by discipline
- Tag-based filtering
- Planned date management

---

## 🤖 AI Smart Assist

- AI-generated teaching recommendations
- Suggested complementary content
- Automatic educational tags
- Suggested support resources
- Structured JSON AI responses

---

## 🌎 Frontend Features

- Responsive interface
- Dark / Light mode
- English / Portuguese support
- Real-time filtering
- Dynamic suggestions
- SPA-like navigation experience

---

# 🛠️ Tech Stack

## Backend

- Python
- Flask
- SQLAlchemy
- Marshmallow
- PostgreSQL / SQLite
- OpenAI-compatible API integration

---

## Frontend

- HTML5
- CSS3
- Bootstrap 5
- Vanilla JavaScript

---

## DevOps

- Docker
- Git
- GitHub

---

# 🧠 Software Architecture

The backend follows a modular and scalable architecture pattern:

```bash
app/
├── ai/
├── models/
├── routes/
├── schemas/
├── services/
└── extensions/

```

## Architecture Highlights

- Application Factory Pattern
- Blueprints
- Service Layer
- Schema Validation
- Environment Variables
- Separation of Concerns
- RESTful conventions

---

# 📂 Project Structure

```bash
lessonflow/
│
├── backend/
│   ├── app/
│   │   ├── ai/
│   │   ├── models/
│   │   ├── routes/
│   │   ├── schemas/
│   │   ├── services/
│   │   └── extensions/
│   │   
│   │
│   ├── requirements.txt
│   ├── Dockerfile
│   └── run.py
│
├── frontend/
│
├── .env.example
├── README.md
└── .gitignore
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/rafael-smoura/lessonflow.git

cd lessonflow
```

---

# 🔧 Backend Setup

## Create Virtual Environment

```bash
python -m venv .venv
```

---

## Activate Virtual Environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux / Mac

```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔐 Environment Variables

Create a `.env` file inside `/backend`.

Example:

```env
GROQ_API_KEY=your_key_api
```

---

# ▶️ Running The Application

## Local Development

```bash
python run.py
```

Application will run at:

```bash
http://127.0.0.1:17001
```

---

# 🐳 Docker

## Build Container

```bash
cd backend
docker build -t lessonflow-api .
```

## Run Container

```bash
docker run -p 17001:17001 --env-file .env lessonflow-api<img width="666" height="677" alt="Screenshot 2026-05-18 154216" src="https://github.com/user-attachments/assets/713d8a2b-595b-448f-a7d8-8e208e93d5d0" />

```

---

# 📡 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/lesson-plans` | List lesson plans |
| GET | `/lesson-plans/<id>` | Get lesson plan |
| POST | `/lesson-plans` | Create lesson plan |
| PUT | `/lesson-plans/<id>` | Update lesson plan |
| DELETE | `/lesson-plans/<id>` | Delete lesson plan |
| POST | `/lesson-plans/ai-recommendations` | Generate AI suggestions |

---

# 🧪 Example Request

## POST `/lesson-plans`

```json
{
  "title": "Introduction to Algebra",
  "objective": "Teach algebra basics",
  "summary": "First contact with algebra",
  "planned_date": "2026-05-20",
  "discipline": "Mathematics",
  "contents": "Variables and equations",
  "support_resources": "Slides and exercises",
  "tags": "math,algebra"
}
```

---

# 📸 Screenshots

## Dashboard

<img width="1916" height="445" alt="ezgif com-animated-gif-maker" src="https://github.com/user-attachments/assets/25fae0ad-86b8-45af-b50e-8c50cfcc23c7" />

---

## AI Recommendation System

> Add AI assistant screenshot here
<img width="1906" height="910" alt="image" src="https://github.com/user-attachments/assets/06e9d2cf-6892-440c-87dd-c190035c9044" />

---


# 🚀 Future Improvements

- JWT authentication
- User accounts
- Role-based access
- Automated tests
- CI/CD pipelines
- AI prompt optimization
- Analytics dashboard
- Cloud deployment

---

# 📚 Development Practices

- Clean Code
- RESTful API Design
- Conventional Commits
- Modular Architecture
- Separation of Concerns
- Environment Variable Protection

---

# 👨‍💻 Author

Developed by Rafael Moura.

GitHub:
https://github.com/rafael-smoura

