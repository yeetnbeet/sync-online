import os
from flask import Flask, flash, request, redirect, url_for, render_template, send_from_directory 
from werkzeug.utils import secure_filename
from helpers import create_output

UPLOAD_FOLDER = './files'
ALLOWED_EXTENSIONS = {'csv'}


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "ghasdfalskdjhfaklsdf"

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        if 'file2' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        file2 = request.files['file2']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == ''or file2.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and file2 and allowed_file(file.filename) and allowed_file(file2.filename):
            filename = secure_filename(file.filename)
            filename2 = secure_filename(file2.filename)
            path1 = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            path2 = os.path.join(app.config['UPLOAD_FOLDER'], filename2)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file2.save((os.path.join(app.config['UPLOAD_FOLDER'], filename2)))
            create_output(path1,path2)
            return redirect(url_for('download_file', name="OUTPUT.csv"))
    return render_template("index.html")

@app.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8000))
    app.run(debug=True, host='0.0.0.0', port=port)