import requests

def send_ride_request():
    url = "http://127.0.0.1:5000/ride-request"  # match server endpoint
    payload = {
        "source_location": "Bangalore",
        "dest_location": "Mysore",
        "user_id": 101
    }
    try:
        response = requests.post(url, json=payload)
        print("Server response:", response.json())
    except Exception as e:
        print("Error communicating with server:", e)

if __name__ == "__main__":
    send_ride_request()
