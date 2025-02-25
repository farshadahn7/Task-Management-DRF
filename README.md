# Task Management API with Django REST Framework (DRF)

This is a Task Management API built using Django REST Framework (DRF). It allows users to create, manage, and organize tasks efficiently. The API provides endpoints for user authentication, task creation, updating, deletion, and more.

## Features

- **User Authentication**: Secure user registration and login using tokens.
- **Database**: Uses PostgreSQL.
- **Task Management**: Create, retrieve, update, and delete tasks.
- **Task status**: (pending, in progress, completed)
- **Filtering and Searching**: Filter tasks by (status and due date) and search tasks by (title)
- **API Documentation**: Detailed API documentation using Swagger.
- **RESTful API**: Follows REST principles for easy integration with frontend applications.

## Technologies Used

- **Django REST Framework (DRF)**: A powerful and flexible toolkit for building Web APIs.
- **Simple JWT**: For token-based authentication.
- **Redis**: As a messege Broker.
- **Celery**: worker for sending verification email task.
- **Docker**: Project is dockerized 
  
## Installation

### Prerequisites

- Python 3.8 or higher
- Django 4.2 or higher
- Django REST Framework 3.15 (DRF)
- PostgreSQL
- Docker

Follow these steps to set up the project locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/farshadahn7/Task-Management-DRF.git
   cd Task-Management-DRF
   
2. **Create a virtual environment**:
   ```bash
    python -m venv venv
    source venv/bin/activate # On Windows: venv\Scripts\activate

3. **Configure .env.exmple**:
  - Configure the postgres variables such as user,password and so on.
4. **Run docker command**:
    ```bash
    docker compose up --build
