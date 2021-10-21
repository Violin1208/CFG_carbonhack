from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField #, StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask_site.static_data.food_dict import info, foods, drinks
# previous:
# class SelectForm(FlaskForm):
#     meats = info.keys()
#     alternatives = info.keys()
#     food_select = SelectField('Primary Food', choices = meats)
#     alternative_select = SelectField('Alternative', choices = alternatives, validate_choice=True)
#     submit = SubmitField('Submit')

# new
class SelectForm(FlaskForm):
    food1 = foods.keys()
    drink1 = drinks.keys()
    food2 = foods[food1].keys()
    drink2 = drinks[drink1].keys()
    food1_select = SelectField('Initial Food Choice', choices=food1)
    drink1_select = SelectField('Initial Drink Choice', choices=drink1, validate_choice=False)
    food2_select = SelectField('Alternative Food Choice', choices=food2)
    drink2_select = SelectField('Alternative Drink Choice', choices=drink2, validate_choice=False)
    submit = SubmitField('Submit')
    submit = SubmitField('Submit')
