# Warehouse Inventory Management System

A simple, containerized full-stack web application for real-time inventory tracking. This project was developed as part of a hiring assignment and demonstrates clear thinking, clean structure, and an organized approach to building a practical business solution.

---

## 🚀 Overview

The **Warehouse Inventory Management System** helps track product quantities across locations with real-time updates. It provides:

- A dashboard for viewing inventories
- A mechanism to record stock movements (incoming/outgoing)
- Automatic low‑stock alerts
- Persistent storage using SQLite
- A fully containerized development environment

---

## ✨ Features

### **📊 Real-Time Dashboard**

- View all product quantities across warehouses
- Filter inventory by **product** or **location**

### **🔄 Transaction Logging**

- Submit **Incoming (stock‑in)** and **Outgoing (stock‑out)** entries
- Simple modal-based UI for quick actions

### **⚠️ Low Stock Alerts**

- Items at or below their threshold are automatically highlighted on the dashboard

### **💾 Persistent Storage**

- Uses a local database file: `/data/inventory.db`
- Keeps all inventory and transaction data intact between container restarts

### **🐳 Zero‑Setup Environment**

- Pre-configured using **VS Code Dev Containers**
- No manual installation of Python, Flask, or libraries

---

## 🛠️ Technology Stack

- **Backend:** Python (Flask)
- **Database:** SQLite
- **Frontend:** HTML, Tailwind CSS (CDN), Vanilla JavaScript
- **Environment:** Docker + VS Code Dev Containers

---

## ⚙️ How to Run (One‑Click Setup)

This project is configured to run seamlessly inside a VS Code Dev Container.

### **Prerequisites**

- Docker Desktop (running)
- Visual Studio Code
- VS Code extension: **Dev Containers** (Microsoft)

---

## ▶️ Running the Application

### **1. Open the Project**

Clone the repository and open the `inventory-app` folder in VS Code.

### **2. Reopen in Container**

VS Code will detect the `.devcontainer` folder and display a pop‑up.

- Click **Reopen in Container**

### **3. Wait for Setup**

VS Code will build the Docker image and install all dependencies automatically.

### **4. Run the App**

Open VS Code terminal (**Ctrl + \`**):

```
python app.py
```

### **5. View the Application**

Open your browser:\
[http://localhost:5000](http://localhost:5000)

---

## 📁 Project Structure

```
/inventory-app
├── .devcontainer/        # Dev Container configuration files
│   ├── devcontainer.json # Ports, extensions, environment
│   └── Dockerfile        # Base container + tool installations
├── data/                 # Persistent SQLite database
│   └── inventory.db      # Auto-created on first run
├── templates/
│   └── index.html        # Main frontend file
├── app.py                # Flask backend (API + DB logic)
└── requirements.txt      # Python dependencies
```

---

## 🧩 API Endpoints

### **GET /**

Serves the main frontend page.

### **GET /api/dashboard**

Returns:

- Inventory list
- Product details
- Location details

### **POST /api/transaction**

Handles stock movement submissions:

- Validates data
- Updates inventory tables
- Logs the transaction

---

## 📌 Notes

- No external database or manual setup required
- All logic is cleanly separated between UI, API, and DB layers
- Designed to reflect real-world warehouse workflow

---

## 📝 License

This project is part of a hiring assignment and intended for demonstration purposes.



