from app import app
from flask import render_template

# home page
@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html')

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
