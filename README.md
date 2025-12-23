
<a name="readme-top"></a>

<div align="center">

  <h3><b>AUTHENTICATION MICROSERVICE</b></h3>
  <p>A simple authentication microservice built with FastAPI, SQLite, and JWT (CSC 805 – Task 3)</p>

  <!-- Badges -->
  <p>
    <img src="https://img.shields.io/badge/Python-3.11-blue.svg" alt="Python">
    <img src="https://img.shields.io/badge/FastAPI-latest-green.svg" alt="FastAPI">
    <img src="https://img.shields.io/badge/Uvicorn-latest-purple.svg" alt="Uvicorn">
    <img src="https://img.shields.io/badge/SQLite-3.39-lightgrey.svg" alt="SQLite">
    <img src="https://img.shields.io/badge/License-Educational-yellow.svg" alt="License">
  </p>

</div>


---

# 📗 Table of Contents

- [📗 Table of Contents](#-table-of-contents)
- [Authentication Microservice](#authentication-microservice)
  - [🛠 Features](#-features)
  - [🏗️ Project Structure](#-project-structure)
  - [🧠 Technology Stack](#-technology-stack)
  - [⚙️ Setup & Installation](#-setup--installation)
  - [🗄️ Database Setup](#-database-setup)
  - [▶️ Running the Service](#-running-the-service)
  - [📡 API Endpoints](#-api-endpoints)
  - [🧪 Testing Examples](#-testing-examples)
  - [📝 Notes](#-notes)
  - [👥 Authors](#-authors)
  - [📝 License](#-license)

---

# Authentication Microservice <a name="authentication-microservice"></a>

> This is a lightweight **authentication microservice** built with **FastAPI**.  
> It provides user registration and login functionality via REST APIs, using **SQLite** for storage and **JWT** for secure authentication.

---

## 🛠 Features <a name="features"></a>

- User registration (`/register`)  
- User login (`/login`) with JWT token generation  
- Password hashing using **bcrypt** (72-byte limit handled)  
- SQLite database storage  
- Exception handling and logging  
- REST API communication  

---

## 🏗️ Project Structure <a name="project-structure"></a>

```

Task3_Microservice/
├── app/
│   ├── main.py        # FastAPI entry point
│   ├── models.py      # Pydantic models
│   ├── database.py    # Database connection & session handling
├── venv/              # Virtual environment
│   ├── bin/
│   ├── include/
│   ├── lib/
│   └── pyvenv.cfg
├── test.db            # SQLite database file
├── .env               # Environment variables
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation

````

---

## 🧠 Technology Stack <a name="technology-stack"></a>

- **Python:** 3.11  
- **FastAPI:** latest  
- **Uvicorn:** latest  
- **SQLAlchemy:** latest  
- **Passlib (bcrypt):** latest  
- **python-jose:** latest  
- **Database:** SQLite  

---

## ⚙️ Setup & Installation <a name="setup--installation"></a>

1. Clone the repository:
```bash
git clone <repository-url>
cd Implement_a_Microservice
````

2. Create a virtual environment:

```bash
python3 -m venv venv
```

3. Activate the virtual environment:

* Linux/macOS:

```bash
source venv/bin/activate
```

* Windows:

```bash
venv\Scripts\activate
```

4. Install dependencies:

```bash
pip install fastapi uvicorn sqlalchemy 'passlib[bcrypt]' python-jose
```

---

## 🗄️ Database Setup <a name="database-setup"></a>

SQLite is used as the database. To create the required tables:

```python
from app.database import engine
from app.models import Base
Base.metadata.create_all(bind=engine)
```

> This will create `test.db` with the required tables.

---

## ▶️ Running the Service <a name="running-the-service"></a>

Start the FastAPI server:

```bash
python3 -m uvicorn app.main:app --reload --port 8002
```

Access the service at:

```
http://127.0.0.1:8002
```

---

## 📡 API Endpoints <a name="api-endpoints"></a>

| Endpoint    | Method | Request Body                                               | Response                                        | Notes                         |
| ----------- | ------ | ---------------------------------------------------------- | ----------------------------------------------- | ----------------------------- |
| `/`         | GET    | –                                                          | `{ "message": "Auth microservice is running" }` | Health check                  |
| `/register` | POST   | `{ "username": "...", "email": "...", "password": "..." }` | `{ "message": "User registered successfully" }` | Passwords >72 bytes truncated |
| `/login`    | POST   | `{ "email": "...", "password": "..." }`                    | `{ "access_token": "jwt_token_here" }`          | Returns JWT token             |

---

## 🧪 Testing Examples <a name="testing-examples"></a>

**Register a user:**

```bash
curl -X POST "http://127.0.0.1:8002/register" \
-H "Content-Type: application/json" \
-d '{"username":"edu1","email":"edu1@example.com","password":"mypassword"}'
```

**Login a user:**

```bash
curl -X POST "http://127.0.0.1:8002/login" \
-H "Content-Type: application/json" \
-d '{"email":"edu1@example.com","password":"mypassword"}'
```

---

## 📝 Notes <a name="notes"></a>

* JWT secret key is hardcoded (`your_secret_key`) for demo purposes. **Use environment variables in production.**
* SQLite is used for simplicity. Switch to MySQL/PostgreSQL in production.
* Passwords are hashed using **bcrypt** for security.

---

## 👥 Authors <a name="authors"></a>

👤 **King Immanuel**

* GitHub: [@Kingno3l](https://github.com/Kingno3l)
* LinkedIn: [King Immanuel](https://www.linkedin.com/in/kingno3l)

---

## 📝 License <a name="license"></a>

This project is for **educational purposes**.
