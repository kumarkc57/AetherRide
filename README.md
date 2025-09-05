
## Team Members

- Kumar K C
- Ayush Gowda. P
- Yagnesh. L 

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

## ⚙️ Setup Instructions

###
1️⃣ Clone Repository
```
git clone https://github.com/kumrkc57/AetherRide.git
cd AetherRide

2️⃣ Setup Server
Navigate to the server folder:
cd server

Install dependencies:
pip install flask


Run the server:
python server.py

Server starts at:
cpp
http://127.0.0.1:5000


3️⃣ Setup Client
Open a new terminal and navigate to the client folder:
cd client

Install dependencies:
pip install requests

Run the client:
python client.py

📌 API Endpoint
POST /ride-request
Request Body:

json

{
  "source_location": "Bangalore",
  "dest_location": "Mysore",
  "user_id": "user123"
}
Response Body:

json

{
  "status": "success",
  "message": "Ride request received (database integration pending)",
  "data": {
    "source_location": "Bangalore",
    "dest_location": "Mysore",
    "user_id": "user123"
  }
}
