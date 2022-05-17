from flask import Flask,render_template,request
import os


PEOPLE_FOLDER = os.path.join('static', 'people_photo')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER


@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/products")
def product():
    return render_template("index.html")

@app.route("/start")
def start():

    full_filename = os.path.join('result.jpg')
    
    
    file = open(r'start.py', 'r').read()
    exec(file)
    return render_template("index.html", user_image = full_filename)
  
@app.route('/show') 
def show_index():
    file = open(r'start.py', 'r').read()
    exec(file)
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'result.jpg')
    return render_template("index.html", user_image = full_filename)
if __name__ == "__main__":
    app.run(debug=True)
