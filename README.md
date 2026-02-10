# Chem-Equipment Analytics  
**Web & Desktop Data Visualization Tool**

## Overview
**Chem-Equipment Analytics** is a hybrid **web and desktop application** for analyzing chemical equipment data from CSV files.  
A shared **Django REST API** processes the data and serves analytics to both a **React web dashboard** and a **PyQt5 desktop application**.

---

## Tech Stack
- **Backend:** Django, Django REST Framework, Pandas, SQLite  
- **Web:** React, Axios, Chart.js  
- **Desktop:** PyQt5, Matplotlib  

---

## Features
- CSV upload (Web & Desktop)
- Equipment summary statistics
- Equipment type distribution
- Interactive charts (Web)
- Native plots (Desktop)
- PDF report generation
- Single backend API for both clients

---

## Project Structure
# Chem-Equipment Analytics  
**Web & Desktop Data Visualization Tool**

## Overview
**Chem-Equipment Analytics** is a hybrid **web and desktop application** for analyzing chemical equipment data from CSV files.  
A shared **Django REST API** processes the data and serves analytics to both a **React web dashboard** and a **PyQt5 desktop application**.

---

## Tech Stack
- **Backend:** Django, Django REST Framework, Pandas, SQLite  
- **Web:** React, Axios, Chart.js  
- **Desktop:** PyQt5, Matplotlib  

---

## Features
- CSV upload (Web & Desktop)
- Equipment summary statistics
- Equipment type distribution
- Interactive charts (Web)
- Native plots (Desktop)
- PDF report generation
- Single backend API for both clients

---

## Project Structure
chem-equipment-analytics/
├── backend/ # Django API
├── frontend/ # React app
├── desktop/ # PyQt5 app
└── README.md

---

## Sample CSV
Equipment Name,Type,Flowrate,Pressure,Temperature
Pump-1,Pump,120,5.2,110


---

## Run Instructions

### Backend
``bash
cd backend
python manage.py migrate
python manage.py runserver
Web Application
cd frontend
npm install
npm start
Desktop Application
cd desktop
python main.py
API Endpoints
POST /api/upload/ – Upload CSV

GET /api/report/ – Download PDF report

Status
UI improvements in progress

Authentication planned
