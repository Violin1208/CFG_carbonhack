from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField #, StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class SelectForm(FlaskForm):
    meats = ['Chicken', 'Beef']
    alternatives = ['Tofu', 'Quorn']
    food_select = SelectField('Meat', choices = meats)
    alternative_select = SelectField('Alternative', choices = alternatives, validate_choice=True)
    submit = SubmitField('Submit')