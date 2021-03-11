from . import main
from .. import mysql,db
from ..request import get_music
from flask import render_template


# Views
@main.route('/album')
def album():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular movie
    album = get_music('gettopalbums')

    title = 'Home - Welcome to Chill'

    return render_template('index.html', title = title, albums = album)


@main.route('/')
def index():
	return render_template("album.html")


@main.route('/black')
def black():
    return render_template('black.html')