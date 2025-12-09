project:
  name: Auth Microservice
  description: >
    A simple authentication microservice built using FastAPI, SQLAlchemy, Passlib (bcrypt), and JWT.
    Provides user registration and login functionality via REST APIs.

features:
  - User registration (/register)
  - User login (/login) with JWT token generation
  - Password hashing using bcrypt (72-byte limit handled)
  - SQLite database storage
  - Exception handling and logging
  - REST API communication

technology_stack:
  python: 3.11
  fastapi: latest
  uvicorn: latest
  sqlalchemy: latest
  passlib: bcrypt
  python_jose: latest
  database: SQLite

folder_structure:
  - app/
    - __pycache__/
    - main.py
    - models.py
    - database.py
  - venv/
    - bin/
    - include/
    - lib/
    - pyvenv.cfg
  - test.db
  - .env

installation:
  steps:
    - git_clone: "git clone <repository-url>"
    - cd_repo: "cd Implement_a_Microservice"
    - create_venv: "python3 -m venv venv"
    - activate_venv: "source venv/bin/activate"
    - install_deps: "pip install fastapi uvicorn sqlalchemy 'passlib[bcrypt]' python-jose"

database_setup:
  description: SQLite is used as the database
  commands:
    - "from app.database import engine"
    - "from app.models import Base"
    - "Base.metadata.create_all(bind=engine)"
  notes: "This will create a test.db file with the required tables."

running_service:
  command: "python3 -m uvicorn main:app --reload --port 8002"
  url: "http://127.0.0.1:8002"

api_endpoints:
  health_check:
    method: GET
    path: "/"
    response:
      message: "Auth microservice is running"

  register:
    method: POST
    path: "/register"
    headers:
      Content-Type: application/json
    request_body:
      username: "your_username"
      email: "your_email@example.com"
      password: "your_password"
    response:
      message: "User registered successfully"
    notes: "Passwords longer than 72 bytes will be truncated automatically."

  login:
    method: POST
    path: "/login"
    headers:
      Content-Type: application/json
    request_body:
      email: "your_email@example.com"
      password: "your_password"
    response:
      access_token: "jwt_token_here"

testing:
  curl_examples:
    register: |
      curl -X POST "http://127.0.0.1:8002/register" \
      -H "Content-Type: application/json" \
      -d '{"username":"edu1","email":"edu1@example.com","password":"mypassword"}'
    login: |
      curl -X POST "http://127.0.0.1:8002/login" \
      -H "Content-Type: application/json" \
      -d '{"email":"edu1@example.com","password":"mypassword"}'

notes:
  - "JWT secret key is hardcoded (your_secret_key) for demo purposes. Use environment variables in production."
  - "SQLite is used for simplicity. Switch to MySQL/PostgreSQL for production."
  - "Passwords are hashed using bcrypt for security."

license:
  description: "This project is for educational purposes."
