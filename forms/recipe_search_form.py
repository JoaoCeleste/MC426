from flask_wtf import FlaskForm
from wtforms import StringField, FieldList, SubmitField
from wtforms.validators import DataRequired

class RecipeSearchByIngredientsForm(FlaskForm):
    ingredients = FieldList(StringField('Nome', validators=[DataRequired()]), min_entries=1)
    submit = SubmitField('Buscar')

class RecipeSearchByNameForm(FlaskForm):
    name = StringField('Nome', validators=[DataRequired()])
    submit = SubmitField('Buscar')