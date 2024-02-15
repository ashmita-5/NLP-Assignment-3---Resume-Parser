from flask import Flask, render_template, request, send_file
import pickle

app = Flask(__name__)

# Route to upload PDF file
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            file_path = 'resume_entities.pkl'  # Path to the pickle file
            return render_template('index.html', file_uploaded=True)
    return render_template('index.html')

# Route to display extracted information
@app.route('/extracted_info', methods=['GET'])
def show_extracted_info():
    # Load extracted information from the pickle file
    with open('resume_entities.pkl', 'rb') as f:
        extracted_info = pickle.load(f)
    return render_template('index.html', extracted_info=extracted_info)

# Route to download extracted information as pickle file
@app.route('/download', methods=['GET'])
def download_file():
    return send_file('resume_entities.pkl', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)