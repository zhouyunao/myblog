from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_simplemde import SimpleMDE
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/ingo/Documents/myblog/blog.db'
# app.config['SIMPLEMDE_JS_IIFE'] = True
# app.config['SIMPLEMDE_USE_CDN'] = True
SimpleMDE(app)
db = SQLAlchemy(app)


class Blogpost(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(50))
    subtitle = db.Column(db.String(50))
    author = db.Column(db.String(20))
    date_posted = db.Column(db.DateTime)
    content = db.Column(db.Text)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/post')
def post():
    return render_template('post.html')

@app.route('/new')
def new_post():
    return render_template('new.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)
