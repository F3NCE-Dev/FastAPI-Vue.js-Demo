# FastAPI + Vue.js Demo

A demonstration of connecting FastAPI with Vue.js.

The app fetches dynamic text from an API and displays it in a styled UI with automatic updates.

## Local installation

### Prerequisites

- Python 3.11+
- Node.js
- Git
- Docker (optional, recommended)

## Step 1: Clone the repository

```bash
git clone https://github.com/F3NCE-Dev/FastAPI-Vue.js-Demo.git
cd FastAPI-Vue.js-Demo
```

## Step 2: Install dependencies

- **Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate # Linux/Mac
# or
venv/Scripts/activate # Windows

```

- **Install requirements**

```bash
pip install -r requirements.txt
```

## Step 3: Create a backend .env file (optional)

```bash
cd backend
echo "" > .env
```

Fill it with the required environment variables

Example:

```env
FRONTEND_ORIGINS=["your", "origins"]
DEBUG_MODE=true
```

## Step 4: Create a frontend .env file (optional, required for Docker)

```bash
cd frontend
echo "" > .env
```

Fill it with the API base URL (Variables must start with `VITE_`):

```env
VITE_API_BASE_URL=api_url
```

## Running the Application

### Option 1: Run with Docker (Recommended)

- **Make sure Docker is installed and running**

```bash
docker-compose up --build
```

### Access the application (Default params)

- Frontend (Vue + Vite): http://localhost
- Backend (via Nginx): http://localhost/api

### Option 2: Run locally (Development)

#### Run the backend

- **Open new terminal and run**

```bash
cd backend
python run.py
```

#### Run the frontend

- **Open new terminal and run**

```bash
cd frontend
npm run dev
```

### Access the application (Default params)

- Frontend (Vue + Vite): http://localhost:5173
- Backend (FastAPI): http://localhost:8000

## Technologies used

### Backend

- **FastAPI**
- **Pydantic**
- **SQLAlchemy**
- **alembic**
- **aiosqlite**
- **Uvicorn**

### Frontend

- **Vue 3**
- **Vue router**
- **Vite**
- **Tailwind CSS**
- **Axios**

### DevOps

- **Docker**
- **Docker Compose**
- **Nginx (Reverse Proxy)**
