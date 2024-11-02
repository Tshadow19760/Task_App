from app import app
from flask import render_template

import forms

@app.route('/', methods=['GET', 'POST'])
@app.route('/about', methods=['GET', 'POST'] )
def index():
    form = forms.AddTaskForm()
    if form.validate_on_submit():
        print('Submitted title', form.title.data)
    return render_template('about.html', form=form)
    

@app.route('/title', methods=['GET', 'POST'])
def about():
    form = forms.AddTaskForm()
    if form.validate_on_submit():
        print('Submitted title', form.title.data)
        return render_template('title.html', current_title='Custom Title', form=form, title=form.title.data)
    return render_template('title.html', current_title='Custom Title', form=form)
