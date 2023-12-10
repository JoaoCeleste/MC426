from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FieldList, FormField, SubmitField
from wtforms.validators import DataRequired

class IngredientForm(FlaskForm):
    ingredient_name = StringField('Nome', validators=[DataRequired()])
    quantity = StringField('Quantidade', validators=[DataRequired()])

class RecipeForm(FlaskForm):
    name = StringField('Nome', validators=[DataRequired()])
    instruction = TextAreaField('Instruções', validators=[DataRequired()])
    ingredients = FieldList(FormField(IngredientForm), min_entries=1)
    submit = SubmitField('Cadastrar')