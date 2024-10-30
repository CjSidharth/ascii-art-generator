from flask import Flask, render_template, request, redirect, url_for
from ascii_converter import convert_to_ascii 
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "file" not in request.files:
            return redirect(request.url)
        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            ascii_art = convert_to_ascii(filepath) 
            return render_template("index.html", ascii_art=ascii_art)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
