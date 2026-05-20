# LessonFlow

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Flask](https://img.shields.io/badge/Flask-Backend-black)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)
![Docker](https://img.shields.io/badge/Docker-Containerization-2496ED)
![Status](https://img.shields.io/badge/Status-In%20Development-orange)

AI-powered lesson plan management platform built with Flask, Bootstrap and PostgreSQL.

<img width="2172" height="724" alt="banner_oficial" src="https://github.com/user-attachments/assets/2318dd9d-f2f9-47c5-8dfb-ba14017b3195" />

---


</div>

<details>
<summary><b>📑 Click to expand Table of Contents</b></summary>

# 📑 Table of Contents

- [🚀 Live Production Demo](#-live-production-demo)
- [🏗️ Deployment Architecture](#️-deployment-architecture)
- [✨ Core Features](#-core-features)
  - [📖 Lesson Plan Management](#-lesson-plan-management)
  - [🤖 AI Smart Assistant](#-ai-smart-assistant)
  - [🌎 Frontend Experience](#-frontend-experience)
- [🛠️ Tech Stack](#️-tech-stack)
  - [Backend](#backend)
  - [Frontend](#frontend)
  - [DevOps & Tools](#devops--tools)
- [🧠 Software Architecture](#-software-architecture)
- [⚙️ Architecture Highlights](#️-architecture-highlights)
- [📂 Project Structure](#-project-structure)
- [📸 Screenshots](#-screenshots)
- [⚙️ Installation](#️-installation)
- [🔧 Backend Setup](#-backend-setup)
- [🔐 Environment Variables](#-environment-variables)
- [▶️ Running The Application](#️-running-the-application)
- [🐳 Docker & Containerization](#-docker--containerization)
- [📡 API Endpoints](#-api-endpoints)
- [🧪 Example Request](#-example-request)
- [🧠 Challenges Faced & Key Learnings](#-challenges-faced--key-learnings)
- [🚀 Future Improvements](#-future-improvements)
- [📚 Development Practices](#-development-practices)
- [📈 GitHub Stats](#-github-stats)
- [👨‍💻 Author](#-author)
  </details>

---

# 🚀 Live Production Demo

The project is fully online and available for testing! The application was deployed using a modern, decoupled architecture on **Render**:

* **🔗 Application Link:** <a href="https://lessonflow-frontend.onrender.com/" target="_blank" rel="noopener noreferrer">https://lessonflow-frontend.onrender.com/</a>


</div>

---

# 🏗️ Deployment Architecture

LessonFlow uses a fully decoupled production architecture deployed on Render.

| Layer | Technology | Description |
|---|---|---|
| Frontend | Static Site | Optimized SPA-like frontend |
| Backend | Flask + Docker | REST API and business logic |
| Database | PostgreSQL | Persistent data storage |
| AI Integration | Groq API | Smart educational recommendations |

---

# ✨ Core Features

# 📖 Lesson Plan Management

- Create lesson plans
- Edit lesson plans
- Delete lesson plans
- Paginated lesson listing
- Search by lesson title
- Filter by discipline
- Tag-based filtering
- Planned date management

---

# 🤖 AI Smart Assistant

- AI-generated teaching recommendations
- Suggested complementary content
- Automatic educational tags
- Suggested support resources
- Structured JSON AI responses
- Real-time recommendation generation

---

# 🌎 Frontend Experience

- Responsive interface
- Dark / Light mode
- English / Portuguese support
- Dynamic DOM updates
- SPA-like navigation
- Real-time filtering
- Async API communication
- Smooth animations without page reloads

---

# 🛠️ Tech Stack

## Backend

- Python
- Flask
- SQLAlchemy
- Marshmallow
- PostgreSQL
- SQLite
- REST APIs
- Groq API Integration

---

## Frontend

- HTML5
- CSS3
- Bootstrap 5
- Vanilla JavaScript
- Async/Await
- Fetch API

---

## DevOps & Tools

- Docker
- Docker Compose
- Git
- GitHub
- Render Deployment

---

# 🧠 Software Architecture

The backend follows scalable and modular software engineering patterns.

```bash
app/
├── ai/
├── extensions/
├── models/
├── routes/
├── schemas/
└── services/
```

---

# ⚙️ Architecture Highlights

- Application Factory Pattern
- Blueprints
- Service Layer
- Schema Validation
- Environment Variables
- Separation of Concerns
- RESTful conventions
- Modular Architecture
- AI Integration Layer

---

# 📂 Project Structure

```bash
lessonflow/
│
├── backend/
│   ├── app/
│   │   ├── ai/
│   │   │   └── lesson_plan_ai.py
│   │   ├── config/
│   │   │   └── config.py
│   │   ├── extensions/
│   │   │   └── extensions.py
│   │   ├── models/
│   │   │   ├── lesson_plan.py
│   │   │   └── user.py
│   │   ├── routes/
│   │   │   ├── auth_routes.py
│   │   │   └── lesson_plan_routes.py
│   │   ├── schemas/
│   │   │   └── lesson_plan_schema.py
│   │   ├── services/
│   │   │   └── lesson_plan_service.py
│   │   └── __init__.py
│   │
│   ├── .dockerignore
│   ├── .env
│   ├── Dockerfile
│   ├── requirements.txt
│   └── run.py
│
├── frontend/
│   ├── css/
│   │   └── styles.css
│   ├── img/
│   │   └── favicon.png
│   ├── js/
│   │   └── app.js
│   ├── Dockerfile
│   └── index.html
│
├── .gitignore
├── docker-compose.yml
├── LICENSE
└── README.md
```

---

# 📸 Screenshots

# 🖥️ Dashboard

<img width="1919" height="573" alt="dashboard" src="https://github.com/user-attachments/assets/73673e2f-4d0d-487f-81a1-b367c1e4bd50" />

---

# 🤖 AI Recommendation System

<img width="1918" height="756" alt="ezgif com-animated-gif-maker (2)" src="https://github.com/user-attachments/assets/248f4052-fbde-426b-a272-ba144b9868f1" />

---

# ⚙️ Installation

# Clone Repository

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
GROQ_API_KEY=your_api_key
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

# 🐳 Docker & Containerization

The application is fully containerized using Docker Compose, allowing you to orchestrate and spin up the entire ecosystem (Backend + Frontend) with a single command.

## Running with Docker Compose (Recommended)

1. Ensure you have a `.env` file configured in the root directory of the project containing your `GROQ_API_KEY`.
2. Run the following command from the project root:

```bash
docker-compose up --build
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
| POST | `/lesson-plans/ai-recommendations` | Generate AI recommendations |

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

# 🧠 Challenges Faced & Key Learnings

video here: https://drive.google.com/file/d/1mCnK795UxGB0qv_2YZLPotZ4qpwzq3dB/view?usp=drivesdk

Developing LessonFlow was a highly rewarding experience that pushed my technical boundaries, especially because this was only my second full-stack integration project.

As my background was significantly stronger in Backend Engineering, I had to rapidly improve my Frontend and JavaScript knowledge while simultaneously delivering a production-ready application.

---

## 1. SPA Experience, Styling & AI Co-piloting

Initially, every request triggered a complete browser page reload, interrupting animations and dynamic interactions. 

As my background was significantly stronger in Backend Engineering, my Frontend skills (JavaScript and CSS) were basic at the time. To bridge this gap, build a polished UI, and deliver a production-ready SPA experience efficiently, **I utilized AI assistance as a coding co-pilot and learning accelerator for both JavaScript logic and CSS styling**.

### Solution & Learning Process
With the help of AI to guide my learning, troubleshoot syntax, and assist with responsive layouts, I designed and implemented the frontend using:
- `event.preventDefault()`, `fetch()`, and `async/await` for asynchronous communication.
- Dynamic DOM manipulation to avoid page reloads.
- Modern CSS and Bootstrap overrides to ensure a clean, responsive, and visually cohesive layout.

This approach not only allowed the frontend to communicate seamlessly with the Flask backend but also served as an intensive, hands-on masterclass in modern UI development for me.

---

## 2. Debugging JSON Data Flow

During the integration with the Groq API, the frontend frequently rendered:

```bash
[object Object]
```

instead of the expected AI-generated text.

### Solution

I learned how JavaScript handles objects and JSON serialization in the browser and implemented:

- Better response mapping
- Structured JSON validation
- Error handling with try/catch
- Safer UI rendering logic

---

## 3. Backend Architecture Evolution

To make the project scalable and production-ready, I studied and implemented:

- Application Factory Pattern
- Blueprints
- Service Layer
- Marshmallow Validation
- Docker Containerization
- RESTful API conventions

This significantly improved maintainability and separation of concerns across the project.

---

# 🚀 Future Improvements

- JWT authentication
- User accounts
- Role-based access
- Automated tests
- CI/CD pipelines
- AI prompt optimization
- Analytics dashboard
- WebSockets for live updates
- Redis caching
- Cloud-native deployment improvements

---

# 📚 Development Practices

- Clean Code
- RESTful API Design
- Conventional Commits
- Separation of Concerns
- Environment Variable Protection
- Modular Architecture
- Scalable Backend Patterns

---


# 📈 Contribution Graph

<div align="center">

<img src="https://github-readme-activity-graph.vercel.app/graph?username=rafael-smoura&theme=react-dark&hide_border=true"/>

</div>

# 👨‍💻 Author

<div align="center">

## Rafael Moura

Backend-focused Software Engineering student passionate about scalable systems, APIs and software architecture.

GitHub:
https://github.com/rafael-smoura

</div>
