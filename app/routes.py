from app import app
from app.forms import LoginForm
from flask import render_template, flash, redirect, url_for

# home page
@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html')

# login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(
            'Login requested for user {}, remember_me={}'.format(
                form.username.data, form.remember_me.data
            )
        )
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

# single-album recommendation page
@app.route('/album')
def album():
    album = {
        'name': 'Metaprogramação',
        'artist': 'Deaf Kids'
    }
    return render_template('album.html', title='Album', album=album)

# multiple-album recommendation page
@app.route('/albums')
def albums():
    albums = [
        {
            'name': 'Metaprogramação',
            'artist': 'Deaf Kids'
        },
        {
            'name': 'The Dance of the Moon and the Sun',
            'artist': 'Natural Snow Buildings'
        },
        {
            'name': 'Charli',
            'artist': 'Charli XCX'
        }
    ]
    return render_template('albums.html', albums=albums)
