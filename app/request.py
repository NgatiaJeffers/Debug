import urllib.request, json
from .models import Album, Tracks
from flask import jsonify

# Getting api key
api_key = None
base_url = None
tracks_url = None

def configure_request(app):
    global api_key, base_url, tracks_url
    api_key = app.config['LAST_API_KEY']
    base_url = app.config["BASE_URL"]
    tracks_url = app.config["TRACKS_URL"]


Album = Album

def get_music(category):
    '''
    Function that gets the jason response to our url request
    '''

    get_music_url = base_url.format(category, api_key)

    with urllib.request.urlopen(get_music_url) as url:
        get_music_data = url.read()
        music_object = json.loads(get_music_data)

        # print(music_object)

        music_results = None

        if music_object['topalbums']:
            music_list = jsonify(music_object['topalbums'])
            music_json = json.dumps(music_list.data).decode('utf8')
            print(music_json)
            # print(dir(music_list))
            music_results = process_results(music_list)

    return music_results


def process_results(music_list):
    # print(music_list)
    # music_results = []
    for att in music_list:
        for item in att:

            print(type(item))
            id = item['mbid']
            name = item['name']
            url = item['url']
            urlToImage = item['UrlToImage']
            playcount = item['playcount']
            listeners = item['listeners']

            music_object = Album(id, name, url, urlToImage, playcount, listeners)
            music_results.append(music_object)

    return music_results



def get_tracks():
    '''
    Function that gets the track News.
    '''

    tracks_songs_url = tracks_url.format(api_key)

    with urllib.request.urlopen(tracks_songs_url) as url:
        track_data = url.read()
        track_response = json.loads(track_data)
        track_results = None
        
        if track_response['track']:
            track_results_list = track_response['track']
            track_results = process_track_results(track_results_list)

    return track_results

def process_track_results(track_results_list):
    '''
    Function that will convert the data being pulled to a json file
    '''
    track_results = []
    for item in track_results_list:
        id = item.get('mbid')
        name = item.get('name')
        url = item.get('url')
        urlToImage = item.get('UrlToImage')
        playcount = item.get('playcount')
        listeners = item.get('listeners')

        track_object = Tracks(id, name, url, urlToImage, playcount, listeners)
        track_results.append(track_object)

    return track_results

