from flask import Flask,render_template,redirect, url_for, abort, flash
from flask_sqlalchemy import SQLAlchemy
from form import PostForm
# from flask_wtf import FlaskForm
# from flask_wtf.file import FileField, FileRequired, FileAllowed
# from wtforms import Form,StringField, PasswordField, BooleanField, IntegerField, \
#     TextAreaField, SubmitField
# from wtforms.validators import DataRequired, Length, ValidationError

app = Flask(__name__)
app.config['SECRET_KEY'] = 'abcdefg'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/ingo/Documents/myblog/blog.db'

db = SQLAlchemy(app)


class Blogpost(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(50))
    # subtitle = db.Column(db.String(50))
    # author = db.Column(db.String(20))
    date_posted = db.Column(db.DateTime)
    content = db.Column(db.Text)

@app.route('/')
def index():
    entries = Blogpost.query.all()
    return render_template('index.html',entries=entries)

@app.route('/post')
def post():
    return render_template('post.html')

@app.route('/new',methods=['GET','POST'])
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        print("yes")
        blogpost = Blogpost()
        blogpost.title = form.title.data
        print(form.title.data)
        blogpost.content = form.text.data
        db.session.add(blogpost)
        db.session.commit()
        flash('success')
        return redirect(url_for('index'))
    return render_template('new.html',form=form)
    # return render_template('new.html')

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
