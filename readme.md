Warehouse Inventory Management System

A simple, containerized web application for real-time inventory tracking. This project is a solution to the hiring assignment, demonstrating a full-stack, containerized approach to solving a real-world business problem.

Features

Real-time Dashboard: View all inventory levels, filterable by product and location.

Transaction Logging: Record "Incoming" (stock-in) and "Outgoing" (stock-out) transactions through a simple modal.

Low Stock Alerts: The dashboard automatically highlights items that have fallen at or below their pre-defined stock threshold.

Persistent Storage: All data is saved in a local SQLite database file (/data/inventory.db).

Zero-Setup Environment: The entire project runs inside a pre-configured Docker container using VS Code Dev Containers.

Technology Stack

Backend: Python (Flask)

Database: SQLite

Frontend: HTML, Tailwind CSS (via CDN), and Vanilla JavaScript

Environment: Docker & VS Code Dev Containers

How to Run (One-Click Setup)

This project is configured to run in a Dev Container, which sets up the entire environment for you automatically.

Prerequisites

Docker Desktop: Must be installed and running.

VS Code: Must be installed.

VS Code Extension: The Dev Containers extension (by Microsoft) must be installed.

Running the Application

Open the Project: Clone this repository and open the inventory-app folder in VS Code.

Reopen in Container: VS Code will automatically detect the .devcontainer folder and show a pop-up in the bottom-right corner. Click "Reopen in Container".

Wait: The first time you do this, VS Code will build the Docker image and install all dependencies (like Flask) automatically. This may take a minute or two.

Run the App: Once the container is running, open the VS Code Integrated Terminal (`Ctrl+``). It will now be a terminal inside the container. Run the application:

python app.py


View the App: The application will be running. Open your browser and go to:

http://localhost:5000

Project Structure

/inventory-app
├── .devcontainer/        # Dev Container configuration
│   ├── devcontainer.json # Defines the container (ports, extensions)
│   └── Dockerfile        # Defines the OS and tools to install
├── data/                 # Holds the persistent SQLite DB
│   └── inventory.db      # (This file is created on first run)
├── templates/
│   └── index.html        # The main HTML/JS/CSS frontend
├── app.py                # The Flask backend (API + DB logic)
└── requirements.txt      # Python dependencies


API Endpoints

The Flask server provides the following endpoints:

GET /: Serves the index.html frontend.

GET /api/dashboard: Fetches all data (inventory list, products, locations) needed to render the dashboard.

POST /api/transaction: Submits a new stock movement. The server handles all logic for updating quantities and logging the transaction.