from flask import Flask, request, jsonify
import os
from werkzeug.utils import secure_filename
from PIL import Image as PilImage
import pytesseract
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskdb.db'
db = SQLAlchemy(app)
ma = Marshmallow(app)

UPLOAD_FOLDER = r'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)

class ImageSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Image

image_schema = ImageSchema()
images_schema = ImageSchema(many=True)

@app.route('/')
def home():
    return "Hi Tejal, You are the Best"

@app.route("/upload", methods=['POST'])
def upload_file():
    if 'files[]' not in request.files:
        return jsonify({"message": 'No file part in the request', "status": 'failed'}), 400

    files = request.files.getlist('files[]')
    errors = {}
    success = False

    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            new_file = Image(title=filename)
            db.session.add(new_file)
            db.session.commit()
            success = True
        else:
            return jsonify({"message": 'File type is not allowed', "status": 'failed'}), 400

    if success:
        return jsonify({"message": 'Files successfully uploaded', "status": 'success'}), 201
    else:
        return jsonify(errors), 500

@app.route('/images', methods=['GET'])
def images():
    all_images = Image.query.all()
    results = images_schema.dump(all_images)
    return jsonify(results)

@app.route('/convert/<int:image_id>', methods=['GET'])
def convert_image_to_text(image_id):
    image = Image.query.get_or_404(image_id)
    filename = image.title
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    if not os.path.exists(file_path):
        return jsonify({"message": "File not found", "status": "failed"}), 404

    try:
        document_text = extract_text_from_image(file_path)
        return jsonify({
            "message": "Text successfully extracted",
            "status": "success",
            "text": document_text
        }), 200
    except Exception as e:
        return jsonify({"message": str(e), "status": "failed"}), 500

def extract_text_from_image(file_path):
    # Ensure Tesseract executable path is correctly set
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    
    image = PilImage.open(file_path)
    text = pytesseract.image_to_string(image, lang='eng')
    return text

if __name__ == '__main__':
    app.run(debug=True)
