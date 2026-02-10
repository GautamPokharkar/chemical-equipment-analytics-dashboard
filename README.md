Chem-Equipment Analytics

Web & Desktop Data Visualization Tool

Overview

Chem-Equipment Analytics is a hybrid web + desktop application for analyzing chemical equipment data from CSV files.
It uses a shared Django REST API to process data and deliver analytics to both a React web dashboard and a PyQt5 desktop app.

Tech Stack

Backend: Django, Django REST Framework, Pandas, SQLite

Web: React, Axios, Chart.js

Desktop: PyQt5, Matplotlib

Features

CSV upload (Web & Desktop)

Equipment statistics and averages

Equipment type distribution

Interactive charts (Web)

Native plots (Desktop)

PDF report generation

Shared backend API for both clients

Project Structure
chem-equipment-analytics/
├── backend/    # Django API
├── frontend/   # React app
├── desktop/    # PyQt5 app
└── README.md

Sample CSV
Equipment Name,Type,Flowrate,Pressure,Temperature
Pump-1,Pump,120,5.2,110

Run Instructions
Backend
cd backend
python manage.py migrate
python manage.py runserver

Web App
cd frontend
npm install
npm start

Desktop App
cd desktop
python main.py

API

POST /api/upload/ – Upload CSV

GET /api/report/ – Download PDF report

Status

UI improvements in progress

Authentication planned
