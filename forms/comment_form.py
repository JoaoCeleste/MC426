from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired

class CommentForm(FlaskForm):
    comment = TextAreaField('Comentário', validators=[DataRequired()])
    submit = SubmitField('Comentar')