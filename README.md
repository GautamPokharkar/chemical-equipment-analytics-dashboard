# Chemical Equipment Parameter Visualizer  
**Hybrid Web + Desktop Application**

##  Project Overview
The **Chemical Equipment Parameter Visualizer** is a hybrid application that runs as both a **Web Application** and a **Desktop Application**.  
It allows users to upload a CSV file containing chemical equipment data, performs analytics using a common Django backend, and visualizes the results through interactive charts and summaries.

Both frontends (React Web and PyQt5 Desktop) consume the **same backend API endpoint**, ensuring consistency across platforms.

---

##  Tech Stack

### Backend
- **Python Django**
- **Django REST Framework**
- **Pandas** (CSV parsing & analytics)
- **SQLite** (store last 5 uploaded datasets)

### Frontend (Web)
- **React.js**
- **Axios**
- **Chart.js**
  
![Web Frontend](imagereact.png)

### Frontend (Desktop)
- **PyQt5**
- **Matplotlib**
- **Requests**
  
![Desktop Frontend](imagepyqt5.png)


---

## Project Structure

```
ChemEquipmentsVisualizer/
│
├── backend/ # Django REST API
│ ├── backend/
│ ├── equipment/
│ └── manage.py
│
├── frontend/ # React Web App
│ └── src/
│
├── desktop/ # PyQt5 Desktop App
│ └── main.py
│
└── README.md
```


---

##  Key Features

-  **CSV Upload** (Web & Desktop)
-  **Data Analytics** using Pandas
-  **Visualization**
    - Chart.js (Web)
    - Matplotlib (Desktop)
-  **Summary Statistics**
    - Total equipment count
    - Average flowrate, pressure, temperature
    - Equipment type distribution
-  **PDF Generation**
    - Download the statistics to user's local storage from common backend Api in the form of PDF 
-  **History Management**
    - Stores last 5 uploaded datasets
-  **Shared Backend Pipeline**
    - One API endpoint used by both clients

---

##  Sample CSV Format

```
Equipment Name	Type	Flowrate	Pressure	Temperature
Pump-1	Pump	120	5.2	110
Compressor-1	Compressor	95	8.4	95

```


---

##  Setup Instructions

### 1 Backend (Django API)

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

#### Backend runs at:
```
http://127.0.0.1:8000
```

#### API Endpoint:
```
POST /api/upload/
```
#### Download PDF Report
- **Method:** GET  
- **Endpoint:** `/api/report/`  
- **Description:** Returns a PDF report containing summary statistics and equipment type distribution for the most recently uploaded dataset.

### 2 Frontend (React)
```
cd frontend
npm install
npm start
```

Web app runs at:
```
http://localhost:3000
```

### 3 Desktop App (PyQt5)
```
cd desktop
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python main.py
```
## API Details
- Upload CSV
- Method: POST
- Endpoint: /api/upload/
- Payload: form-data (file: CSV file)

### Response (JSON):
```
{
  "total": 10,
  "avg_flowrate": 9.4,
  "avg_pressure": 2.8,
  "avg_temperature": 72.1,
  "type_distribution": {
    "Pump": 4,
    "Valve": 3,
    "Tank": 3
  }
}
```
## Currently Working on 

- Enhanced UI styling
- Authentication (login)
- Deployment of web version


