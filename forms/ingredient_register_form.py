from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FieldList, FormField, SubmitField
from wtforms.validators import DataRequired

class IngredientForm(FlaskForm):
    ingredient_name = StringField('Nome', validators=[DataRequired()])
    calories = StringField('Calorias', validators=[DataRequired()])
    proteins = StringField('Proteínas', validators=[DataRequired()])
    fats = StringField('Gorduras', validators=[DataRequired()])
    carbohydrates = StringField('Carboidratos', validators=[DataRequired()])
    submit = SubmitField('Cadastrar')