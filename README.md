# 🧪 QuizVerse

## 🚀 Project Overview

**QuizVerse** is a lightweight, interactive multiple-choice quiz application built with Django. It demonstrates full-stack fundamentals including database relationships, form handling, request lifecycle management, and dynamic template rendering—all styled with a modern UI using Tailwind CSS.

### Key Highlights
- **Django ORM Relationships:** Robust data modeling with Foreign Keys.
- **Optimization:** Efficient database querying using `prefetch_related`.
- **Security:** Secure form handling with built-in CSRF protection.
- **Modern UI:** Clean, responsive design utilizing Tailwind CSS.

---

## ✨ Features

### Home & Quiz Interface
- **Dynamic Loading:** Fetches all questions and associated choices from the database.
- **Optimized Queries:** Uses `prefetch_related('choices')` to minimize database hits.
- **Interactive UI:** Questions are presented with radio-button choices in a card-based layout.

### Scoring Engine
- **Submission Handling:** Processes user answers securely via `POST` requests.
- **Validation:** Compares user input against the database `is_correct` field.
- **Scoring:** Instantly calculates the total score upon submission.
- **Results Page:** Displays the final score, total questions, and a "Retake Quiz" option.

### UI / UX Design
- **Responsive Layout:** Built with a global `base.html` containing a sticky navbar and footer.
- **Styling:** Fast and modern styling via **Tailwind CSS** (CDN).
- **Icons:** Visual enhancements provided by **Font Awesome**.

---

## 🛠 Tech Stack

- **Backend:** Django (Python)
- **Database:** SQLite (Default)
- **Frontend:** HTML5, Tailwind CSS (CDN), Font Awesome

---

## 📂 Project Structure

```bash
QuizVerse/
├── manage.py                # Django project management script
├── Quiz_Verse/              # Project Configuration
│   ├── settings.py          # Apps, database, and template config
│   ├── urls.py              # Root URL config
│   ├── asgi.py
│   └── wsgi.py
├── quiz_app/                # Main Application
│   ├── models.py            # Question and Choice database models
│   ├── views.py             # Quiz rendering and scoring logic
│   ├── urls.py              # App-level URL routing
│   ├── admin.py             # Admin panel configuration
│   ├── migrations/          # Database migrations
│   └── templates/
│       ├── quiz.html        # Quiz interface template
│       └── score.html       # Score display template
└── templates/
    └── base.html            # Shared base layout (Nav, Footer, Scripts)
```
## 🗄️Data Models

Defined in `quiz_app/models.py`:

### 1️⃣Question
- Represents the query presented to the user.
  - text: CharField containing the question string.
  - choices: Reverse relationship from the Choice model.
  - Returns: The question text string.

### 2️⃣Choice
- Represents an answer option for a specific question.
  - question: ForeignKey linking to the Question model (Cascades on delete).
  - text: CharField containing the answer option.
  - is_correct: BooleanField indicating if this choice is the right answer (default: False).
  - Returns: The choice text string.


### 💻Setup & Installation


- **Install dependencies**
  - From the project root (where manage.py lives)
  ```bash
  pip install django
  ```

- **Apply Database migrations**
  - Initialize the SQLite database and create tables.
  ```bash
  python manage.py migrate
  ```

- **Create a superuser (optional, for admin management)**

  ```bash
  python manage.py createsuperuser
  ```

- **Run the development server**

  ```bash
  python manage.py runserver
  ```

- **Access the app**
  - Quiz: `http://127.0.0.1:8000/`
  - Admin panel: `http://127.0.0.1:8000/admin/`



------------------------

