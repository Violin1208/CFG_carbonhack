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

# primary food options

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = SelectForm()
    if form.validate_on_submit():
        prifood = form.food1_select.data
        pridrink = form.drink1_select.data
        saving = calculate_saving(prifood, pridrink)
        flash(f'Submitted choice is {prifood}{pridrink}')
        return redirect(url_for('info', prifood=prifood, pridrink=pridrink,
                                saving=saving))
    else:
        return render_template('index.html', title='Home', form=form)
# swap page
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index2():
    form = SelectForm()
    if form.validate_on_submit():
        meat = form.food1_select.data
        alternative = form.drink1_select.data
        saving = calculate_saving(meat, alternative)
        flash(f'Submitted choice is {meat}')
        return redirect(url_for('info', meat=meat, alternative=alternative,
                                saving=saving))
    else:
        return render_template('index.html', title='Home', form=form)
