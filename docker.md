# 🐳 Docker Guide for `taskweb`

This guide will help you containerize the `taskweb` Flask app using Docker. We'll explain what Docker is, why it's useful, and how to set everything up step-by-step.

---

## 🚀 What is Docker?

Docker is a tool that lets you **package your application and its dependencies into a portable container**.

- Think of a container like a lightweight virtual machine.
- It includes your code, Python, Flask, SQLite, and everything your app needs.
- Once it's in a container, it will **run the same way** on any machine.

---

## 📦 What is a Container?

A container is:
- Isolated from your system
- Lightweight (shares your OS kernel)
- Fast to start and stop
- Easy to reproduce on any machine or server

If you’ve ever heard "it works on my machine," Docker solves that problem.

---

## 🛠️ Prerequisites

Before continuing:
1. Install [Docker Desktop](https://www.docker.com/products/docker-desktop) for your OS
2. Open a terminal and run:

   ```bash
   docker --version
   ```

   You should see something like: `Docker version 24.x.x, build abc123`

---

## 📁 File Structure

Make sure your project directory looks something like this:

```
taskweb/
├── app.py
├── templates/
├── static/
├── db_schema.sql
├── requirements.txt
└── Dockerfile       ← we'll add this
```

> You can generate `requirements.txt` by running:
> ```bash
> pip freeze > requirements.txt
> ```

---

## 🧾 Dockerfile

Create a file named `Dockerfile` in the root of the `taskweb` directory:

```Dockerfile
# Use the official lightweight Python image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy everything from current dir to the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port that Flask runs on
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
```

---

## 🧪 Running It with Docker

### 1. Build the Docker Image

From your `taskweb/` directory:

```bash
docker build -t taskweb .
```

This will:
- Read the Dockerfile
- Install Python and dependencies
- Package your app into an image called `taskweb`

### 2. Run the Container

```bash
docker run -p 5000:5000 taskweb
```

Now visit [http://localhost:5000](http://localhost:5000) in your browser.

You’re running `taskweb` inside a container!

---

## 🧹 Stopping and Cleaning Up

To stop the container, hit `Ctrl+C`.

To see all containers (even stopped ones):

```bash
docker ps -a
```

To delete a container:

```bash
docker rm <container_id>
```

To delete the image:

```bash
docker rmi taskweb
```

---

## 🧰 Bonus: docker-compose (Optional)

If you later add a PostgreSQL or Redis backend, you’ll want to use `docker-compose`. It lets you run multiple containers together.

---

## ✅ Summary

- Docker lets you package and run apps in a portable, consistent environment.
- Containers are like lightweight, disposable virtual machines.
- With just a few files, you made `taskweb` deployable anywhere — no setup required.

You’re now one step closer to production-grade deployment! 🚀
