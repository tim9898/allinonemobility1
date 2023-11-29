from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Beispiel-Daten
mobility_data = {
    "locations": ["Ort A", "Ort B", "Ort C"],
    "fahrzeuge": ["Auto", "Fahrrad", "Elektroroller"]
}

# Routen
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/locations', methods=['GET'])
def get_locations():
    return jsonify(mobility_data['locations'])

@app.route('/vehicles', methods=['GET'])
def get_vehicles():
    return jsonify(mobility_data['fahrzeuge'])

if __name__ == '__main__':
    app.run(debug=True)
