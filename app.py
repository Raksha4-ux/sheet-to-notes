from flask import Flask, request, jsonify, render_template
import xml.etree.ElementTree as ET
import subprocess
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["sheet"]
    input_path = os.path.join(BASE_DIR, "uploaded.png")
    output_path = os.path.join(BASE_DIR, "uploaded.musicxml")

    file.save(input_path)

    result = subprocess.run(
        ["oemer", "uploaded.png"],
        cwd=BASE_DIR,
        capture_output=True,
        text=True
    )

    if not os.path.exists(output_path):
        return jsonify({"error": "oemer failed to process image", "detail": result.stderr}), 500

    tree = ET.parse(output_path)
    root = tree.getroot()

    measures = []

    for measure in root.iter("measure"):
        measure_notes = []
        for note in measure.iter("note"):
            if note.find("rest") is not None:
                continue
            staff = note.find("staff")
            if staff is not None and staff.text != "1":
                continue
            pitch = note.find("pitch")
            if pitch is not None:
                measure_notes.append(pitch.find("step").text)
        if measure_notes:
            measures.append(measure_notes)

    return jsonify({"measures": measures})

if __name__ == "__main__":
    app.run(debug=True)
