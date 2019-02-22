from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import Form,StringField, PasswordField, BooleanField, IntegerField, \
    TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(),Length(max=255)])
    text = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Save')
