📒 Daftar — Task Manager API
A full-featured Task Manager backend built with FastAPI, offering task management with due date support, image uploads, and AI-powered task planning.
✨ Features
🔐 Full JWT Authentication (Signup / Login / Protected Routes)
✅ Complete task CRUD (Create, Read, Update, Delete)
📅 Due Date support with dedicated endpoints for Overdue and Upcoming tasks
🖼️ Image upload attached to tasks
🤖 AI-Powered Task Planning — automatically suggests and organizes tasks using the Gemini API
🗄️ Multi-database support (SQLite for development / PostgreSQL for production) via SQLAlchemy ORM
🛠️ Tech Stack
Technology
Purpose
FastAPI
Backend framework
SQLAlchemy
ORM for database interaction
Pydantic
Data validation & schemas
PostgreSQL / SQLite
Database
JWT (python-jose)
Authentication & authorization
Anthropic API
AI task planning

📂 Project Structure
Code
Approximate structure — update it to match your actual project layout.
⚙️ Local Setup
1. Clone the project
Bash
2. Create a virtual environment
Bash
3. Install dependencies
Bash
4. Set up environment variables
Copy .env.example to .env and fill in the real values:
Code
5. Run the server
Bash
The server will run at: http://127.0.0.1:8000
Interactive docs (Swagger UI): http://127.0.0.1:8000/docs
📡 API Endpoints
🔐 Authentication
Method
Endpoint
Description
POST
/auth/signup
Create a new account
POST
/auth/login
Log in and receive a token
✅ Tasks
Method
Endpoint
Description
GET
/tasks/
List all tasks
POST
/tasks/
Create a new task
GET
/tasks/{id}
Get a specific task
PUT
/tasks/{id}
Update a task
DELETE
/tasks/{id}
Delete a task
GET
/tasks/overdue
Get overdue tasks
GET
/tasks/upcoming
Get upcoming tasks
POST
/tasks/{id}/image
Upload an image attached to a task
🤖 AI Planning
Method
Endpoint
Description
POST
/ai/plan
Generate a smart task plan using AI
Update this table to exactly match your actual routes.

👤 Author
Essam Waleed
backend developer- python developer(fastapi - django )
Business Information Systems student — Tanta University
Creates Arabic programming content on YouTube and TikTok
GitHub
📄 License
This project is open source for educational purposes. Feel free to use and modify it.
