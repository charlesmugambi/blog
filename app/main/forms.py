from wtforms import StringField,TextAreaField,SelectField,SubmitField
from wtforms.validators import Required
from flask_wtf import FlaskForm

class PostForm(FlaskForm):

    title = StringField('Title', validators=[Required()])
    text = TextAreaField('Text', validators=[Required()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Bio.', validators=[Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    text = TextAreaField('Leave a comment:',validators=[Required()])
    submit = SubmitField('Submit')