import os
from flask import Flask, request
from fastbook import *

# Ensure proper image formats
valid_extensions = {"jpg", "jpeg", "png"}

path = Path("uploads")

if not path.exists():
    path.mkdir()

uploads = "uploads"


app = Flask(__name__)
app.config["uploads"] = uploads
learner = load_learner("model.pkl")

def valid_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in valid_extensions

@app.route("/status")
def status():
    return {"success": "Server is running"}, 200

@app.route("/classify", methods = ["POST"])
def classify():
    if "image" not in request.files:
        return {"error": "No image found"}, 400
    
    file = request.files["image"]
    if file.filename == "":
        return {"error": "No image found."}, 400

    if file and valid_file(file.filename):
        filename = file.filename
        filepath = os.path.join(app.config["uploads"], filename)
        file.save(filepath)
        classification = learner.predict(filepath)
        return {"success": classification[0]}, 200
    
    return {"error": "Something went wrong"}, 500

if __name__ == '__main__':
    port = os.getenv('PORT',5000)
    app.run(debug=True, host='0.0.0.0', port=port)




