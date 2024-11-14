import os
import openai
import base64
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
from openai import OpenAI

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Initialize the OpenAI client with your API key
client = OpenAI(api_key=os.environ.get('OPENAI_KEY'))  # replace with your actual OpenAI API key

# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def encode_image_to_base64(image_path):
    """Encode the image file as a base64 string."""
    with open(image_path, "rb") as image_file:
        base64_image = base64.b64encode(image_file.read()).decode("utf-8")
    return base64_image

def process_image_with_openai(base64_image):
    """Use OpenAI API to process the base64-encoded image with gpt-4-vision model."""
    prompt = (
        "Extract and format details from this Indonesian KTP data in the image. "
        "Format it in JSON with fields: Province, City, NIK, Name, BirthPlace, BirthDate, Gender, BloodType, "
        "Address, RT/RW, Village, District, Religion, MaritalStatus, Occupation, Nationality, ValidUntil."
        "Do not wrap the json codes in JSON markers"
    )

    # response = client.chat.completions.create(
    #     model="gpt-4-turbo",
    #     messages=[{"role": "user", "content": prompt}],
    #     files=[{"file": base64_image, "file_type": "image"}],
    #     max_tokens=300,
    #     temperature=0
    # )

    response = client.chat.completions.create(
      model="gpt-4o-mini",
      messages=[
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": prompt,
            },
            {
              "type": "image_url",
              "image_url": {
                "url":  "data:image/jpeg;base64," + base64_image
              },
            },
          ],
        }
      ],
    )

    print(response)
    details = response.choices[0].message.content #.strip()
    print(details)
    return details

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    # Save the uploaded file
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    # Encode the image as base64
    base64_image = encode_image_to_base64(filepath)

    # Process the image with OpenAI API
    details = process_image_with_openai(base64_image)
    
    # Return extracted details as JSON
    return jsonify({'details': details})
    # return(details)

if __name__ == '__main__':
    app.run(debug=True, port=8000)

