from backend import app
from backend.utils import allowed_file
from flask import request, flash, redirect,send_file,url_for
from backend import model
from io import BytesIO
import matplotlib.pyplot as plt
from flask import render_template

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload',methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No file Part')
        return redirect(url_for('home'))
    file=request.files['file']
    if file.filename=='':
        flash('No selected file')
        return redirect(url_for('home'))
    if file and allowed_file(file.filename):
        k = int(request.form.get('k', 16))
        file_comprr=model.base(file,k=k)
        img_io=BytesIO()
        plt.imsave(img_io,file_comprr,format='png')
        img_io.seek(0)
        return send_file(img_io,mimetype='image/png')