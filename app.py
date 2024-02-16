from flask import Flask, render_template, request, send_file
import os
from utils import readPDF

app = Flask(__name__)

# Route for the file upload page
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = file.filename
            file_path = os.path.join('uploads', filename)
            file.save(file_path)
            extracted_info = readPDF(file_path)
            return render_template('index.html', extracted_info=extracted_info)
    return render_template('index.html', extracted_info=None)

# Route to download extracted information as a CSV file
@app.route('/download', methods=['POST'])
def download_file():
    extracted_info = request.form.to_dict()
    # Save extracted_info as CSV
    return send_file('extracted_info.csv', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)