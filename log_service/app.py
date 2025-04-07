from flask import Flask, request, jsonify
from logger import write_log

app = Flask(__name__)

@app.route('/log', methods=['POST'])
def log_event():
    data = request.json
    event = data.get("event")
    if not event:
        return jsonify({"error": "Missing event message"}), 400
    write_log(event)
    return jsonify({"message": "Event logged"}), 200

if __name__ == '__main__':
    app.run(port=5002, debug=True)
