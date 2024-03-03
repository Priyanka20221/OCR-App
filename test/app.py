from flask import Flask, render_template, request
from PIL import Image
import pytesseract

app = Flask(__name__)

# Set the Tesseract OCR path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            return render_template('index.html', error='No file part')

        file = request.files['file']

        # Check if the file is empty
        if file.filename == '':
            return render_template('index.html', error='No selected file')

        # Check if the file is an allowed extension
        if file:
            image = Image.open(file)
            extracted_text = pytesseract.image_to_string(image)

            return render_template('index.html', extracted_text=extracted_text)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
