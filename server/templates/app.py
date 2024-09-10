from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data storage
buyers = [
    {"name": "John Doe", "device_id": "device123", "status": "active", "payload": "http://www.venvokjr.xyz/info/device123"},
    # Add more sample data as needed
]

@app.route('/')
def index():
    return render_template('index.html', buyers=buyers)

@app.route('/add_buyer', methods=['POST'])
def add_buyer():
    name = request.form['name']
    device_id = request.form['device_id']
    payload = request.form['payload']
    buyers.append({"name": name, "device_id": device_id, "status": "active", "payload": payload})
    return redirect(url_for('index'))

@app.route('/remove_buyer/<device_id>', methods=['POST'])
def remove_buyer(device_id):
    global buyers
    buyers = [buyer for buyer in buyers if buyer['device_id'] != device_id]
    return redirect(url_for('index'))

@app.route('/update_status', methods=['POST'])
def update_status():
    device_id = request.form['device_id']
    status = request.form['status']
    for buyer in buyers:
        if buyer['device_id'] == device_id:
            buyer['status'] = status
            break
    return redirect(url_for('index'))

@app.route('/generate_payload', methods=['POST'])
def generate_payload():
    device_id = request.form['device_id']
    # Generate a new payload for the given device_id
    new_payload = f"http://www.venvokjr.xyz/info/{device_id}"
    for buyer in buyers:
        if buyer['device_id'] == device_id:
            buyer['payload'] = new_payload
            break
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
