from flask import flash, redirect, render_template, request, url_for

from flask_site import app
from flask_site.forms import SelectForm
from flask_site.utils import calculate_saving

@app.route('/info', methods=['GET', 'POST'])
def info():
    """Display page showing CO2 savings"""
    meat = request.args.get('meat')
    alternative = request.args.get('alternative')
    saving = request.args.get('saving')
    return render_template('info.html', meat=meat, alternative=alternative, 
                                saving=saving)

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = SelectForm()
    if form.validate_on_submit():
        meat = form.food_select.data
        alternative = form.alternative_select.data
        saving = calculate_saving(meat, alternative)
        flash(f'Submitted choice is {meat}')
        return redirect(url_for('info', meat=meat, alternative=alternative, 
                                saving=saving))
    else:
        return render_template('index.html', title='Home', form=form)
