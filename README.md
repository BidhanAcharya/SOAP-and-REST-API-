
# REST and SOAP API 

This project implements a simple calculator API using **FastAPI** (REST) and **Spyne** (SOAP). It provides endpoints to add two numbers using both REST and SOAP protocols.

---

## 📌 Features
- **REST API** using FastAPI for handling JSON requests.
- **SOAP API** using Spyne, integrated with FastAPI.
- **Input Validation** using Pydantic.
- **Modular Code Structure** for better maintainability.

---

## 🛠 Installation and Setup

### 1️⃣ Prerequisites
Ensure you have Python (>=3.8) installed along with `pip`.

### 2️⃣ Clone the Repository
```sh
git clone https://github.com/BidhanAcharya/SOAP-and-REST-API-.git
cd SOAP-and-REST-API-
```

### 3️⃣ Create and Activate a Virtual Environment
```sh
python -m venv venv
 On Windows use: venv\Scripts\activate
```

### 4️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

---

## 🚀 Running the Application

### Start FastAPI Server
```sh
uvicorn main:app --reload
```
The server will start at `http://127.0.0.1:8000`.

---

## 📡 REST API Usage
**Endpoint:**  
`POST http://127.0.0.1:8000/add_two_numbers`

**Request Body:**
```json
{
    "firstnumber": 5,
    "secondnumber": 3
}
```

**Response:**
```json
{
    "sum of two number is ": 8
}
```

---

## 🔗 SOAP API Usage
The SOAP service is available at:
```
http://127.0.0.1:8000/soap
```


## 📂 Project Structure
```
├── restapi.py        # FastAPI REST implementation
├── soapapi.py      # SOAP API implementation
├── schemas.py     # Pydantic schema for request validation
├── requirements.txt # List of dependencies
└── README.md      # Project documentation
```

---

## 📸 API Screenshots

### REST API Request and  Response

![Screenshot 2025-02-16 162949](https://github.com/user-attachments/assets/4c3e9e61-37cf-4da5-9bb1-64c8f5954c41)

### SOAP API Request and Response

![Screenshot 2025-02-16 164010](https://github.com/user-attachments/assets/e0ad53b2-7353-4dc6-9878-98245c9fb5e6)



---







