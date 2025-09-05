from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/ride-request", methods=["POST"])
def ride_request():
    data = request.get_json()

    source = data.get("source_location")
    dest = data.get("dest_location")
    user_id = data.get("user_id")

    print("We will store this data in Postgres now:", data)

    return jsonify({
        "status": "success",
        "message": "Ride request received (Postgres integration pending)",
        "data": data
    })

if __name__ == "__main__":
    app.run(debug=True)
