from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField #, StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask_site.static_data.food_dict import info

class SelectForm(FlaskForm):
    meats = info.keys()
    alternatives = info.keys()
    food_select = SelectField('Meat', choices = meats)
    alternative_select = SelectField('Alternative', choices = alternatives, validate_choice=True)
    submit = SubmitField('Submit')