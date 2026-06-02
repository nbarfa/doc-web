# doc-web

# Doc-Web

A Flask-based web application with PostgreSQL database integration, containerized using Docker and deployed automatically through a Jenkins CI/CD pipeline.

## Features

* Create and manage records through REST APIs
* PostgreSQL database integration
* Flask backend application
* Docker containerization
* Docker Compose for multi-container management
* Automated CI/CD using Jenkins
* GitHub Webhook integration
* Automatic Docker Hub image publishing
* Automatic deployment after every GitHub push

---

## Tech Stack

* Python 3.12
* Flask
* Flask-SQLAlchemy
* PostgreSQL
* Docker
* Docker Compose
* Jenkins
* GitHub
* Docker Hub

---

## Project Structure

```text
Doc-Web/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── Jenkinsfile
└── README.md
```

---

## Running Locally

### Clone Repository

```bash
git clone https://github.com/nbarfa/doc-web.git
cd doc-web
```

### Start Containers

```bash
docker compose up -d
```

### Access Application

```text
http://localhost:8000
```

---

## Docker Image

Build image manually:

```bash
docker build -t nitin260/doc-web:latest .
```

Run container:

```bash
docker run -p 8000:8000 nitin260/doc-web:latest
```

---

## CI/CD Pipeline

The project uses Jenkins for Continuous Integration and Continuous Deployment.

Pipeline Workflow:

1. Developer pushes code to GitHub.
2. GitHub Webhook triggers Jenkins automatically.
3. Jenkins checks out the latest code.
4. Docker image is built.
5. Jenkins logs in to Docker Hub.
6. Image is pushed to Docker Hub.
7. Docker Compose pulls the latest image.
8. Application is redeployed automatically.

```text
GitHub Push
      ↓
GitHub Webhook
      ↓
Jenkins Pipeline
      ↓
Docker Build
      ↓
Docker Hub Push
      ↓
Docker Compose Deploy
      ↓
Updated Application
```

---

## Jenkins Stages

### Build Docker Image

Builds the latest application image.

### Docker Login

Authenticates with Docker Hub using Jenkins credentials.

### Push Image

Pushes the latest image to Docker Hub.

### Deploy

Pulls the latest image and redeploys containers using Docker Compose.

---

## Docker Hub Repository

```text
nitin260/doc-web
```

---

## Author

Nitin Barfa

Built as a hands-on Full Stack learning project demonstrating Docker containerization and automated CI/CD deployment using Jenkins.
