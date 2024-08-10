'''
#All in one - 
from flask import Flask
import PyPDF2

app = Flask(__name__)

@app.route('/')
def home():
    return "Hi Tejal, You are the Best"

#frog_book = 'C:/Users/tejal/OneDrive/Desktop/Project_git/Prescription/Backend/Eat-That-Frog.pdf'

@app.route('/convert')
def PDF_to_text():
    reader = PyPDF2.PdfReader('C:/Users/tejal/OneDrive/Desktop/Project_git/Prescription/Backend/Syllabus.pdf')
    str = ''
    for page in reader.pages:
        str += page.extract_text()
    
    #with open("text2_server.txt", "w", encoding='utf-8') as f:
    #    f.write(str)
    return str

#if __name__ == "__main__":
app.run(debug=True)
'''

from flask import Flask, json, request, jsonify
import os
import urllib.request
from werkzeug.utils import secure_filename #pip install Werkzeug
from flask_cors import CORS #ModuleNotFoundError: No module named 'flask_cors' = pip install Flask-Cors
from flask_marshmallow import Marshmallow #ModuleNotFoundError: No module named 'flask_marshmallow' = pip install flask-marshmallow https://pypi.org/project/flask-marshmallow/
 
from models import db, Image
 
app = Flask(__name__)
CORS(app, supports_credentials=True)
 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskdb.db'
# Databse configuration mysql                             Username:password@hostname/databasename
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:''@localhost/flaskreact'
 
db.init_app(app)
  
with app.app_context():
    db.create_all()
 
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
 
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
 
ma=Marshmallow(app)
 
class ImageSchema(ma.Schema):
    class Meta:
        fields = ('id','title')
         
image_schema = ImageSchema(many=True)
 
@app.route("/")
def hello_world():
    return "Hello, World!"
 
@app.route('/upload', methods=['POST'])
def upload_file():
    # check if the post request has the file part
    if 'files[]' not in request.files:
        resp = jsonify({
            "message": 'No file part in the request',
            "status": 'failed'
        })
        resp.status_code = 400
        return resp
  
    files = request.files.getlist('files[]')
      
    errors = {}
    success = False
      
    for file in files:      
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
 
            newFile = Image(title=filename)
            db.session.add(newFile)
            db.session.commit()
 
            success = True
        else:
            resp = jsonify({
                "message": 'File type is not allowed',
                "status": 'failed'
            })
            return resp
         
    if success and errors:
        errors['message'] = 'File(s) successfully uploaded'
        errors['status'] = 'failed'
        resp = jsonify(errors)
        resp.status_code = 500
        return resp
    if success:
        resp = jsonify({
            "message": 'Files successfully uploaded',
            "status": 'successs'
        })
        resp.status_code = 201
        return resp
    else:
        resp = jsonify(errors)
        resp.status_code = 500
        return resp
     
@app.route('/images',methods =['GET'])
def images():
    all_images = Image.query.all()
    results = image_schema.dump(all_images)
    return jsonify(results)