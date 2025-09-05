# 🚖 AetherRide

AetherRide is a simple client-server project that demonstrates how ride requests can be sent from a **client** to a **server** using Python.  
The **server** is built with Flask, while the **client** uses the `requests` library.

---

## 🚀 Features
- REST API backend with Flask  
- Client sends JSON ride requests  
- Server responds with structured JSON  
- Clean modular structure (separate client and server folders)  

---

## 📂 Project Structure
AetherRide/
│── server/
│ ├── server.py # Flask backend
│ └── README.md # (optional, for server-specific docs)
│
│── client/
│ ├── client.py # Client script
│ └── README.md # (optional, for client-specific docs)
│
└── README.md # Main documentation

yaml
Copy code

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository
```bash
git clone https://github.com/your-username/AetherRide.git
cd AetherRide
2️⃣ Setup Server
Navigate to the server folder:

bash
Copy code
cd server
Install dependencies:

bash
Copy code
pip install flask
Run the server:

bash
Copy code
python server.py
Server starts at:

cpp
Copy code
http://127.0.0.1:5000
3️⃣ Setup Client
Open a new terminal and navigate to the client folder:

bash
Copy code
cd client
Install dependencies:

bash
Copy code
pip install requests
Run the client:

bash
Copy code
python client.py
📌 API Endpoint
POST /ride-request
Request Body:

json
Copy code
{
  "source_location": "Bangalore",
  "dest_location": "Mysore",
  "user_id": "user123"
}
Response Body:

json
Copy code
{
  "status": "success",
  "message": "Ride request received (database integration pending)",
  "data": {
    "source_location": "Bangalore",
    "dest_location": "Mysore",
    "user_id": "user123"
  }
}
