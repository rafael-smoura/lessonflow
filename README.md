# LessonFlow

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Flask](https://img.shields.io/badge/Flask-Backend-black)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)
![Docker](https://img.shields.io/badge/Docker-Containerization-2496ED)
![Status](https://img.shields.io/badge/Status-In%20Development-orange)

AI-powered lesson plan management platform built with Flask, Bootstrap and PostgreSQL.

<img width="2172" height="724" alt="banner_oficial" src="https://github.com/user-attachments/assets/2318dd9d-f2f9-47c5-8dfb-ba14017b3195" />

---
# 🚀 Production Demo

The project is fully online and available for testing! The application was deployed using a modern, decoupled architecture on **Render**:

* **🔗 Application Link:** <a href="https://lessonflow-frontend.onrender.com/" target="_blank" rel="noopener noreferrer">https://lessonflow-frontend.onrender.com/</a>

### 🏗️ Deployment Architecture
* **Frontend:** Hosted as a *Static Site* for fast and optimized loading times.
* **Backend:** Containerized with **Docker** into a *Web Service*, handling requests using Python/Flask.
* **Database:** Isolated **PostgreSQL** instance for secure persistence of lesson plans.
* **AI:** Real-time integration with the **Groq** API for smart content generation.

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

# 🐳 Docker & Containerization

The application is fully containerized using Docker Compose, allowing you to orchestrate and spin up the entire ecosystem (Backend + Frontend) with a single command.

## Running with Docker Compose (Recommended)

1. Ensure you have a `.env` file configured in the root directory of the project containing your `GROQ_API_KEY`.
2. Run the following command from the project root:

```bash
docker-compose up --build

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

<img width="1919" height="573" alt="dashboard" src="https://github.com/user-attachments/assets/73673e2f-4d0d-487f-81a1-b367c1e4bd50" />

---

## AI Recommendation System

> Add AI assistant screenshot here
<img width="1918" height="756" alt="ezgif com-animated-gif-maker (2)" src="https://github.com/user-attachments/assets/248f4052-fbde-426b-a272-ba144b9868f1" />

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

# 🧠 Challenges Faced & Key Learnings

Developing **LessonFlow** was a highly rewarding experience that pushed my technical boundaries, especially since this was only my **second time creating a full-stack integration** between a Frontend and a Backend application. 

As my previous technical background was significantly stronger in **Backend development**, my knowledge of Frontend concepts and Vanilla JavaScript was very basic. This discrepancy forced me to find intelligent ways to accelerate my learning curve and meet the strict project deadlines, which is where utilizing Artificial Intelligence as a strategic co-pilot became essential.

### 1. The SPA Experience vs. Flask's Native Synchronous Behavior
Initially, whenever a user submitted a form or requested an AI generation, the browser followed its native HTTP behavior: it triggered a full-page reload (the traditional "F5 refresh effect"). Because the project demanded a fluid, seamless interface inspired by Notion, a standard multi-page reload was unacceptable.
* **How AI helped me solve it:** I used AI to study DOM manipulation and asynchronous operations. With its assistance, I implemented `event.preventDefault()` to intercept form submissions and completely restructured the API communications using JavaScript's `fetch()` API combined with `async/await`. This allowed data to flow to and from the Flask server in the background, updating the UI dynamically without a single page refresh.

### 2. Debugging the Data Flow: Overcoming the `[object Object]` Trap
During the initial connections between the Frontend and the Groq AI service on the Backend, the application frequently outputted `[object Object]` inside the recommendation textareas instead of the actual text. 
* **How AI helped me solve it:** Coming from a backend perspective, I had to quickly understand how JavaScript treats JSON objects in the browser's memory. With the help of AI, I learned how to debug the server response payload, ensuring I was correctly mapping the nested properties (e.g., `result.data.contents`) and using error-handling try-catch blocks to catch malformed structures before they reached the user interface.

### 3. Rapid Upskilling Under Tight Deadlines
To deliver a production-ready application within the challenge's timeline, I had to deeply study and apply complex architectural patterns simultaneously:
* Implementing the **Application Factory Pattern** and **Blueprints** in Flask.
* Enforcing strict validation schemas using **Marshmallow**.
* Structuring strict JSON prompt formats for the **Groq API**.
* Ensuring environment isolation using **Docker & Docker Compose**.

Using AI during this project was never about blindly copying and pasting code. Instead, it served as an on-demand, private technical mentor that helped me translate complex architectural requirements into functional, clean code while drastically reducing the time spent debugging unfamiliar frontend syntax.

---

# 👨‍💻 Author

Developed by Rafael Moura.

GitHub:
https://github.com/rafael-smoura

